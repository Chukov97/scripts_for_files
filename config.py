import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
RESOURCE_DIR = os.path.join(CURRENT_DIR, 'resources')
LIST_FILE = os.listdir(TMP_DIR)
ZIP_FILE_DIR = os.path.join(RESOURCE_DIR, 'test.zip')
TEMPORARY_PDF = os.path.join(CURRENT_DIR, 'tmp.pdf')
TEMPORARY_CSV = os.path.join(CURRENT_DIR, 'tmp.csv')
TEMPORARY_XLSX = os.path.join(CURRENT_DIR, 'tmp.xlsx')
