import zipfile
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
relative_folder_location='AIS'
# relative_folder_location='ICOADS'
# relative_folder_location='OISST'
path = os.path.join(base_dir, relative_folder_location)


for file in os.listdir(path):
    if file.endswith(".zip"):
        print(os.path.join(path, file))
        zip_ref = zipfile.ZipFile(os.path.join(path, file), 'r')
        zip_ref.extractall(path)
zip_ref.close()