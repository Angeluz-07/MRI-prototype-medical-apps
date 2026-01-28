from src.repository.algorithm import InMemoryAlgorithmRepository
from src.repository.execution import InMemoryExecutionRepository
from src.repository.file import FileRepository
from src.domain.services import get_implementation
from src.domain.models import Execution
from src.domain.filepath_manager import WORKSPACE_DEFAULT_FOLDER

def get_algorithms():
    return InMemoryAlgorithmRepository().get_all()

def run_algorithm(algorithm_id, filename, execution_repository):
    algorithm_repo = InMemoryAlgorithmRepository()
    file_repo = FileRepository(WORKSPACE_DEFAULT_FOLDER)
    execution_repo = execution_repository

    img_full_path = file_repo.get_full_path(filename)
    algorithm = algorithm_repo.get_by_id(algorithm_id)
    
    if algorithm is None:
        raise Exception(f"unknown algorithm {algorithm_id}")
    
    fn = get_implementation(algorithm.name)
    
    try:
        exec = Execution(algorithm_id=algorithm.id)
        exec.add_log("starting")

        fn(img_full_path)
        
        exec.add_log("finished")
    except Exception:
        exec.add_log("error ocurred")
        raise
    finally:
        execution_repo.add(exec)

    return "success"
