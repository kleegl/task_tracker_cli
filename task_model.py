from enum import Enum


class Task:
    id: int
    description: str
    status: int
    createdAt: str
    updatedAt: str

    def __init__(self, id, description, status, createdAt, updatedAt) -> None:
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt


class Task_Status(Enum):
    TODO = 0
    PROGRESS = 1
    DONE = 2
