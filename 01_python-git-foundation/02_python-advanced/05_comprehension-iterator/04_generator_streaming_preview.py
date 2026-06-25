"""yield를 이용해 값을 하나씩 생성하는 스트리밍 맛보기 예제입니다."""


def stream_answer_chunks(answer: str):
    """응답 문장을 단어 단위로 하나씩 생성합니다."""

    # split은 문장을 공백 기준으로 나누어 단어 목록을 만듭니다.
    words = answer.split()

    # 단어를 하나씩 꺼냅니다.
    for word in words:
        # yield는 값을 하나 반환하고 함수 실행 상태를 잠시 멈춥니다.
        # 다음 반복에서 이어서 다음 단어를 반환합니다.
        yield word


answer_text = "FastAPI SSE streaming response preview"

print("스트리밍 출력:")
for chunk in stream_answer_chunks(answer_text):
    print("chunk:", chunk)
