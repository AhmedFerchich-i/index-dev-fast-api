from database import Base
from sqlalchemy.orm import relationship,mapped_column,Mapped
from sqlalchemy import String,ForeignKey
from typing import List 

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    roles:Mapped[List["Role"]] = relationship("Role", secondary="user_roles", back_populates="users")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"