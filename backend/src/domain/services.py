from src.repository.algorithm import InMemoryAlgorithmRepository

def get_algorithms():
    return InMemoryAlgorithmRepository().get_all()