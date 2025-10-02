from abc import ABC, abstractmethod

class Performance(ABC):
    def __init__(self, subjects, grades):
        self._subjects = subjects
        self._grades = grades

    @abstractmethod
    def average(self):
        pass