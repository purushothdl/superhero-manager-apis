from fastapi import HTTPException, status
from app.repositories.hero_repository import HeroRepository
from app.database.models import Hero
from app.database.models import Mission

class HeroService:
    def __init__(self, hero_repository: HeroRepository):
        self.hero_repository = hero_repository

    async def get_all_heroes(self) -> list[Hero]:
        return await self.hero_repository.get_all_heroes()
    
    async def get_hero_by_id(self, hero_id: int) -> Hero:
        return await self.hero_repository.get_hero_by_id(hero_id)
    
    async def get_all_missions(self) -> list[Mission]:
        return await self.hero_repository.get_all_missions()
    
    async def get_mission_by_id(self, mission_id: int) -> Mission:
        return await self.hero_repository.get_mission_by_id(mission_id)