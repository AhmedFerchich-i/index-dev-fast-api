
from repos.role import RoleRepo
class RoleService:
    def __init__(self, role_repository: RoleRepo):
        self.role_repository = role_repository

    def create_role(self, name):
        return self.role_repository.create(name)

    def get_role(self, role_id):
        return self.role_repository.get_by_id(role_id)

    def update_role(self, role_id, name):
        return self.role_repository.update(role_id, name)

    def delete_role(self, role_id):
        return self.role_repository.delete(role_id)