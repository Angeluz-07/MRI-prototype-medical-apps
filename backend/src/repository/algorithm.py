from .interface import Repository, Item
from typing import List
from src.domain.models import Algorithm
from abc import ABC, abstractmethod

# Repository Interface
class Repository(ABC):
    @abstractmethod
    def get_all(self, id: int) -> Algorithm | None:
        pass
    
    @abstractmethod
    def add(self, item: Algorithm):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Algorithm | None:
        pass

class InMemoryAlgorithmRepository(Repository):
    
    def __init__(self):
        self.items = [
            Algorithm(id=1,name="My first alg", description="dummy 1"), 
            Algorithm(id=2,name="My second alg",description="dummy 2"), 
            Algorithm(id=3,name="My third alg", description="dummy 3")
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