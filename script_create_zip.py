import zipfile
import os

path = 'tmp'
zip_folder = 'resources'
file_dir = os.listdir(path)
zip_file_dir = os.path.join(zip_folder, 'test.zip')


def create_zip():
    with zipfile.ZipFile(zip_file_dir, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file, os.path.basename(add_file))
