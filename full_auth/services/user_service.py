from repos.user import UserRepo
from security import hash_password

class UserService:
    def __init__(self, user_repository: UserRepo):
        self.user_repository = user_repository

    async def create_user(self, email, password):
        if await self.user_repository.get_by_attribute(email=email):
            raise ValueError("Email already exists")
        
        hashed_password = hash_password(password)
        user = await self.user_repository.create(email=email, password=hashed_password)
        
        # --- THE COMMIT ---
        # The Service owns the transaction. We must make it permanent.
        await self.user_repository.db.commit()
        return user

    async def get_user(self, user_id):
        return await self.user_repository.get_by_id(user_id)

    async def get_user_by_email(self, email):
        return await self.user_repository.get_by_attribute(email=email)

    async def update_user(self, user_id, **kwargs):
        if "password" in kwargs:
            raise ValueError(
                "Security fields cannot be updated via update_profile. "
                "Use change_password() instead."
            )
            
        user = await self.get_user(user_id)
        if not user:
            return None
        
        updated_user = await self.user_repository.update(user, **kwargs)
        
        # --- THE COMMIT ---
        await self.user_repository.db.commit()
        return updated_user

    async def delete_user(self, user_id):
        # We check if it exists or was successful before committing
        result = await self.user_repository.delete(user_id)
        if result:
            await self.user_repository.db.commit()
        return result