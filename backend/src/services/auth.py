from pwdlib import PasswordHash
from src.domain.models import User

# 1. Configuración de Seguridad
password_helper = PasswordHash.recommended()




def add_user(user_repository, user_register_schema):
    user = User(
        username=user_register_schema.username,
        email=user_register_schema.email,
        password=user_register_schema.password,
    )
    user_repository.add(user)
    return user
    # user.id = user.id or str(uuid.uuid4())
    # user.password = password_helper.hash(user.password) # Hasheo automático al añadir


class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def is_user_authorized(self, login_schema):
        user = self.user_repository.get_by_email(login_schema.email)
        # if not user or not password_helper.verify(credentials.password, user.password):
        return user and user.password == login_schema.password

    def get_user_by_email(self, email):
        return self.user_repository.get_by_email(email)

    def get_user_by_id(self, id):
        return self.user_repository.get_by_id(id)
