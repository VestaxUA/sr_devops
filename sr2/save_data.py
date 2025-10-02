from abc import ABC, abstractmethod

class SaveData(ABC):
    @abstractmethod
    def save(self, data: dict, filename: str):
        pass