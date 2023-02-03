import zipfile
from pathlib import Path


def unzip(ruta_zip):
    with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
        zip_ref.extractall(Path.cwd())
