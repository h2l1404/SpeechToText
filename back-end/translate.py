import requests

def translate_ja_to_vi(text):
    url = "https://translate.argosopentech.com/translate" 
    payload = {
        "q": text,
        "source": "ja",
        "target": "vi"
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            return response.json()["translatedText"]
        else:
            return ""
    except Exception as e:
        print(f"Lỗi dịch: {e}")
        return ""