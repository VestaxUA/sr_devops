from sr2.save_data import SaveData
import xml.etree.ElementTree as ET

class SaveXML(SaveData):
    def save(self, data: dict, filename: str):
        root = ET.Element("StudentData")

        student_elem = ET.SubElement(root, "Student")
        for key, value in data["Student"].items():
            ET.SubElement(student_elem, key).text = str(value)

        real_elem = ET.SubElement(root, "RealPerformance")
        for key, value in data["RealPerformance"].items():
            if isinstance(value, list):
                sub_elem = ET.SubElement(real_elem, key)
                for v in value:
                    ET.SubElement(sub_elem, "Item").text = str(v)
            else:
                ET.SubElement(real_elem, key).text = str(value)

        desired_elem = ET.SubElement(root, "DesiredPerformance")
        for key, value in data["DesiredPerformance"].items():
            if isinstance(value, list):
                sub_elem = ET.SubElement(desired_elem, key)
                for v in value:
                    ET.SubElement(sub_elem, "Item").text = str(v)
            else:
                ET.SubElement(desired_elem, key).text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)