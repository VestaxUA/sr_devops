from sr2.desired_perfomance import DesiredPerformance
from sr2.perfomance import Performance
from sr2.save_csv import SaveCSV
from sr2.save_json import SaveJSON
from sr2.save_xml import SaveXML
from sr2.student import Student
from sr2.student_data import StudentData

class RealPerformance(Performance):
    def average(self):
        return sum(self._grades) / len(self._grades) if self._grades else 0

if __name__ == "__main__":
    st = Student("Іваненко Іван Іванович", "КН-21", "2003-05-12", "Київ")

    real_perf = RealPerformance(["Математика", "Програмування C++", "Філософія"], [90, 80, 85])

    desired_perf = DesiredPerformance(["Математика", "Програмування C++", "Філософія"], [100, 95, 100])

    student_data = StudentData(st, real_perf, desired_perf).to_dict()

    filename_base = "IvanenkoIvanIvanovich_KN21_Lab1"

    SaveJSON().save(student_data, filename_base + ".json")
    SaveCSV().save(student_data, filename_base + ".csv")
    SaveXML().save(student_data, filename_base + ".xml")

    print("Дані збережено!")