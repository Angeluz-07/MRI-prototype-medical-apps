from abc import ABC, abstractmethod
from typing import List

class Item:
    pass

# Repository Interface
class Repository(ABC):
    @abstractmethod
    def get_all(self, id: str) -> List[Item]:
        pass
    
    @abstractmethod
    def add(self, item: Item):
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Item | None:
        pass