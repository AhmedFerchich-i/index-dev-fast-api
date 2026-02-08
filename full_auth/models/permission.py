from database import Base
from sqlalchemy.orm import relationship,mapped_column,Mapped
from sqlalchemy import String
from typing import List 
class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    roles:Mapped[List["Role"]] = relationship("Role", secondary="role_permissions", back_populates="permissions")

    def __repr__(self):
        return f"<Permission(id={self.id}, name='{self.name}')>"