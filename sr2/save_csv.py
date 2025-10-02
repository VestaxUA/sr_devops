import csv
from sr2.save_data import SaveData

class SaveCSV(SaveData):
    def save(self, data: dict, filename: str):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Section", "Field", "Value"])

            for key, value in data["Student"].items():
                writer.writerow(["Student", key, value])

            for i, subj in enumerate(data["RealPerformance"]["Subjects"]):
                writer.writerow(["RealPerformance", subj, data["RealPerformance"]["Grades"][i]])
            writer.writerow(["RealPerformance", "Average", data["RealPerformance"]["Average"]])

            for i, subj in enumerate(data["DesiredPerformance"]["Subjects"]):
                writer.writerow(["DesiredPerformance", subj, data["DesiredPerformance"]["DesiredGrades"][i]])
            writer.writerow(["DesiredPerformance", "DesiredAverage", data["DesiredPerformance"]["DesiredAverage"]])
