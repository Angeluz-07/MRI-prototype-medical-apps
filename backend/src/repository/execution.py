from .interface import Repository, Item
from typing import List
from src.domain.models import Execution
from abc import ABC, abstractmethod

# Repository Interface
class Repository(ABC):
    @abstractmethod
    def get_all(self, id: int) -> Execution | None:
        pass
    
    @abstractmethod
    def add(self, item: Execution):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Execution | None:
        pass

from datetime import datetime, timezone
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