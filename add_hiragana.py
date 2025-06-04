import json
import pykakasi

# Khởi tạo Kakasi
kks = pykakasi.kakasi()

# Hàm chuyển Kanji/Katakana thành Hiragana
def to_hiragana(text):
    result = kks.convert(text)
    return ''.join([item['hira'] for item in result])

# Đọc file JSON đã có lời nói gốc
with open("words_with_translation.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

# Thêm hiragana cho từng câu
for seg in segments:
    seg["hiragana"] = to_hiragana(seg["text"])
    # Nếu bạn có từng từ riêng lẻ:
    for word in seg.get("words", []):
        word["hiragana"] = to_hiragana(word["word"])

# Ghi lại file JSON với thông tin hiragana
with open("words_with_hiragana.json", "w", encoding="utf-8") as f:
    json.dump(segments, f, ensure_ascii=False, indent=2)

print("✅ Đã thêm Hiragana vào words_with_hiragana.json")