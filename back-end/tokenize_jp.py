import fugashi

def tokenize_japanese(text):
    tagger = fugashi.Tagger()
    words = []

    for word in tagger(text):
        surface = word.surface
        feature = word.feature

        # Truy cập các trường bằng chỉ số hoặc trực tiếp
        pos = feature[0]           # POS chính (pos1)
        base_form = feature[6]      # base_form
        reading = feature[8]        # cách đọc (hiragana/katakana)
        pronunciation = feature[8]  # cách phát âm

        words.append({
            "surface": surface,
            "pos": pos,
            "base_form": base_form,
            "reading": reading,
            "pronunciation": pronunciation
        })

    return words