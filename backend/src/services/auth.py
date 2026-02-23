from fastapi import FastAPI, Depends, HTTPException, status
from authx import AuthX, AuthXConfig
from pwdlib import PasswordHash
from pydantic import BaseModel, EmailStr
import uuid

# 1. Configuración de Seguridad
password_helper = PasswordHash.recommended()
config = AuthXConfig(
    JWT_SECRET_KEY="SUPER_SECRET", # Usa una clave real en prod
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_TOKEN_LOCATION=["headers"]
)
auth = AuthX(config=config)


# 2. Modelos y Repositorio
class User(BaseModel):
    id: str = None
    username: str
    email: EmailStr
    password: str # En memoria será el hash

class InMemoryUserRepository:
    def __init__(self):
        # Nota: En un caso real, estos passwords ya estarían hasheados en la DB
        self.items = [
            User(id="29a2ba2b-0db4-41bb-87b0-a5af98462a42", username="testy", email="test@example.com", password=password_helper.hash("test")),
            User(id=str(uuid.uuid4()), username="loki", email="test2@example.com", password=password_helper.hash("test2"))
        ]

    def get_by_email(self, email: str):
        return next((u for u in self.items if u.email == email), None)
    
    def get_by_id(self, id: str):
        return next((u for u in self.items if u.id == id), None)

    def add(self, user: User):
        user.id = user.id or str(uuid.uuid4())
        user.password = password_helper.hash(user.password) # Hasheo automático al añadir
        self.items.append(user)
        return user

# Inyectamos el repositorio
repo = InMemoryUserRepository()

