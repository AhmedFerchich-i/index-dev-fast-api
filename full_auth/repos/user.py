from models import User
from .base import BaseRepo
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepo(BaseRepo[User]):
    def __init__(self, db: AsyncSession):
        
        super().__init__(db, User)

    async def get_by_email(self, email: str) -> User | None:
        
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()