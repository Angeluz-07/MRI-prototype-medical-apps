from src.repository.execution import InMemoryExecutionRepository

def get_executions(execution_repository):
    return execution_repository.get_all()