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

auth_backend = AuthX(config=config)

