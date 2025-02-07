from typing import Optional
from fastapi import HTTPException, status
from app.repositories.auth_repository import AuthRepository
from app.database.models import User
from app.core.security import get_password_hash, verify_admin_invite_token, verify_password, create_access_token
from app.core.config import settings

class AuthService:
    def __init__(self, auth_repo: AuthRepository):
        self.auth_repo = auth_repo

    async def register_user(self, username: str, password: str, invite_token: Optional[str] = None) -> User:
        role = "admin" if username == settings.FIRST_ADMIN_USERNAME or (invite_token and verify_admin_invite_token(invite_token)) else "user"
        
        if await self.auth_repo.get_user_by_username(username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
        
        hashed_password = get_password_hash(password)
        return await self.auth_repo.create_user(username, hashed_password, role)

    async def authenticate_user(self, username: str, password: str) -> str:
        user = await self.auth_repo.get_user_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        return create_access_token(data={"sub": user.username, "role": user.role})

    async def delete_user(self, username: str):
        await self.auth_repo.delete_user(username) 