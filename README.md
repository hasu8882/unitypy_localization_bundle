# unitypy_localization_bundle

For the unity game translator 

1.You can extract m_name, m_id, m_localization(scripts) within localization-string-tables-english(en)_assets_all.bundle using export_csv.py
1. export_csv.py를 사용하여 m_name, m_id, m_localization(대사) 를 localization-string-tables-english(en)_assets_all.bundle에서 추출 할수 있습니다.
   
2.Also you can edit csv using google spreadsheet etc. 
Note that the translation should be on the third line. You should copy the original text on the fourth line for translation reference.
2. csv 파일을 구글스프레드 시트등을 사용하여 편집하세요.
번역 참고를 위해 3열에 있는 m_localized의 내용을 복사하여 4열에 붙여넣을 수 있습니다. 다만 헤드는 편집 하지 말아주세요.

3.Reformat csv using notepad++ etc, otherwise an error will occur.
3. notepad++ 등을 사용 하여 csv를 리포멧 합니다. 하지 않는다면 uabea에서 오류가 발생합니다. 

4.Create a 'dump'(name) folder and extract the dump there
4. dump 라는 이름의 폴더를 만들고 uabea 등을 사용하여 localization-string-tables-english(en)_assets_all.bundle의 대사 monoibehavior 를 추출 하세요.

5.Create an update folder
5. update라는 이름의 폴더를 만드세요.

6.Run import_csv.py.
6. import_csv.py를 실행합니다.

7. Import txt in the update folder using uabea.
7.  update 폴더 안에 있는 txt를 uabea를 사용하여 import 해줍니다. 
