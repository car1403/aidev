import os  # 환경변수에서 Gemini API key와 모델명을 읽기 위해 사용합니다.
from dataclasses import dataclass  # 응답 결과를 보기 쉬운 데이터 묶음으로 표현하기 위해 사용합니다.

import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 가져옵니다.
from dotenv import load_dotenv  # .env 파일에 적어 둔 값을 Python 환경변수로 불러오기 위해 사용합니다.

load_dotenv()  # 현재 폴더 또는 상위 폴더의 .env 파일을 읽어 환경변수로 등록합니다.

DEFAULT_MODEL = "gemini-2.5-flash-lite"  # 01~03 과정에서 기본으로 사용하는 Gemini 실습 모델입니다.


@dataclass
class ChatResult:
    answer: str  # 화면에 표시할 assistant 답변입니다.
    provider: str  # mock 응답인지 Gemini 응답인지 구분하기 위한 값입니다.
    model: str  # 어떤 모델 또는 mock 이름으로 응답했는지 보여 주는 값입니다.
    actual_api_called: bool  # 실제 외부 API를 호출했는지 확인하기 위한 값입니다.


def is_real_api_key(value):
    """자리 표시자 key인지 실제 key인지 초보자도 확인하기 쉽게 분리한 함수입니다."""
    if not value:  # 값이 비어 있으면 실제 API key가 아니므로 False를 돌려줍니다.
        return False

    normalized = value.strip().lower()  # 앞뒤 공백과 대소문자 차이를 없애 비교하기 쉽게 만듭니다.
    placeholder_values = {"", "none", "null", "test", "demo"}  # 실습용 가짜 값으로 자주 쓰는 문자열입니다.

    if normalized in placeholder_values:  # 명확한 가짜 값이면 실제 호출을 하지 않습니다.
        return False
    if normalized.startswith(("your-", "replace-", "example-", "sk-your")):  # .env 예시 문구도 실제 key가 아닙니다.
        return False

    return len(normalized) >= 20  # 실제 key는 보통 충분히 길기 때문에 아주 짧은 값은 제외합니다.


def create_mock_reply(prompt, reason):
    """Gemini key가 없거나 오류가 날 때 화면 흐름을 계속 확인할 수 있게 mock 응답을 만듭니다."""
    return ChatResult(
        answer=f"mock 응답입니다. '{prompt}' 질문을 화면에 표시하는 흐름을 확인했습니다. ({reason})",
        provider="mock",
        model="mock-chat",
        actual_api_called=False,
    )


def call_gemini_or_mock(prompt):
    """Gemini API key가 있으면 실제 Gemini를 호출하고, 없으면 mock 응답으로 대체합니다."""
    api_key = os.getenv("GEMINI_API_KEY")  # .env에서 GEMINI_API_KEY 값을 읽습니다.
    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL)  # .env에 모델명이 없으면 기본 모델을 사용합니다.

    if not is_real_api_key(api_key):  # 실제 key가 없으면 외부 API 호출 없이 안전하게 mock 응답을 돌려줍니다.
        return create_mock_reply(prompt, "GEMINI_API_KEY가 없어 실제 호출을 생략했습니다.")

    try:
        from google import genai  # google-genai 패키지가 설치되어 있을 때만 Gemini SDK를 가져옵니다.
    except ImportError:
        return create_mock_reply(prompt, "google-genai 패키지가 설치되어 있지 않습니다.")

    try:
        client = genai.Client(api_key=api_key)  # API key를 사용해 Gemini 클라이언트 객체를 만듭니다.
        response = client.models.generate_content(model=model, contents=prompt)  # 모델에 사용자 질문을 보내 응답을 생성합니다.
        answer = getattr(response, "text", "") or "응답 텍스트를 찾지 못했습니다."  # 응답 객체에서 text 값을 안전하게 꺼냅니다.
        return ChatResult(answer=answer, provider="gemini", model=model, actual_api_called=True)
    except Exception as error:
        return create_mock_reply(prompt, f"Gemini 호출 중 오류가 발생했습니다: {error}")


st.title("Gemini SDK 선택 응답 표시")  # 화면의 제목을 표시합니다.
st.caption("기본은 mock 응답이며, GEMINI_API_KEY가 있을 때만 실제 Gemini API를 호출합니다.")  # 실습 기준을 안내합니다.

prompt = st.chat_input("질문을 입력하세요")  # 사용자가 입력한 질문을 prompt 변수에 저장합니다.

if prompt:  # 사용자가 질문을 입력했을 때만 아래 코드를 실행합니다.
    with st.chat_message("user"):  # 사용자 메시지를 표시할 채팅 영역을 만듭니다.
        st.write(prompt)  # 사용자가 입력한 질문을 화면에 출력합니다.

    with st.spinner("응답을 준비하는 중입니다..."):  # 응답 생성 중이라는 로딩 상태를 보여줍니다.
        result = call_gemini_or_mock(prompt)  # Gemini 또는 mock 응답을 받아 result 변수에 저장합니다.

    with st.chat_message("assistant"):  # assistant 응답을 표시할 채팅 영역을 만듭니다.
        st.write(result.answer)  # 응답 문장을 화면에 출력합니다.
        st.json(  # 어떤 방식으로 응답했는지 확인할 수 있게 메타데이터를 JSON 형태로 보여줍니다.
            {
                "provider": result.provider,
                "model": result.model,
                "actual_api_called": result.actual_api_called,
            }
        )
        if not result.actual_api_called:  # mock 응답이면 실제 API 비용이 발생하지 않았음을 안내합니다.
            st.info("실제 API 호출 없이 화면 연결 흐름을 확인했습니다.")
