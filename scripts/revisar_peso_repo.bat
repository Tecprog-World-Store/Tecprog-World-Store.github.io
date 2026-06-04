@echo off
setlocal
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$paths=@('assets/img','assets/pdf','data','catalogo','lineas'); foreach($p in $paths){ if(Test-Path $p){ $bytes=(Get-ChildItem $p -Recurse -File | Measure-Object Length -Sum).Sum; '{0,-14} {1,10:N2} MB' -f $p, ($bytes/1MB) } }"
endlocal
