import psycopg2
from config import DATABASE

def init_db():
    conn = psycopg2.connect(**DATABASE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            id SERIAL PRIMARY KEY,
            youtube_url TEXT UNIQUE,
            audio_path TEXT,
            subtitle_json JSONB
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def save_result(youtube_url, audio_path, subtitles):
    conn = psycopg2.connect(**DATABASE)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO videos (youtube_url, audio_path, subtitle_json)
        VALUES (%s, %s, %s)
        ON CONFLICT (youtube_url) DO UPDATE SET
            audio_path = EXCLUDED.audio_path,
            subtitle_json = EXCLUDED.subtitle_json
    """, (youtube_url, audio_path, json.dumps(subtitles)))
    conn.commit()
    cur.close()
    conn.close()