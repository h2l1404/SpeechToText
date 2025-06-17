import pykakasi

kks = pykakasi.kakasi()

def add_hiragana_to_words(words):
    for word in words:
        hiragana = ''.join([x['hira'] for x in kks.convert(word["surface"])])
        word["hiragana"] = hiragana
    return words