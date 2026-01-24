from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import UUID, uuid4

@dataclass
class Algorithm:
    id: int 
    name: str
    description: str


@dataclass
class Execution:
    id: int 
    message: str
    timestamp: datetime

@dataclass
class File:
    path: str