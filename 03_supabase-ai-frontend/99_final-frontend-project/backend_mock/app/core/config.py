import os


APP_NAME = "99 Final Frontend Project Backend"
MOCK_TOKEN_PREFIX = os.getenv("MOCK_TOKEN_PREFIX", "mock")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
ENABLE_FAKE_DELAY = os.getenv("ENABLE_FAKE_DELAY", "false").lower() == "true"
CORS_ALLOW_ORIGINS = os.getenv("CORS_ALLOW_ORIGINS", "*").split(",")
