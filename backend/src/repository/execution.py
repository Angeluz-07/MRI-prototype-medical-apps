from src.domain.models import Execution, ExecutionDetail
from src.repository.interfaces import Repository

class InMemoryExecutionRepository(Repository):
    
    def __init__(self):
        exec =  Execution(algorithm_id="29a2ba2b-0db4-41bb-87b0-a5af98462a4e")
        exec.add_log("testing...")
        self.items = [
           exec
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
    
import json
import os
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

class JsonExecutionRepository(Repository):
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not self.file_path.exists():
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def _read_all(self) -> List[dict]:
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def _write_all(self, data: List[dict]):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def get_all(self) -> List[Execution]:
        data = self._read_all()
        return [self._map_to_entity(item) for item in data]

    def get_by_id(self, id: str) -> Optional[Execution]:
        data = self._read_all()
        item = next((x for x in data if x["id"] == id), None)
        return self._map_to_entity(item) if item else None

    def add(self, execution: Execution):
        data = self._read_all()
        # Convert dataclass to dict; datetime handled by custom logic
        execution_dict = asdict(execution)
        # Convert datetime objects to ISO strings for JSON
        for detail in execution_dict['details']:
            if isinstance(detail['timestamp'], datetime):
                detail['timestamp'] = detail['timestamp'].isoformat()
        
        data.append(execution_dict)
        self._write_all(data)

    def _map_to_entity(self, data: dict) -> Execution:
        """Helper to reconstruct the objects from a dictionary."""
        details = [
            ExecutionDetail(
                timestamp=datetime.fromisoformat(d['timestamp']),
                message=d['message'],
                level=d['level'],
                id=d['id']
            ) for d in data['details']
        ]
        return Execution(
            algorithm_id=data['algorithm_id'],
            id=data['id'],
            details=details
        )