async function process() {
  const urlInput = document.getElementById("youtubeUrl");
  const status = document.getElementById("status");
  const url = urlInput.value;

  if (!url) {
    alert("Vui lòng nhập URL YouTube");
    return;
  }

  status.textContent = "Đang xử lý...";

  try {
    const res = await fetch("http://localhost:5000/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });

    const data = await res.json();

    if (data.status === "success") {
      status.textContent = "✅ Xử lý thành công!";
      document.getElementById('audio').src = "/audio"; // giả sử backend trả về đường dẫn audio
      renderKaraoke(data.subtitles);
    } else {
      status.textContent = "❌ Lỗi: " + (data.error || "Không xác định");
    }
  } catch (e) {
    status.textContent = "❌ Lỗi kết nối tới API";
    console.error(e);
  }
}

function renderKaraoke(segments) {
  const lyricsDiv = document.getElementById('lyrics');
  lyricsDiv.innerHTML = '';

  segments.forEach(seg => {
    const p = document.createElement('div');
    p.className = 'sentence';

    (seg.words || []).forEach(wordData => {
      const span = document.createElement('span');
      span.className = 'word';
      span.textContent = wordData.word;
      span.dataset.start = wordData.start;
      span.dataset.end = wordData.end;

      // Hiển thị Hiragana
      const hiragana = document.createElement('div');
      hiragana.className = 'hiragana';
      hiragana.textContent = wordData.hiragana || "";
      span.appendChild(hiragana);

      p.appendChild(span);
    });

    // Hiển thị bản dịch của cả câu
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = seg.translation || "";
    p.appendChild(tooltip);

    lyricsDiv.appendChild(p);
  });

  setupHighlighting();
}

function setupHighlighting() {
  const audio = document.getElementById('audio');
  audio.addEventListener('timeupdate', () => {
    const currentTime = audio.currentTime;
    document.querySelectorAll('.word').forEach(span => {
      const start = parseFloat(span.dataset.start);
      const end = parseFloat(span.dataset.end);

      if (currentTime >= start && currentTime <= end) {
        span.classList.add('highlight');
      } else {
        span.classList.remove('highlight');
      }
    });
  });
}