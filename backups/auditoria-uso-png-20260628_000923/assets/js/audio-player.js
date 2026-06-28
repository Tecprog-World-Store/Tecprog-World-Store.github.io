(function () {
  const SCRIPT_SRC = document.currentScript?.getAttribute("src") || "";
  const BASE_PREFIX = SCRIPT_SRC
    ? new URL("../../", new URL(SCRIPT_SRC, document.baseURI)).href
    : "/";
  const WIDGET_HTML = `
    <button type="button" data-audio-prev aria-label="Pista anterior">‹</button>
    <button type="button" data-audio-play aria-pressed="false">Play</button>
    <button type="button" data-audio-next aria-label="Pista siguiente">›</button>
    <span class="audio-track-title" data-audio-title>Pista --</span>
    <label class="audio-volume">
      <span class="sr-only">Volumen</span>
      <input type="range" data-audio-volume min="0" max="1" step="0.05" value="0.25" aria-label="Volumen de musica ambiental">
    </label>
    <audio data-audio-player preload="metadata"></audio>
  `;

  let state = {
    currentIndex: 0,
    playlist: [],
    userRequestedPlayback: false
  };

  function rootPath(path) {
    if (!path) return "";
    if (/^(https?:)?\/\//.test(path) || path.startsWith("data:")) return path;
    if (path.startsWith("../") || path.startsWith("./")) return path;
    return `${BASE_PREFIX}${path}`;
  }

  function ensureWidget() {
    let widget = document.querySelector("[data-audio-widget]");
    if (!widget) {
      widget = document.createElement("div");
      widget.setAttribute("data-audio-widget", "");
      widget.setAttribute("aria-label", "Reproductor de musica ambiental opcional");
      document.body.appendChild(widget);
    }

    widget.className = "audio-widget";
    widget.innerHTML = WIDGET_HTML;
    return widget;
  }

  function setStatus(widget, text) {
    const title = widget.querySelector("[data-audio-title]");
    if (title) title.textContent = text;
  }

  function setPlayButton(widget, isPlaying) {
    const play = widget.querySelector("[data-audio-play]");
    if (!play) return;
    play.textContent = isPlaying ? "Pausa" : "Play";
    play.setAttribute("aria-pressed", String(isPlaying));
  }

  function loadTrack(widget, audio, index) {
    if (!state.playlist.length) {
      audio.removeAttribute("src");
      setStatus(widget, "Sin audio");
      setPlayButton(widget, false);
      return;
    }

    state.currentIndex = (index + state.playlist.length) % state.playlist.length;
    const track = state.playlist[state.currentIndex];
    audio.src = rootPath(track.src);
    audio.load();
    setStatus(widget, track.title || `Pista ${String(state.currentIndex + 1).padStart(2, "0")}`);
    setPlayButton(widget, false);
  }

  async function playCurrent(widget, audio) {
    if (!state.playlist.length) {
      setStatus(widget, "Sin audio");
      return;
    }

    state.userRequestedPlayback = true;
    try {
      await audio.play();
      setPlayButton(widget, true);
    } catch (error) {
      console.warn("No se pudo reproducir la pista de audio.", state.playlist[state.currentIndex]?.src, error);
      setPlayButton(widget, false);
    }
  }

  async function moveTrack(widget, audio, step, shouldPlay = state.userRequestedPlayback && !audio.paused) {
    if (!state.playlist.length) return;
    audio.pause();
    loadTrack(widget, audio, state.currentIndex + step);
    if (shouldPlay) await playCurrent(widget, audio);
  }

  async function loadPlaylist() {
    try {
      const response = await fetch(rootPath("assets/audio/playlist.json"), { cache: "no-store" });
      const playlist = response.ok ? await response.json() : [];
      return Array.isArray(playlist) ? playlist.filter((track) => track?.src) : [];
    } catch (error) {
      console.warn("No se pudo cargar assets/audio/playlist.json.", error);
      return [];
    }
  }

  async function init() {
    if (document.documentElement.dataset.twAudioReady === "true") return;
    document.documentElement.dataset.twAudioReady = "true";

    const widget = ensureWidget();
    const audio = widget.querySelector("[data-audio-player]");
    const volume = widget.querySelector("[data-audio-volume]");
    if (!audio) return;

    audio.volume = Number(volume?.value || 0.25);
    state.playlist = await loadPlaylist();
    loadTrack(widget, audio, 0);

    widget.querySelector("[data-audio-play]")?.addEventListener("click", async () => {
      if (audio.paused) await playCurrent(widget, audio);
      else {
        audio.pause();
        setPlayButton(widget, false);
      }
    });

    widget.querySelector("[data-audio-next]")?.addEventListener("click", () => moveTrack(widget, audio, 1));
    widget.querySelector("[data-audio-prev]")?.addEventListener("click", () => moveTrack(widget, audio, -1));
    volume?.addEventListener("input", () => {
      audio.volume = Number(volume.value || 0.25);
    });
    audio.addEventListener("ended", () => moveTrack(widget, audio, 1, state.userRequestedPlayback));
    audio.addEventListener("error", () => {
      if (state.playlist.length > 1) moveTrack(widget, audio, 1, state.userRequestedPlayback);
      else setStatus(widget, "Sin audio");
    });
  }

  window.TWAudioPlayer = { init };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
