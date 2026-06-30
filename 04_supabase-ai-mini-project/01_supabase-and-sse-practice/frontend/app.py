from pathlib import Path
import json
import os
import time

import httpx
import pandas as pd
import streamlit as st
from dotenv import load_dotenv


COURSE_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(COURSE_ROOT / ".env")


def api_base_url() -> str:
    return os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")


def request_json(method: str, path: str, **kwargs):
    try:
        response = httpx.request(method, f"{api_base_url()}{path}", timeout=5.0, **kwargs)
        response.raise_for_status()
        return response.json(), None
    except httpx.HTTPError as exc:
        return None, str(exc)


def parse_sse_data(line: str) -> dict | None:
    if not line.startswith("data: "):
        return None
    return json.loads(line.removeprefix("data: ").strip())


st.set_page_config(page_title="Realtime Log Dashboard", layout="wide")
st.title("AI 서비스 실시간 로그 대시보드")
st.caption("Supabase DB 저장, Redis 이벤트 전달, FastAPI SSE, Streamlit 표시 흐름을 확인합니다.")

with st.sidebar:
    st.subheader("연결")
    st.code(f"API_BASE_URL={api_base_url()}")
    if st.button("백엔드 상태 확인"):
        data, error = request_json("GET", "/health")
        if error:
            st.error(error)
        else:
            st.json(data)

left, right = st.columns([1, 2])

with left:
    st.subheader("로그 생성")
    level = st.selectbox("level", ["info", "warning", "error"])
    source = st.text_input("source", value="chat-api")
    message = st.text_area("message", value="AI 응답 생성 완료")
    latency_ms = st.number_input("latency_ms", min_value=0, value=120)
    status_code = st.number_input("status_code", min_value=100, value=200)

    if st.button("POST /logs"):
        payload = {
            "level": level,
            "source": source,
            "message": message,
            "request_path": "/chat",
            "status_code": int(status_code),
            "latency_ms": int(latency_ms),
            "metadata": {"course": "04-mini-project"},
        }
        data, error = request_json("POST", "/logs", json=payload)
        if error:
            st.error(error)
        else:
            st.success("로그를 생성했습니다.")
            st.json(data)

with right:
    st.subheader("최근 로그")
    if st.button("최근 로그 새로고침"):
        data, error = request_json("GET", "/logs")
        if error:
            st.error(error)
        elif not data:
            st.info("저장된 로그가 없습니다.")
        else:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
            if "level" in df:
                st.bar_chart(df["level"].value_counts())

st.divider()
st.subheader("SSE 실시간 로그")
st.caption("버튼을 누른 뒤 다른 창에서 로그를 생성하거나, 같은 화면에서 로그 생성 후 다시 실행해 확인합니다.")

seconds = st.slider("수신 시간(초)", min_value=3, max_value=30, value=10)
stream_box = st.empty()

if st.button("GET /stream/logs 실시간 보기"):
    events: list[dict] = []
    started = time.time()

    try:
        with httpx.stream("GET", f"{api_base_url()}/stream/logs", timeout=None) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                item = parse_sse_data(line)
                if item:
                    events.insert(0, item)
                    stream_box.dataframe(pd.DataFrame(events), use_container_width=True)
                if time.time() - started > seconds:
                    break
    except httpx.HTTPError as exc:
        st.error(f"SSE 연결 실패: {exc}")
