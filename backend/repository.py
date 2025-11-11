
from dataclasses import dataclass
from typing import List
from pydantic import BaseModel


class Task(BaseModel):
    id : int
    name: str
    status: bool
    
    
class TasksRepository:
    tasks: List[str]
    
    def __init__(self):
        self.tasks = [
            Task(id=1,name="My first task", status=False), 
            Task(id=2,name="My second task",status=False), 
            Task(id=3,name="My third task", status=False)
        ]

    def get_all(self):
        return self.tasks
    
    def save(self, task: Task):
        self.tasks.append(task)

    def get_by_id(self, id):
        for x in self.tasks:
            if x.id == id:
                return x
        return None