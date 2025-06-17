import fugashi

def tokenize_japanese(text):
    tagger = fugashi.Tagger()
    words = []

    for word in tagger(text):
        surface = word.surface
        feature = word.feature.split(',')

        pos = feature[0]  # Loại từ: danh từ, động từ...
        meaning = feature[5] if len(feature) > 6 else None

        words.append({
            "surface": surface,
            "pos": pos,
            "meaning": meaning
        })

    return words