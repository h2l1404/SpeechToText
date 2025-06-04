import json
from googletrans import Translator

# Đọc file JSON đã có lời nói gốc
with open("words.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

# Hàm dịch bằng Google Translate
def translate(text, source_lang="ja", target_lang="vi"):
    translator = Translator()
    try:
        result = translator.translate(text, src=source_lang, dest=target_lang)
        return result.text
    except Exception as e:
        print(f"❌ Lỗi dịch [{text}]: {e}")
        return ""

# Thêm bản dịch vào từng câu
for seg in segments:
    seg["translation"] = translate(seg["text"])

# Ghi lại file JSON có bản dịch
with open("words_with_translation.json", "w", encoding="utf-8") as f:
    json.dump(segments, f, ensure_ascii=False, indent=2)

print("✅ Đã thêm bản dịch bằng Google Translate vào words_with_translation.json")