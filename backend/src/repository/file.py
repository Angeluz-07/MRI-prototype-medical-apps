from .interface import Repository, Item
from typing import List
from src.domain.models import File
from abc import ABC, abstractmethod

# Repository Interface
class Repository(ABC):
    @abstractmethod
    def get_all(self, id: int) -> File | None:
        pass
    
    @abstractmethod
    def add(self, item: File):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> File | None:
        pass

from pathlib import Path
import shutil
WORKSPACE_DEFAULT_FOLDER = Path(__file__).parent.parent.parent / "workspace" / "default"
RESULTS_FOLDER = Path(__file__).parent / "out"

#by now holds only input files
class FileRepository(Repository):
    
    def __init__(self):
        self.items = []

    def get_all(self):
        return self.items
    
    def add(self, item: File):
        self.items.append(item)

    def get_by_id(self, id):
        for x in self.items:
            if x.id == id:
                return x
        return None
    
    def get_full_path(self, filename):
        return str(WORKSPACE_DEFAULT_FOLDER / filename)
