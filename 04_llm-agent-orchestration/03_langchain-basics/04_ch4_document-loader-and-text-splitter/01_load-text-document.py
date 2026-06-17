"""텍스트 파일을 LangChain Document 객체로 읽어보는 예제입니다."""

from pathlib import Path

from langchain_core.documents import Document


CURRENT_DIR = Path(__file__).resolve().parent
file_path = CURRENT_DIR / "sample_policy.md"

# 간단한 수업에서는 별도 loader 없이 파일을 읽고 Document 객체를 직접 만들 수 있습니다.
if file_path.exists():
    text = file_path.read_text(encoding="utf-8")
    source = file_path.name
else:
    # 문서 정리 후 샘플 Markdown 파일이 없어도 예제가 실행되도록 기본 샘플을 사용합니다.
    text = """
    수업 운영 정책

    학생은 실습 전에 Python 가상환경을 활성화해야 합니다.
    API Key는 .env 파일에 저장하고 GitHub에 올리지 않습니다.
    Docker 실습은 Docker Desktop이 실행 중일 때만 진행합니다.
    """
    source = "inline_sample_policy"

document = Document(page_content=text, metadata={"source": source})

print("[문서 메타데이터]")
print(document.metadata)
print("\n[문서 앞부분]")
print(document.page_content[:200])
