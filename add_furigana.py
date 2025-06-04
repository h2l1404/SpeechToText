import json
from sudachipy import tokenizer, dictionary

# Khởi tạo tokenizer
tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.B  # Chia nhỏ các thành phần

def add_furigana(text):
    tokens = tokenizer_obj.tokenize(text, mode)
    result = []
    for token in tokens:
        word = token.surface()
        hiragana = token.reading_form()  # Lấy reading form (hiragana/katakana)

        # Chỉ thêm furigana nếu từ có Kanji
        if any('\u4e00' <= c <= '\u9fff' for c in word):  # Kiểm tra có chứa Kanji không
            ruby_tag = f"<ruby>{word}<rt>{hiragana}</rt></ruby>"
            result.append(ruby_tag)
        else:
            result.append(word)
    return " ".join(result)

# Đọc file JSON đã có lời nói gốc
with open("words_with_translation.json", "r", encoding="utf-8") as f:
    segments = json.load(f)

# Thêm furigana vào từng câu
for seg in segments:
    seg["furigana"] = add_furigana(seg["text"])

# Ghi lại file JSON có furigana
with open("words_with_furigana.json", "w", encoding="utf-8") as f:
    json.dump(segments, f, ensure_ascii=False, indent=2)

print("✅ Đã thêm furigana vào words_with_furigana.json")