from src.domain.models import Algorithm
from src.repository.interfaces import Repository

class InMemoryAlgorithmRepository(Repository):
    
    def __init__(self):
        self.items = []

    def get_all(self):
        return self.items
    
    def add(self, item: Algorithm):
        self.items.append(item)

    def get_by_id(self, id):
        for x in self.items:
            if x.id == id:
                return x
        return None