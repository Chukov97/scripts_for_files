import shutil

from config import RESOURCE_DIR, ZIP_FILE_DIR, TMP_DIR, LIST_FILE, TEMPORARY_PDF
import zipfile
import pytest
import os


@pytest.fixture
def create_zip():
    if not os.path.exists(RESOURCE_DIR):
        os.mkdir(RESOURCE_DIR)
    with zipfile.ZipFile(ZIP_FILE_DIR, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in LIST_FILE:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))
    yield
    shutil.rmtree(RESOURCE_DIR)


@pytest.fixture
def rm_pdf():
    yield
    os.remove(TEMPORARY_PDF)
