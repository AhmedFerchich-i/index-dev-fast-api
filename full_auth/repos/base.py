from typing import Optional, Sequence, Any
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

class BaseRepo[T: DeclarativeBase]:
    def __init__(self, db: AsyncSession, model: type[T]):
        
        self.db = db
        self.model = model

    async def get_by_id(self, id: Any) -> Optional[T]:
       
        return await self.db.get(self.model, id)

    async def get_all(self, skip: int = 0, limit: int = 100) -> Sequence[T]:
        
        result = await self.db.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def get_by_attribute(self, **kwargs: Any) -> Optional[T]:
        
        result = await self.db.execute(select(self.model).filter_by(**kwargs))
        return result.scalar_one_or_none()

    async def create(self, **kwargs: Any) -> T:
        
        obj = self.model(**kwargs)
        self.db.add(obj)
      
        await self.db.flush()
      
        await self.db.refresh(obj)
        return obj

    async def update(self, db_obj: T, **kwargs: Any) -> T:
        
        for field, value in kwargs.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)
        
        self.db.add(db_obj)
        await self.db.flush()
        await self.db.refresh(db_obj)
        return db_obj

    async def delete(self, id: Any) -> bool:
        
        obj = await self.get_by_id(id)
        if obj:
            await self.db.delete(obj)
            await self.db.flush()
            return True
        return False