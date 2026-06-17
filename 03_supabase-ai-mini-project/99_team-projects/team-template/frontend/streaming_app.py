import json
import os

import httpx
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8001")

st.set_page_config(page_title="SSE Streaming Chat", layout="centered")
st.title("SSE 실시간 AI 응답 스트리밍")
st.caption(f"API_BASE_URL: {API_BASE_URL}")


def parse_sse_line(line: str) -> dict | None:
    if not line.startswith("data: "):
        return None

    raw_data = line.removeprefix("data: ").strip()
    if not raw_data:
        return None

    return json.loads(raw_data)


def stream_answer(message: str):
    answer_area = st.empty()
    final_answer = ""

    with httpx.stream(
        "POST",
        f"{API_BASE_URL}/api/chat/stream",
        json={"message": message},
        timeout=30.0,
    ) as response:
        response.raise_for_status()

        for line in response.iter_lines():
            event = parse_sse_line(line)
            if event is None:
                continue

            if event["type"] == "chunk":
                final_answer += event["content"]
                answer_area.markdown(final_answer)

            if event["type"] == "done":
                final_answer = event["content"]
                answer_area.markdown(final_answer)
                return final_answer

    return final_answer


message = st.text_area("질문", value="Supabase와 SSE는 어떤 역할이 다른가요?")

if st.button("스트리밍 응답 받기"):
    if not message.strip():
        st.warning("질문을 입력해 주세요.")
    else:
        try:
            with st.status("AI 응답을 스트리밍으로 받는 중입니다.", expanded=True):
                final = stream_answer(message)
                st.write("스트리밍 완료")

            st.success("최종 응답이 완성되었습니다.")
            st.info("실제 프로젝트에서는 이 최종 응답을 Supabase messages 테이블에 저장합니다.")
            st.code(final)
        except httpx.HTTPError as error:
            st.error(f"스트리밍 요청 실패: {error}")
