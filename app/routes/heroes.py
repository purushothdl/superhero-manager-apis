from fastapi import APIRouter, Depends
from typing import List
from app.services.hero_service import HeroService
from app.dependencies.service_dependencies import get_hero_service
from app.schemas.hero_schemas import HeroResponse, MissionResponse
from app.dependencies.auth_dependencies import get_current_user

router = APIRouter(tags=["heroes"], prefix="/heroes")

@router.get("/missions", response_model=List[MissionResponse])
async def get_missions(
    hero_service: HeroService = Depends(get_hero_service),
    current_user: dict = Depends(get_current_user)
):
    """Get all missions from the database"""
    return await hero_service.get_all_missions()

@router.get("/missions/{mission_id}", response_model=MissionResponse)
async def get_mission(
    mission_id: int,
    hero_service: HeroService = Depends(get_hero_service),
    current_user: dict = Depends(get_current_user)
):
    """Get a specific mission by ID"""
    return await hero_service.get_mission_by_id(mission_id)

@router.get("/", response_model=List[HeroResponse])
async def get_heroes(
    hero_service: HeroService = Depends(get_hero_service),
    current_user: dict = Depends(get_current_user)
):
    """Get all heroes from the database"""
    return await hero_service.get_all_heroes()

@router.get("/{hero_id}", response_model=HeroResponse)
async def get_hero(
    hero_id: int,
    hero_service: HeroService = Depends(get_hero_service),
    current_user: dict = Depends(get_current_user)
):
    """Get a specific hero by ID"""
    return await hero_service.get_hero_by_id(hero_id)