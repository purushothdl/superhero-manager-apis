from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import Hero, Mission, User
from app.schemas.admin_schemas import HeroCreate, MissionAssign, MissionCreate
from fastapi import HTTPException, status

class AdminRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_hero(self, hero: HeroCreate) -> Hero:
        new_hero = Hero(**hero.dict())
        self.db.add(new_hero)
        await self.db.commit()
        await self.db.refresh(new_hero)
        return new_hero

    async def create_mission(self, mission: MissionCreate) -> Mission:
        new_mission = Mission(**mission.dict())
        self.db.add(new_mission)
        await self.db.commit()
        await self.db.refresh(new_mission)
        return new_mission
    
    async def assign_mission(self, mission: MissionAssign) -> Mission:
        # Fetch the mission
        result = await self.db.execute(select(Mission).where(Mission.id == mission.mission_id))
        mission_to_assign = result.scalars().first()
        if not mission_to_assign:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mission not found")

        # Explicitly load the heroes relationship
        await self.db.refresh(mission_to_assign, ["heroes"])

        # Assign heroes to the mission
        for hero_id in mission.hero_ids:
            result = await self.db.execute(select(Hero).where(Hero.id == hero_id))
            hero = result.scalars().first()
            if not hero:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Hero with ID {hero_id} not found")
            mission_to_assign.heroes.append(hero)

        await self.db.commit()
        await self.db.refresh(mission_to_assign)
        return mission_to_assign

    async def get_all_users(self) -> list[User]:
        result = await self.db.execute(select(User))
        return result.scalars().all() 