"""Migración monetaria reproducible; conserva importes históricos y no consulta la red."""
import json
import re
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TC = Decimal('3.360')
VERSION = '20260909-2b'
USD_KEYS = ('precio_base_usd', 'precio_usd_base', 'precio_dolares', 'precio_internacional_usd', 'precio_internacional_desde_usd', 'precio_exterior_usd', 'precio_usd')
PEN_KEYS = ('precio_soles', 'precio_publico', 'precio_peru_igv_soles', 'precio_desde_soles_igv', 'precio_peru_desde_soles', 'precio_final_soles_con_igv', 'precio_soles_igv', 'precio_material_soles', 'precio_peru_soles_igv', 'precio_desde', 'precio')

def load(name):
    return json.loads((ROOT / 'data' / (name + '.json')).read_text(encoding='utf-8'))

def save(name, value):
    (ROOT / 'data' / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def numeric(value):
    if isinstance(value, (float, int)) and not isinstance(value, bool):
        return Decimal(str(value))
    if isinstance(value, str):
        found = re.findall(r'(?<!\w)\d[\d,]*(?:\.\d+)?', value)
        if len(found) == 1:
            return Decimal(found[0].replace(',', ''))
    return None

def first(item, keys):
    for key in keys:
        value = numeric(item.get(key))
        if value is not None:
            return value
    return None

def calculate(base):
    base = Decimal(str(base)).quantize(Decimal('.01'), rounding=ROUND_CEILING)
    if base < 0:
        raise ValueError('Precio negativo')
    raw = (base + Decimal('.30')) / Decimal('.946') if base else Decimal(0)
    final = raw.to_integral_value(rounding=ROUND_CEILING) if raw < 20 else ((raw-9)/10).to_integral_value(rounding=ROUND_CEILING)*10+9
    return {'precio_base_usd': float(base), 'precio_paypal_calculado_usd': float(raw.quantize(Decimal('.000001'), rounding=ROUND_CEILING)), 'precio_venta_usd': int(final)}

# Horas mínimas estimadas para entregables iniciales; USD 75/h en ingeniería.
INTERACTIVE = [
    (2, 'Revisión de una cuenca y de hasta tres series aportadas; nota de diagnóstico hidrológico.'),
    (3, 'Plan de aforo para una sección y revisión de un registro aportado; sin campaña de campo.'),
    (3, 'Revisión de un levantamiento aportado, sistema de referencia y control básico de coordenadas.'),
    (4, 'Revisión de una nube batimétrica aportada y plan de control de calidad; sin embarcación ni medición.'),
    (4, 'Revisión preliminar de una serie marina aportada y nota de criterios de análisis.'),
    (4, 'Revisión de un modelo existente y diagnóstico de configuración de un escenario; sin estudio integral.'),
    (4, 'Revisión documental preliminar de una estructura costera y nota de criterios de diseño.'),
    (3, 'Revisión de un registro visual subacuático aportado y plan de inspección; sin buceo ni movilización.'),
    (3, 'Revisión de un expediente ambiental y lista de información necesaria para su siguiente etapa.'),
    (3, 'Diagnóstico documental de un trámite sectorial y lista de requisitos; sin tasas ni representación.'),
    (3, 'Identificación preliminar de riesgos de un sitio a partir de información aportada.'),
    (4, 'Revisión de supuestos de inversión y esquema preliminar de evaluación de un proyecto.'),
    (4, 'Diagnóstico de un flujo de datos y diseño de una prueba de integración digital.'),
    (3, 'Revisión de un proceso logístico y propuesta preliminar de indicadores y mejoras.'),
]

def apply(item, base, origin, scope='', variable=False):
    item.update(calculate(base))
    item['moneda_publica'] = 'USD'
    item['precio_desde_usd'] = bool(variable)
    item['precio_texto_usd'] = 'Gratis' if not item['precio_venta_usd'] else ('Desde ' if variable else '') + f"USD {item['precio_venta_usd']}"
    item['precio_origen'] = origin
    item['precio_version'] = VERSION
    if scope:
        item['alcance_precio_desde'] = scope
    return item

def normalize(item, source):
    if item.get('precio_version') == VERSION:
        return item
    typ = str(item.get('tipo_item', item.get('tipo', ''))).lower()
    is_course = 'curso' in typ or source in ('catalogo-general-cursos','cursos','cursos/2026-06','cursos_tw_educa')
    base = first(item, USD_KEYS)
    pen = first(item, PEN_KEYS)
    origin = 'USD histórico'
    scope = ''
    variable = is_course or any(t in typ for t in ('servicio','proyecto','consultor')) or source.startswith('catalogo-tw-')
    if str(item.get('precio', '')).lower() == 'gratis':
        base = Decimal(0)
    if base is None and pen is not None:
        base = pen / TC
        origin = 'PEN / 3.360; SBS venta 2026-09-08 vía BCRP'
        item['precio_conversion_usd_sin_redondear'] = str(base)
    if base is None:
        raise ValueError(f"Falta decisión de precio: {source}: {item.get('id',item.get('nombre'))}")
    if variable and base:
        scope = item.get('alcance_precio_desde') or 'Modalidad inicial publicada; revisa los entregables y condiciones de esta ficha.'
    apply(item, base, origin, scope, variable)
    if is_course and item.get('visible_cliente') is not False:
        item['estado_publico'] = 'Matrícula abierta'
    return item

def normalize_file(name):
    value = load(name)
    for item in value:
        normalize(item, name)
    save(name, value)

def migrate():
    # Bases explícitas para los servicios sin precio histórico.
    interactive = load('tw-interactive')
    for item, (hours, scope) in zip(interactive['servicios'], INTERACTIVE, strict=True):
        apply(item, hours*75, f'Estimación: {hours} h × USD 75/h; referencias WPE/BCP Consulting', scope, True)
    save('tw-interactive', interactive)
    salud = load('tw-salud')
    for item in salud['servicios']:
        normalize(item,'catalogo-tw-salud')
    save('tw-salud',salud)
    # Las tarifas USD vigentes por perfil/etapa conservan su base histórica.
    intl = load('precios_internacionales_tw_educa')
    index = {}
    for course in intl['cursos']:
        for profile in course['perfiles']:
            for stage in ('preventa','lanzamiento','regular'):
                profile.setdefault(stage+'_base_usd', profile[stage+'_usd'])
                profile[stage+'_venta_usd'] = calculate(profile[stage+'_base_usd'])['precio_venta_usd']
        index[course['curso_id']] = course
    save('precios_internacionales_tw_educa',intl)
    courses=load('cursos_tw_educa')
    for course in courses:
        profiles=index[course['id']]['perfiles']
        base=min(p[s+'_base_usd'] for p in profiles for s in ('preventa','lanzamiento','regular'))
        apply(course,base,'Mínimo USD histórico por perfil/etapa',variable=True)
        course['estado_publico']='Matrícula abierta'
        for p,u in zip(course['precios'],profiles,strict=True):
            assert p['publico']==u['publico']
            for stage in ('preventa','lanzamiento','regular'):
                p[stage+'_venta_usd']=u[stage+'_venta_usd']
    save('cursos_tw_educa',courses)
    # El resto conserva valores originales. No cruza IDs con productos_store.
    for name in ('productos_store','materiales','guias','compendios','cursos','ofertas','precios','cursos/2026-06'):
        normalize_file(name)
    payments=load('pagos')
    for item in payments:
        if item['id']=='reserva-proyecto-software':
            apply(item,100,'Estimación: 2 h × USD 50/h; WPE','Sesión de requisitos y resumen funcional inicial. No incluye desarrollo.',True)
        else:normalize(item,'pagos')
    save('pagos',payments)
    global_items=load('catalogo_global')
    courses_by_id={c['id']:c for c in courses}
    interactive_by_id={s['id']:s for s in interactive['servicios']}
    aliases={'tw-educa-001':'tw-educa-curso-20','tw-educa-002':'tw-educa-curso-21','tw-educa-003':'tw-educa-curso-22','tw-educa-004':'tw-educa-curso-23','tw-educa-005':'tw-educa-curso-24','tw-educa-006':'tw-educa-curso-29'}
    for item in global_items:
        ident=item['id'];source=courses_by_id.get(ident) or courses_by_id.get(aliases.get(ident)) or interactive_by_id.get(ident)
        if source:
            for key,value in source.items():
                if key.startswith('precio_') and key not in ('precio_soles','precio_dolares'):item[key]=value
            item['moneda_publica']='USD'
            if item.get('tipo_item')=='curso':item['estado_publico']='Matrícula abierta'
            continue
        if first(item,USD_KEYS) is not None or first(item,PEN_KEYS) is not None:
            normalize(item,'catalogo_global');continue
        if ident=='tw-store-014':
            item['nombre']='Meta Quest 3 512GB'
            apply(item,Decimal(3999)/TC,'Krear3D: PEN 3999; contraste Storeplay PEN 2590','Equipo de 512GB bajo pedido; entrega y garantía se coordinan antes del pago.')
            continue
        if ident=='tw-disfruta-004':
            apply(item,Decimal(100)/TC,'Referencia impresión 3D POLYTEC: piezas PEN 10–100+','Figura pequeña en PLA, un color, desde archivo listo para imprimir; sin modelado ni pintura.',True);continue
        if ident=='tw-disfruta-005':
            apply(item,Decimal(109)/TC,'Referencia Zalo: polo personalizado PEN 89–109','Un polo con impresión de diseño suministrado; no incluye creación de marca.',True);continue
        if ident in ('tw-educa-007','tw-educa-008'):
            course_id='qgis' if ident.endswith('007') else 'openfoam-cfd'
            general=load('catalogo-general-cursos')
            matching=next((c for c in general if c['id']==course_id),None)
            if matching:
                normalize(matching,'catalogo-general-cursos');apply(item,matching['precio_base_usd'],'Tarifa histórica de formación equivalente: '+course_id,variable=True)
            else:apply(item,100,'Paquete formativo inicial: 2 h × USD 50/h; referencia WPE','Dos horas de tutoría inicial y ejercicio guiado.',True)
            item['estado_publico']='Matrícula abierta';continue
        hours=2
        if item['linea_negocio'] in ('tw-investiga','tw-salud','tw-construye','tw-inox'):hours=3
        if ident in ('tw-innova-002','tw-innova-003','tw-innova-004','tw-disfruta-001','tw-disfruta-002'):hours=4
        rate=75 if item['linea_negocio'] in ('tw-investiga','tw-salud','tw-construye','tw-inox') else 50
        scope=f"Paquete inicial para {item['nombre'].lower()}: revisión del requerimiento, sesión técnica y documento de propuesta o primer esquema. No incluye fabricación, equipos, instalación ni ejecución integral."
        if item['tipo_item']=='contenido_digital':scope='Una pieza digital inicial personalizada, con una revisión y entrega del archivo; complejidad básica.'
        apply(item,hours*rate,f'Estimación: {hours} h × USD {rate}/h; WPE/BCP Consulting',scope,True)
    save('catalogo_global',global_items)

if __name__=='__main__':
    migrate()
