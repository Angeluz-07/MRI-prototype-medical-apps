from src.domain.models import Execution, ExecutionDetail
from src.repository.interfaces import Repository

class InMemoryExecutionRepository(Repository):
    
    def __init__(self):
        exec =  Execution(algorithm_id="29a2ba2b-0db4-41bb-87b0-a5af98462a4e")
        exec.add_log("testing...")
        self.items = [
           exec
        ] 

    def get_all(self):
        return self.items
    
    def add(self, item: Execution):
        self.items.append(item)

    def get_by_id(self, id):
        for x in self.items:
            if x.id == id:
                return x
        return None