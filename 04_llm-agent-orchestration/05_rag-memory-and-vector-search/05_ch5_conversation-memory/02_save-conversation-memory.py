"""Docker run으로 실행한 pgvector PostgreSQL에 대화 메시지를 저장하는 예제입니다."""

from pathlib import Path
import os

from dotenv import load_dotenv
import psycopg


BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

# 04 과정에서는 PostgreSQL을 PC에 직접 설치하지 않습니다.
# 아래 기본 주소는 docker run으로 실행한 rag-pgvector 컨테이너를 가리킵니다.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://rag_user:rag_password@localhost:5433/rag_db")

session_id = "demo-session-001"
messages = [
    ("user", "LLM Agent 과정에서는 무엇을 배우나요?"),
    ("assistant", "OpenAI API, LangChain, Function Calling, RAG, LangGraph를 배웁니다."),
]

with psycopg.connect(DATABASE_URL) as conn:
    with conn.cursor() as cur:
        for role, content in messages:
            cur.execute(
                """
                INSERT INTO conversation_messages (session_id, role, content)
                VALUES (%s, %s, %s)
                """,
                (session_id, role, content),
            )
        cur.execute(
            """
            SELECT role, content, created_at
            FROM conversation_messages
            WHERE session_id = %s
            ORDER BY id
            """,
            (session_id,),
        )
        rows = cur.fetchall()
    conn.commit()

for role, content, created_at in rows:
    print(f"[{created_at}] {role}: {content}")
