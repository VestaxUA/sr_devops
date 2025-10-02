from sr2.desired_perfomance import DesiredPerformance
from sr2.perfomance import Performance

class StudentData:
    def __init__(self, student, real_perf: Performance, desired_perf: DesiredPerformance):
        self.student = student
        self.real_perf = real_perf
        self.desired_perf = desired_perf

    def to_dict(self):
        return {
            "Student": {
                "PIB": self.student.get_pib(),
                "Group": self.student.get_group(),
                "BirthDate": self.student.get_birth_date(),
                "Address": self.student.get_address()
            },
            "RealPerformance": {
                "Subjects": self.real_perf._subjects,
                "Grades": self.real_perf._grades,
                "Average": self.real_perf.average()
            },
            "DesiredPerformance": {
                "Subjects": self.desired_perf._subjects,
                "DesiredGrades": self.desired_perf._grades,
                "DesiredAverage": self.desired_perf.average()
            }
        }