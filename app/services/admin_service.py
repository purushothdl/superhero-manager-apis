from fastapi import HTTPException, status
from app.repositories.admin_repository import AdminRepository
from app.database.models import Hero, Mission, User
from app.schemas.admin_schemas import HeroCreate, MissionCreate, MissionAssign

class AdminService:
    def __init__(self, admin_repo: AdminRepository):
        self.admin_repo = admin_repo

    async def create_hero(self, hero: HeroCreate) -> Hero:
        return await self.admin_repo.create_hero(hero)

    async def create_mission(self, mission: MissionCreate) -> Mission:
        return await self.admin_repo.create_mission(mission)

    async def assign_mission(self, mission: MissionAssign) -> Mission:
        return await self.admin_repo.assign_mission(mission)

    async def get_all_users(self) -> list[User]:
        return await self.admin_repo.get_all_users() 