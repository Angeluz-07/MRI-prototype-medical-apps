from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import UUID, uuid4
from enum import Enum
from datetime import timezone

@dataclass
class File:
    path: str

@dataclass
class Algorithm:
    name: str
    description: str
    id: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class ExecutionDetail:
    """Value Object or Entity representing a trace event."""
    timestamp: datetime
    message: str
    level: str  # INFO, ERROR, etc.
    id: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Execution:
    algorithm_id: str
    id: str = field(default_factory=lambda: str(uuid4()))
    details:List[ExecutionDetail] = field(default_factory=list)

    def add_log(self, message, level ="INFO"):
        detail = ExecutionDetail(datetime.now(timezone.utc), message, level)
        self.details.append(detail)

