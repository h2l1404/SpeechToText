import whisper

def transcribe_audio_with_whisper(audio_path):
    model = whisper.load_model("small")
    result = model.transcribe(audio_path, language="ja", word_timestamps=True)
    return result["segments"]  # Có thời gian từng từ/câu