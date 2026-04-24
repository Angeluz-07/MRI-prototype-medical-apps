from src.services.file import FileService
from src.services.algorithm import AlgorithmService
from src.services.execution import ExecutionService
from src.services.user import UserService
from src.services.auth import AuthService
from src.repository.execution import (
    InMemoryExecutionRepository,
    JsonExecutionRepository,
)
from src.repository.algorithm import InMemoryAlgorithmRepository
from src.repository.user import InMemoryUserRepository
from src.repository.file import FileRepository


file_service = FileService()

# execution_repository = InMemoryExecutionRepository()
execution_repository = JsonExecutionRepository()
algorithm_repository = InMemoryAlgorithmRepository()
file_repository = FileRepository()

algorithm_service = AlgorithmService(
    algorithm_repository, execution_repository, file_repository
)
execution_service = ExecutionService(execution_repository)

users_repository = InMemoryUserRepository()
user_service = UserService(users_repository)

from authx import AuthX, AuthXConfig

config = AuthXConfig(
    JWT_SECRET_KEY="SUPER_SECRET",  # Usa una clave real en prod
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_TOKEN_LOCATION=["headers"],
)

auth_backend = AuthX(config=config)
auth_service = AuthService(users_repository)
