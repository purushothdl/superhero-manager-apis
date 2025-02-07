from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.admin_schemas import HeroCreate, MissionAssign, MissionCreate
from app.services.admin_service import AdminService
from app.dependencies.auth_dependencies import require_admin
from app.dependencies.service_dependencies import get_admin_service
from app.core.security import create_admin_invite_token

router = APIRouter(tags=["admin"], prefix="/admin")

@router.post("/heroes", status_code=status.HTTP_201_CREATED)
async def create_hero(
    hero: HeroCreate,
    admin_service: AdminService = Depends(get_admin_service),
    _ = Depends(require_admin)
):
    """Create a new hero."""
    return await admin_service.create_hero(hero)

@router.post("/missions", status_code=status.HTTP_201_CREATED)
async def create_mission(
    mission: MissionCreate,
    admin_service: AdminService = Depends(get_admin_service),
    _ = Depends(require_admin)
):
    """Create a new mission."""
    return await admin_service.create_mission(mission)

@router.post("/missions/assign", status_code=status.HTTP_200_OK)
async def assign_mission(
    mission: MissionAssign,
    admin_service: AdminService = Depends(get_admin_service),
    _ = Depends(require_admin)
):
    """Assign a hero to a mission."""
    return await admin_service.assign_mission(mission)

@router.get("/users", status_code=status.HTTP_200_OK)
async def get_all_users(
    admin_service: AdminService = Depends(get_admin_service),
    _ = Depends(require_admin)
):
    """Retrieve all registered users."""
    return await admin_service.get_all_users()

@router.post("/invite-token", status_code=status.HTTP_201_CREATED)
async def generate_admin_invite_token(
    admin_service: AdminService = Depends(get_admin_service),
    _ = Depends(require_admin)
):
    """Generate an admin invite token."""
    return {"invite_token": create_admin_invite_token()}