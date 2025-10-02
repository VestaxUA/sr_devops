import json
from sr2.save_data import SaveData

class SaveJSON(SaveData):
    def save(self, data: dict, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)