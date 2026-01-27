from src.domain.models import Algorithm
from src.repository.interfaces import Repository

class InMemoryAlgorithmRepository(Repository):
    
    def __init__(self):
        self.items = [
            Algorithm(name="brain_extraction", description="Extracts the brain from an mri image.", id="29a2ba2b-0db4-41bb-87b0-a5af98462a4e"), 
            Algorithm(name="My second alg",description="dummy 2"), 
            Algorithm(name="My third alg", description="dummy 3")
        ]

    def get_all(self):
        return self.items
    
    def add(self, item: Algorithm):
        self.items.append(item)

    def get_by_id(self, id):
        for x in self.items:
            if x.id == id:
                return x
        return None