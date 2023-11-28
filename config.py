import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
RESOURCE_DIR = os.path.join(CURRENT_DIR, 'resources')
LIST_FILE = os.listdir(TMP_DIR)
ZIP_FILE_DIR = os.path.join(RESOURCE_DIR, 'test.zip')
