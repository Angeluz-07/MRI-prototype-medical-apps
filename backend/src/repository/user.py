from src.domain.models import User
from src.repository.interfaces import Repository

class InMemoryUserRepository(Repository):
    
    def __init__(self):
        self.items = [
            User(username="testy", email="test@example.com", password="test", id="29a2ba2b-0db4-41bb-87b0-a5af98462a42"), 
            User(username="loki", email="test2@example.com", password="test2"),
            User(username="thor", email="test3@example.com", password="test2")
        ]

    def get_all(self):
        return self.items
    
    def add(self, item: User):
        self.items.append(item)

    def get_by_id(self, id):
        for x in self.items:
            if x.id == id:
                return x
        return None