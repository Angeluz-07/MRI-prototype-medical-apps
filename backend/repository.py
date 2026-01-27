
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

from pathlib import Path
import shutil
WORKSPACE_DEFAULT_FOLDER = Path(__file__).parent / "workspace" / "default"
RESULTS_FOLDER = Path(__file__).parent / "out"

class File(Item):
    path: str

import base64
def get_base64_str_from_path(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()                
    # 2. Encode the binary content to Base64
    encoded_content = base64.b64encode(file_content)                
    # 3. Decode the Base64 bytes to a string for JSON serialization
    base64_string = encoded_content.decode('utf-8')     
    return base64_string

class FileRepository(Repository):
    def get_all(self):
        folder_path = Path(WORKSPACE_DEFAULT_FOLDER)   
        result =  [file_path.name for file_path in folder_path.iterdir() if file_path.is_file()]
        return result

    def add(self, file: File):
        pass
    
    def add_raw(self, file):
        path = WORKSPACE_DEFAULT_FOLDER / f"{file.filename}"
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file.filename

    def service_segment_brain(self, filename):
        import img_process
        path = WORKSPACE_DEFAULT_FOLDER / filename
        img_process.run(str(path))
    
    def get_str_by_id(self, id):
        path = Path(WORKSPACE_DEFAULT_FOLDER) / id
        s = get_base64_str_from_path(path)
        return s
    def get_by_id(self, id):
        pass


class FileRepositoryResults(Repository):
    def get_all(self):
        folder_path = Path(RESULTS_FOLDER)   
        result =  [file_path.name for file_path in folder_path.iterdir() if file_path.is_file()]
        return result

    def add(self, file: File):
        pass
        
    def get_str_by_id(self, id):
        path = Path(RESULTS_FOLDER) / id
        s = get_base64_str_from_path(path)
        return s

    def get_by_id(self, id):
        pass
