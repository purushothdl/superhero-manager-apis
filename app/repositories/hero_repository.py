from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from app.database.models import Hero, Mission


class HeroRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_heroes(self) -> list[Hero]:
        result = await self.db.execute(select(Hero))
        return result.scalars().all()
    
    async def get_hero_by_id(self, hero_id: int) -> Hero:
        result = await self.db.execute(select(Hero).where(Hero.id == hero_id))
        hero = result.scalars().first()
        if not hero:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hero not found")
        return hero

    async def get_all_missions(self) -> list[Mission]:
        result = await self.db.execute(
            select(Mission).options(selectinload(Mission.heroes))
        )
        return result.scalars().all()
    
    async def get_mission_by_id(self, mission_id: int) -> Mission:
        result = await self.db.execute(
            select(Mission)
            .where(Mission.id == mission_id)
            .options(selectinload(Mission.heroes))
        )
        mission = result.scalars().first()
        if not mission:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mission not found")
        return mission