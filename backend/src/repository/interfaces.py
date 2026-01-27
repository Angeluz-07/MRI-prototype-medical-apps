from abc import ABC, abstractmethod

class Item:
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