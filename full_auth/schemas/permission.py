from pydantic import BaseModel

class PermissionBase(BaseModel):
    name: str
    
class PermissionRead(PermissionBase):
    id: int

    class Config:
        orm_mode = True