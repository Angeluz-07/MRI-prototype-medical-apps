from fastapi import APIRouter
from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


from src.context import auth_service, auth_backend

router = APIRouter(prefix="/auth", tags=["Auth"])

# Esquema para Swagger
security = HTTPBearer()


# 3. Schemas para Endpoints
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# 2. Modelos y Repositorio
class UserRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str  # En memoria será el hash


@router.post("/login")
def login(login_schema: LoginRequest):
    authorized = auth_service.is_user_authorized(login_schema)

    if not authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas"
        )

    user = auth_service.get_user_by_email(login_schema.email)
    # AuthX genera el token usando el ID del usuario
    token = auth_backend.create_access_token(uid=user.id)
    return {"access_token": token, "token_type": "bearer"}


# 5. Ruta Protegida
@router.get("/me")
def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(security),
    payload=Depends(auth_backend.access_token_required),
):
    user_id = payload.sub
    user = auth_service.get_user_by_id(user_id)
    return {"username": user.username, "email": user.email, "id": user.id}
