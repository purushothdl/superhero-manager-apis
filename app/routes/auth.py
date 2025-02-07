from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import verify_admin_invite_token
from app.schemas.auth_schemas import UserLogin, UserRegister, UserResponse
from app.services.auth_service import AuthService
from app.dependencies.service_dependencies import get_auth_service
from app.dependencies.auth_dependencies import get_current_user, require_admin

router = APIRouter(tags=["auth"], prefix="/auth")

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user: UserRegister,
    auth_service: AuthService = Depends(get_auth_service)
):
    if user.invite_token and not verify_admin_invite_token(user.invite_token):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or expired admin invite token",
        )
    role = "admin" if user.invite_token else "user"
    await auth_service.register_user(user.username, user.password, role)
    return {"message": f"{role.capitalize()} registered successfully"}

@router.post("/login")
async def login(
    user: UserLogin,
    auth_service: AuthService = Depends(get_auth_service)
):
    token = await auth_service.authenticate_user(user.username, user.password)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
async def get_current_user_details(user: dict = Depends(get_current_user)):
    return {"username": user.get("sub"), "role": user.get("role")}

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_current_user(
    user: dict = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service)
):
    await auth_service.delete_user(user.get("sub")) 