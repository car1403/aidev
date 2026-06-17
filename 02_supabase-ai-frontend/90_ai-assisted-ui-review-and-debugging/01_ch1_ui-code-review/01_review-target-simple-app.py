import streamlit as st  # Python 코드로 웹 화면을 만들기 위해 Streamlit을 st라는 별칭으로 가져옵니다.

st.title("리뷰 대상: 간단 입력 앱")  # Streamlit 화면의 가장 큰 제목을 표시합니다.

name = st.text_input("이름")  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.
score = st.number_input("점수", min_value=0, max_value=100, value=70)  # 계산 결과나 입력값을 이후 코드에서 다시 쓰기 위해 변수에 저장합니다.

if st.button("결과 보기"):  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
    if not name:  # 조건식이 True일 때만 아래 들여쓰기 블록을 실행합니다.
        st.warning("이름을 입력하세요.")  # 주의가 필요한 상황을 경고 메시지로 표시합니다.
    elif score >= 80:  # 앞 조건이 False일 때 추가 조건을 검사합니다.
        st.success(f"{name}님은 다음 단계로 넘어가도 좋습니다.")  # 작업이 성공했음을 초록색 성공 메시지로 표시합니다.
    else:  # 위 조건들이 모두 False일 때 실행할 대체 흐름입니다.
        st.info(f"{name}님은 예제를 한 번 더 수정해 보세요.")  # 다음 행동을 안내하는 정보 메시지를 표시합니다.

