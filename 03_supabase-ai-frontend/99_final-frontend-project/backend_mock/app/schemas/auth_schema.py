from pydantic import BaseModel, Field


class SignupRequest(BaseModel):
    email: str = Field(min_length=3, description="로그인에 사용할 이메일")
    password: str = Field(min_length=4, description="수업용 비밀번호")
    display_name: str = Field(min_length=1, description="화면에 표시할 이름")


class SigninRequest(BaseModel):
    email: str = Field(min_length=3)
    password: str = Field(min_length=4)


class UserResponse(BaseModel):
    email: str
    display_name: str


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class MessageResponse(BaseModel):
    message: str
