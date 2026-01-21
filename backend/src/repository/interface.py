
from dataclasses import dataclass
from typing import List
from pydantic import BaseModel

from abc import ABC, abstractmethod

class Item(BaseModel):
    pass

# Repository Interface
class Repository(ABC):
    @abstractmethod
    def get_all(self, id: int) -> Item | None:
        pass
    
    @abstractmethod
    def add(self, item: Item):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Item | None:
        pass