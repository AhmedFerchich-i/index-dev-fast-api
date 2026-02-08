from database import Base
from sqlalchemy.orm import relationship,mapped_column,Mapped
from sqlalchemy import String,ForeignKey
from typing import List 


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    permissions:Mapped[List["Permission"]] = relationship("Permission", secondary="role_permissions", back_populates="roles")

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}')>"