from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str
class UserRead(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
class UserCreate(User):
    pass