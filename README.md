# GPU-ZIP: Super Fast Folder Compression with GPU

GPU-ZIP is a Python script that utilizes GPU power to speed up compression of folders into ZIP files. Using the Cupy library, this script reads and writes file data at a much higher speed than traditional methods.

## Requirements
- CuPy
- zipfile36
- tqdm

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bimantaraz/GPU-ZIP.git
    cd GPU-ZIP
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To compress a folder using GPU, run the following command:

```bash
python main.py
```
