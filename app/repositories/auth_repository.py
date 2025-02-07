from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import User
from app.core.security import get_password_hash
from fastapi import HTTPException, status

class AuthRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_username(self, username: str) -> User:
        result = await self.db.execute(select(User).where(User.username == username))
        return result.scalars().first()

    async def create_user(self, username: str, hashed_password: str, role: str = "user") -> User:
        user = User(username=username, hashed_password=hashed_password, role=role)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete_user(self, username: str):
        result = await self.db.execute(select(User).where(User.username == username))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        await self.db.delete(user)
        await self.db.commit() 