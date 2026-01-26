from src.repository.execution import InMemoryExecutionRepository

def get_executions():
    return InMemoryExecutionRepository().get_all()