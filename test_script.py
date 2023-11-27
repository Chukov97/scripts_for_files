from zipfile import ZipFile
from pypdf import PdfReader
import os

zip_folder = 'resources'
zip_file_dir = os.path.join(zip_folder, 'test.zip')


def test_pdf(rm_pdf):
    with ZipFile(zip_file_dir, 'r') as zf:
        content = zf.read('sample.pdf')
        with open('tmp.pdf',
                  'wb') as tmp_file:  # извлечение содержимого pdf-файла во временный файл, который удаляется через фикстуру
            tmp_file.write(content)
        reader = PdfReader('tmp.pdf')
        page = reader.pages[0]
        text = page.extract_text()
        assert 'just for use in the Virtual Mechanics tutorials' in text
