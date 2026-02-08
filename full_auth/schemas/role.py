from pydantic import BaseModel
from .permission import PermissionRead
class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
   
    permissions:list[int]


class RoleRead(RoleBase):
    id: int
    permissions: list[PermissionRead]

    class Config:
        orm_mode = True