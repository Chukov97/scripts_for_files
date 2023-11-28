import shutil
import zipfile
import os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
RESOURCE_DIR = os.path.join(CURRENT_DIR, 'resources')
LIST_FILE = os.listdir(TMP_DIR)
ZIP_FILE_DIR = os.path.join(RESOURCE_DIR, 'test.zip')


def create_zip():
    if not os.path.exists(RESOURCE_DIR):
        os.mkdir(RESOURCE_DIR)
    with zipfile.ZipFile(ZIP_FILE_DIR, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in LIST_FILE:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    shutil.rmtree(RESOURCE_DIR)

create_zip()
