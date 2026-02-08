from models import Role
from .base import BaseRepo
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

class RoleRepo(BaseRepo[Role]):
    def __init__(self, db: AsyncSession):
        # We pass the 'Role' model and the 'db' session up to the BaseRepo
        super().__init__(db, Role)

    async def get_by_name(self, name: str) -> Role | None:
        """Find a specific role by its name (e.g., 'admin')."""
        result = await self.db.execute(select(Role).where(Role.name == name))
        return result.scalar_one_or_none()