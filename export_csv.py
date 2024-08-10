import os
import UnityPy
import csv

def work():
    filename = "localization-string-tables-english(en)_assets_all.bundle"
    env = UnityPy.load(filename)
    data = []
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour" and obj.serialized_type.nodes:
            tree = obj.read_typetree()
            name = tree["m_Name"] 
            tabledata = tree.get('m_TableData')
            if isinstance(tabledata, list):
                for entry in tabledata:
                    m_Localized = entry.get('m_Localized')
                    m_Id = entry.get('m_Id')
                    data.append([name, m_Id, m_Localized])

    csv_filename = "exort.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Filename", "m_Id", "m_Localized"])
        writer.writerows(data)

    print(f"추출됨 {csv_filename}")

def main():
    work()

if __name__ == "__main__":
    main()