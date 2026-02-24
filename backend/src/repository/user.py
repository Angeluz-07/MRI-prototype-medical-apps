from src.domain.models import User
from src.repository.interfaces import Repository

class InMemoryUserRepository(Repository):
    
    def __init__(self):
        self.items = [
            User(username="testy", email="test@example.com", password="test", id="29a2ba2b-0db4-41bb-87b0-a5af98462a42"), 
            User(username="loki", email="test2@example.com", password="test2", id="665fff20-adee-4e53-8b61-3c776b3e39a1"),
            User(username="thor", email="test3@example.com", password="test2")
        ]

    def get_all(self):
        return self.items
    
    def add(self, item: User):
        self.items.append(item)

    def get_by_id(self, id: str):
        return next((u for u in self.items if u.id == id), None)

    def get_by_email(self, email: str):
        return next((u for u in self.items if u.email == email), None)
    