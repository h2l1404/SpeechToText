import json
from flask import Flask, request, jsonify
from download_audio import download_audio_from_youtube
from transcribe import transcribe_audio_with_whisper
from tokenize_jp import tokenize_japanese
from add_hiragana import add_hiragana_to_words
from translate import translate_ja_to_vi
from database import save_result, init_db
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "downloads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/process", methods=["POST"])
def process_video():
    youtube_url = request.json.get("url")
    if not youtube_url:
        return jsonify({"error": "Thiếu URL"}), 400

    try:
        # Bước 1: Tải âm thanh
        audio_path = download_audio_from_youtube(youtube_url, UPLOAD_FOLDER)

        # Bước 2: Chuyển âm thanh thành văn bản
        segments = transcribe_audio_with_whisper(audio_path)

        # Bước 3: Xử lý từng câu để phân tích từ vựng
        processed_segments = []

        for seg in segments:
            words = tokenize_japanese(seg["text"])
            words = add_hiragana_to_words(words)

            for word in words:
                word["translation"] = translate_ja_to_vi(word["surface"])

            seg["words"] = words
            seg["translation"] = translate_ja_to_vi(seg["text"])
            processed_segments.append(seg)

        # Bước 4: Lưu vào DB
        save_result(youtube_url, audio_path, processed_segments)

        return jsonify({
            "status": "success",
            "message": "Đã xử lý xong!",
            "subtitles": processed_segments
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)