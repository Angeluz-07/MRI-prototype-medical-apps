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
from src.domain.models import Algorithm
from src.domain.services import get_implementation

### Repositories
# execution_repository = InMemoryExecutionRepository()
execution_repository = JsonExecutionRepository()
algorithm_repository = InMemoryAlgorithmRepository()
file_repository = FileRepository()
users_repository = InMemoryUserRepository()


### Seed initial Data
algs = [
    Algorithm(
        name="mask_brain",
        description="Given a T1 MRI image, segment the brain and mask it",
        id="29a2ba2b-0db4-41bb-87b0-a5af98462a4e",
    ),
    Algorithm(
        name="ants_denoise",
        description="Given a T1 MRI image, denoise it with AntsPy",
        id="29a2ba2b-0db4-41bb-87b0-a5af98462a42",
    ),
    Algorithm(name="My third alg", description="dummy 3"),
]

for alg in algs:
    alg.run = get_implementation(alg.name)
    algorithm_repository.add(alg)


### Services
file_service = FileService()
algorithm_service = AlgorithmService(
    algorithm_repository, execution_repository, file_repository
)
execution_service = ExecutionService(algorithm_repository, execution_repository)
user_service = UserService(users_repository)


from authx import AuthX, AuthXConfig

config = AuthXConfig(
    JWT_SECRET_KEY="SUPER_SECRET",  # Usa una clave real en prod
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_TOKEN_LOCATION=["headers"],
)

auth_backend = AuthX(config=config)
auth_service = AuthService(users_repository)
