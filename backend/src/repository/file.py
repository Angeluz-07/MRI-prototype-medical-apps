from typing import List
from src.domain.models import File
from src.repository.interfaces import Repository
import shutil
from src.config import WORKSPACE_DEFAULT_FOLDER
from pathlib import Path

#by now holds only input files
class FileRepository(Repository):
    folder_path : str
    files : List[File]

    def __init__(self, folder_path = str(WORKSPACE_DEFAULT_FOLDER)):
        self.folder_path = Path(folder_path)
        files =  [File(file_path.name) for file_path in self.folder_path.iterdir() if file_path.is_file()]
        self.items = files

    def get_all(self):
        return self.items
    
    def add(self, item: File):
        self.items.append(item)

    def get_by_id(self, id):
        for x in self.items:
            if x.name == id:
                return x
        return None

    def get_full_path(self, filename):
        return str(self.folder_path / filename)
 
    def add_raw(self, filename, file):
        path = self.folder_path / f"{filename}"
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file, buffer)

        self.add(File(filename))

        return filename