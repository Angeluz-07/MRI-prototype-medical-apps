from authx import AuthX, AuthXConfig
from pwdlib import PasswordHash
from src.domain.models import User

# 1. Configuración de Seguridad
password_helper = PasswordHash.recommended()

config = AuthXConfig(
    JWT_SECRET_KEY="SUPER_SECRET", # Usa una clave real en prod
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_TOKEN_LOCATION=["headers"]
)

auth_backend = AuthX(config=config)

def get_users_(user_repository):
    return user_repository.get_all()

def get_user_by_email(user_repository, email):
    return user_repository.get_by_email(email)

def add_user(user_repository, user_register_schema):
    user = User(username= user_register_schema.username,
                email=user_register_schema.email,
                password=user_register_schema.password)
    user_repository.add(user)
    return user
    # user.id = user.id or str(uuid.uuid4())
    # user.password = password_helper.hash(user.password) # Hasheo automático al añadir

def is_user_authorized(user_repository, login_schema):
    user = user_repository.get_by_email(login_schema.email)
    #if not user or not password_helper.verify(credentials.password, user.password):
    return (user and user.password == login_schema.password)
