import os
import zipfile
import cupy as cp
from tqdm import tqdm

def zip_folder_gpu(folder_path, output_path):
    # Mendapatkan daftar semua file dalam folder
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))

    # Membuat file ZIP
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Melakukan traversal pada file dengan progress bar
        for file_path in tqdm(file_list, desc="Compressing", unit="files"):
            # Membaca file sebagai array cuPy
            with open(file_path, 'rb') as f:
                file_data = cp.array(bytearray(f.read()))
            # Menulis file ke dalam ZIP
            zipf.writestr(os.path.relpath(file_path, folder_path), cp.asnumpy(file_data))

# Contoh penggunaan
folder_path = 'film'  # Ganti dengan path folder Anda
output_path = 'film.zip'   # Ganti dengan path output zip yang diinginkan
zip_folder_gpu(folder_path, output_path)
