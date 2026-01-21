from .interface import Repository, Item
from typing import List

class Operation(Item):
    id: int
    name: str
    description: str

class InMemoryOperationsRepository(Repository):
    items: List[Operation]
    
    def __init__(self):
        self.items = [
            Operation(id=1,name="My first Op", description="dummy 1"), 
            Operation(id=2,name="My second Op",description="dummy 2"), 
            Operation(id=3,name="My third op", description="dummy 3")
        ]

    def get_all(self):
        return self.items
    
    def add(self, item: Operation):
        self.items.append(item)

    def get_by_id(self, id):
        for x in self.items:
            if x.id == id:
                return x
        return None