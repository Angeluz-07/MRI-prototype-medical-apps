from src.services.file import FileService
from src.services.algorithm import AlgorithmService
from src.services.execution import ExecutionService
from src.repository.execution import InMemoryExecutionRepository, JsonExecutionRepository
from src.domain.filepath_manager import BASE_DIR

#execution_repository = InMemoryExecutionRepository()
execution_repository = JsonExecutionRepository(str(BASE_DIR / "data" / "executions.json"))

file_service = FileService()
algorithm_service = AlgorithmService(execution_repository)
execution_service = ExecutionService(execution_repository)