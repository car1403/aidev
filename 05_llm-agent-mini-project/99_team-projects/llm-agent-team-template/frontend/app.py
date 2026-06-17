"""팀 프로젝트 Streamlit 시작 화면입니다."""

from pathlib import Path
import sys

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
BACKEND_DIR = ROOT_DIR / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from graph import run_agent  # noqa: E402


st.set_page_config(page_title="Schedule Agent", layout="wide")
st.title("복합 API 연계 일정 조정 에이전트")

user_request = st.text_area(
    "요청",
    value="김님과 이님이 가능한 30분 회의 시간을 찾아줘",
    height=120,
)

if st.button("에이전트 실행"):
    result = run_agent(user_request)
    st.subheader("최종 답변")
    st.write(result["final_answer"])
    st.subheader("State")
    st.json(result)
