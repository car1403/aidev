"""pgvector 테이블에 작은 샘플 벡터를 저장하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://rag_user:rag_password@localhost:5433/rag_db")

samples = [
    ("FastAPI", "Python API backend framework", "[0.9,0.1,0.2]"),
    ("Backend", "Server API database logic", "[0.8,0.2,0.3]"),
    ("Streamlit", "Python frontend dashboard", "[0.1,0.9,0.2]"),
]

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM sample_vectors")
        for title, content, embedding in samples:
            cur.execute(
                """
                INSERT INTO sample_vectors (title, content, embedding)
                VALUES (%s, %s, %s::vector)
                """,
                (title, content, embedding),
            )
    conn.commit()

print("샘플 벡터 저장 완료")
