import os
import pandas as pd
import re

csv_file_path = 'export.csv'

dump_directory = './dump'
update_directory = './update'

if not os.path.exists(update_directory):
    os.makedirs(update_directory)

txt_files = [
    (os.path.join(dump_directory, file_name), file_name)
    for file_name in os.listdir(dump_directory)
    if file_name.endswith('.txt')
]

csv_data = pd.read_csv(csv_file_path)
csv_dict = csv_data.set_index('m_Id')['m_Localized'].to_dict()

def replace_localized_text(match):
    m_id = int(match.group(2))
    localized_text = csv_dict.get(m_id, match.group(3))
    return f'{match.group(1)}{localized_text}{match.group(4)}'

for txt_file_path, file_name in txt_files:
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        txt_data = file.read()

    updated_txt_data = re.sub(
        r'(0 SInt64 m_Id = (\d+)\s+1 string m_Localized = ")(.*?)(")',
        replace_localized_text,
        txt_data
    )

    updated_txt_file_path = os.path.join(update_directory, file_name)
    with open(updated_txt_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_txt_data)

    print(f"Updated TXT file saved to: {updated_txt_file_path}")