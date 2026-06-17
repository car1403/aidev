"""pgvector cosine distance로 비슷한 벡터를 검색하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://rag_user:rag_password@localhost:5433/rag_db")
query_vector = "[0.85,0.15,0.25]"

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT title, content, embedding <=> %s::vector AS cosine_distance
            FROM sample_vectors
            ORDER BY embedding <=> %s::vector
            LIMIT 3
            """,
            (query_vector, query_vector),
        )
        rows = cur.fetchall()

for title, content, distance in rows:
    print(f"{title} | distance={distance:.4f} | {content}")
