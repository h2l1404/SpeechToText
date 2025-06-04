import whisper
import json

# Load mô hình Whisper (chỉ dùng small trở lên để có word_timestamps)
model = whisper.load_model("small")  # hoặc "medium", "large" nếu có GPU

# Chuyển đổi âm thanh thành văn bản với thời gian từng từ
result = model.transcribe("audio.wav", language="ja", word_timestamps=True)

# Lưu kết quả dưới dạng JSON
with open("words.json", "w", encoding="utf-8") as f:
    json.dump(result["segments"], f, ensure_ascii=False, indent=2)

print("✅ Đã lưu phụ đề theo từng từ vào words.json")