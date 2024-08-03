# This should ba an abstract class, there should be a few types of tasks: a timed task, shopping list and more that will inherit from Task.

from datetime import datetime

class Task:
    def __init__(self, title: str, description: str = "", due_date: datetime = datetime.now) -> None:
        self.title = title
        self.description = description
        self.due_date = due_date
        self.created = datetime.now