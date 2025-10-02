from perfomance import Performance

class DesiredPerformance(Performance):
    def __init__(self, subjects, desired_grades):
        super().__init__(subjects, desired_grades)

    def average(self):
        if len(self._grades) == 0:
            return 0
        return sum(self._grades) / len(self._grades)