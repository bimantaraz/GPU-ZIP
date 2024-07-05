import os
import zipfile
import cupy as cp
from tqdm import tqdm

def zip_folder_gpu(folder_path, output_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in tqdm(file_list, desc="Compressing", unit="files"):
            with open(file_path, 'rb') as f:
                file_data = cp.array(bytearray(f.read()))
            zipf.writestr(os.path.relpath(file_path, folder_path), cp.asnumpy(file_data))

folder_path = 'folder_name' 
output_path = 'output.zip' 
zip_folder_gpu(folder_path, output_path)
