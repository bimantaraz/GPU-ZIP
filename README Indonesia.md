# GPU-ZIP: Kompresi Folder Super Cepat dengan GPU

GPU-ZIP adalah script Python yang memanfaatkan power GPU untuk mempercepat kompresi folder menjadi file ZIP. Dengan menggunakan library Cupy, script ini membaca dan menulis data file dengan kecepatan yang jauh lebih tinggi daripada metode tradisional.

## Requirements
- CuPy
- zipfile36
- tqdm

## Instalasi

1. Clone the repository:

    ```bash
    git clone https://github.com/bimantaraz/GPU-ZIP.git
    cd GPU-ZIP
    ```

2. Instal paket yang diperlukan:

    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan

Untuk mengompres folder menggunakan GPU, jalankan perintah berikut:

```bash
python main.py /path/to/your/folder /path/to/output.zip
```
