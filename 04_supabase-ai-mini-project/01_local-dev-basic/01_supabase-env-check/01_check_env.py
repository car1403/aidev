import os  # 운영체제 환경변수에서 Supabase 설정값을 읽기 위해 os 모듈을 가져옵니다.

from dotenv import load_dotenv  # .env 파일의 값을 Python 환경변수로 불러오기 위해 사용합니다.


load_dotenv()  # 현재 폴더 또는 상위 실행 위치의 .env 값을 os.getenv로 읽을 수 있게 등록합니다.

REQUIRED_ENV_KEYS = [  # 미니 프로젝트를 시작하기 전에 반드시 확인해야 하는 환경변수 이름 목록입니다.
    "SUPABASE_URL",
    "SUPABASE_ANON_KEY",
    "SUPABASE_SERVICE_ROLE_KEY",
    "API_BASE_URL",
]

OPTIONAL_LLM_KEYS = [  # 실제 AI API 호출을 진행할 때 확인할 LLM 관련 환경변수입니다.
    "GEMINI_API_KEY",  # 03 과정의 기본 AI API key입니다.
    "GEMINI_MODEL",  # 사용할 Gemini 모델 이름입니다.
    "OPENAI_API_KEY",  # OpenAI 선택/비교 실습을 진행할 때만 사용합니다.
    "OPENAI_MODEL",  # OpenAI 선택/비교 실습용 모델 이름입니다.
]


def mask_value(value: str | None) -> str:  # 실제 key 전체를 화면에 출력하지 않도록 일부만 가리는 함수입니다.
    if not value:  # 값이 비어 있으면 아직 설정하지 않은 상태입니다.
        return "missing"
    if len(value) <= 8:  # 값이 너무 짧으면 일부만 보여줘도 노출 위험이 있으므로 전부 가립니다.
        return "set"
    return f"{value[:4]}...{value[-4:]}"  # 앞뒤 몇 글자만 보여줘서 설정 여부만 확인합니다.


def main() -> None:  # 스크립트를 실행했을 때 수행할 전체 확인 절차입니다.
    print("Supabase mini project environment check")
    print("-" * 42)

    missing_keys = []  # 비어 있는 환경변수 이름을 모아 마지막에 안내하기 위한 리스트입니다.
    for key in REQUIRED_ENV_KEYS:  # 필요한 환경변수를 하나씩 확인합니다.
        value = os.getenv(key)  # 환경변수 값을 읽습니다.
        print(f"{key}: {mask_value(value)}")  # 실제 비밀 값을 노출하지 않고 설정 여부만 출력합니다.
        if not value:  # 값이 없으면 누락 목록에 추가합니다.
            missing_keys.append(key)

    print("\nLLM settings")
    print("-" * 42)
    for key in OPTIONAL_LLM_KEYS:  # LLM 관련 값은 설정 여부만 확인합니다.
        value = os.getenv(key)  # key 전체를 출력하지 않기 위해 mask_value를 거칩니다.
        print(f"{key}: {mask_value(value)}")

    if missing_keys:  # 하나라도 빠진 값이 있으면 학생이 수정할 수 있게 안내합니다.
        print("\nMissing values:")
        for key in missing_keys:
            print(f"- {key}")
        print("\nCopy .env.example to .env and fill in your Supabase values.")
        return

    print("\nOK: required environment values are set.")
    print("Keep SUPABASE_SERVICE_ROLE_KEY on the backend side only.")
    print("Use Gemini API as the default LLM provider for this mini project.")
    print("Use OpenAI API only for optional comparison practice.")


if __name__ == "__main__":  # 이 파일을 직접 실행했을 때만 main 함수를 호출합니다.
    main()
