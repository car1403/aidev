# Project Workflow Tips

팀 프로젝트를 진행할 때 도움이 되는 작업 방식입니다.

## 역할 예시

- Backend 담당: FastAPI API와 Supabase 처리
- Frontend 담당: Streamlit 화면과 API 호출
- Data 담당: Supabase 테이블 설계와 SQL
- QA 담당: 실행 확인과 발표 자료 정리

## 추천 작업 순서

1. 주제 정하기
2. 화면에 필요한 데이터 정하기
3. Supabase 테이블 설계하기
4. `.env` 설정 확인하기
5. FastAPI 엔드포인트 만들기
6. Streamlit 화면 만들기
7. Supabase CRUD 동작 확인하기
8. README 실행 방법 정리하기
9. 발표 시연 준비하기

## 실행 담당자

팀원 중 한 명은 실행 방법을 계속 검증해야 합니다.

확인할 것:

- Supabase 프로젝트와 테이블 준비
- `.env` 값 설정
- FastAPI 로컬 실행
- Streamlit 로컬 실행
- README만 보고 다른 팀원이 실행 가능한지

## 범위 관리

03 과정에서는 Docker나 AWS 배포까지 욕심내기보다, Supabase 테이블과 FastAPI/Streamlit 연결을 확실히 완성하는 것이 우선입니다.
