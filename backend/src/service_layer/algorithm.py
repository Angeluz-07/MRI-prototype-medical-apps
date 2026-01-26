from src.repository.algorithm import InMemoryAlgorithmRepository
from src.repository.file import FileRepository
from src.domain.services import ALGORITHMS

def get_algorithms():
    return InMemoryAlgorithmRepository().get_all()

def run_algorithm(filename, algorithm_name):
    img_full_path = FileRepository().get_full_path(filename)
    algorithm = ALGORITHMS.get(algorithm_name)
    msg = None
    try:
        if algorithm is not None:
            algorithm(img_full_path)
            msg = f"successfully executed {algorithm_name} on {filename}"
        else:
            msg = "Unknown algorithm: ", algorithm_name
    except Exception as e:
        msg = f"Error while executing {algorithm_name} on {filename} = {e}"
        print(msg)
        raise e
    print(msg)
    return msg