from pathlib import Path

from dotenv import load_dotenv


COURSE_ROOT = Path(__file__).resolve().parents[4]
load_dotenv(COURSE_ROOT / ".env")
