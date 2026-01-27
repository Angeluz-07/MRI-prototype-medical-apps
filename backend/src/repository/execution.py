from src.domain.models import Execution
from src.repository.interfaces import Repository

class InMemoryExecutionRepository(Repository):
    
    def __init__(self):
        self.items = [
            Execution(algorithm_id="sss"), 
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