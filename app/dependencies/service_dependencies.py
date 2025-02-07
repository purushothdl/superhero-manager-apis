from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.repositories.auth_repository import AuthRepository
from app.services.auth_service import AuthService
from app.repositories.admin_repository import AdminRepository
from app.services.admin_service import AdminService
from app.services.hero_service import HeroService
from app.services.hero_service import HeroService
from app.repositories.hero_repository import HeroRepository

async def get_auth_repository(db: AsyncSession = Depends(get_db)) -> AuthRepository:
    return AuthRepository(db)

async def get_auth_service(auth_repo: AuthRepository = Depends(get_auth_repository)) -> AuthService:
    return AuthService(auth_repo)

async def get_admin_repository(db: AsyncSession = Depends(get_db)) -> AdminRepository:
    return AdminRepository(db)

async def get_admin_service(admin_repo: AdminRepository = Depends(get_admin_repository)) -> AdminService:
    return AdminService(admin_repo) 

async def get_hero_repository(db: AsyncSession = Depends(get_db)) -> HeroRepository:
    return HeroRepository(db)

async def get_hero_service(hero_repo: HeroRepository = Depends(get_hero_repository)) -> HeroService:
    return HeroService(hero_repo)