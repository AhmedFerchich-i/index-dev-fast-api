from repos.user import UserRepo
from security import hash_password
class UserService:
    def __init__(self, user_repository: UserRepo):
        self.user_repository = user_repository

    async def create_user(self, email, password):
        if await self.user_repository.get_by_attribute(email=email):
            raise ValueError("Email already exists")
        password = hash_password(password)
        return await self.user_repository.create(email=email, password=password)

    async def get_user(self, user_id):
        return await self.user_repository.get_by_id(user_id)

    async def get_user_by_email(self, email):
        return await self.user_repository.get_by_attribute(email=email)

    async def update_user(self, user_id, **kwargs):
        if "password" in kwargs  in kwargs:
           raise ValueError(
            "Security fields cannot be updated via update_profile. "
            "Use change_password() instead."
             )
        user = await self.get_user(user_id)
        if not user:
            return None
        return await self.user_repository.update(user, **kwargs)

    async def delete_user(self, user_id):
        return await self.user_repository.delete(user_id)