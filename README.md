# Digital Forensics Tool for Recovering Deleted WhatsApp Messages

## Introduction

Proyek ini adalah alat forensik digital yang dirancang untuk memulihkan pesan yang dihapus dari file backup WhatsApp. Alat ini mengekstrak dan menganalisis data dari file backup dan menghasilkan laporan forensik yang komprehensif.

## Features

- Memulihkan pesan yang dihapus dari backup WhatsApp
- Mengekstrak file media yang terkait dengan pesan
- Menganalisis metadata untuk informasi terperinci
- Menghasilkan laporan forensik dalam format PDF
- Antarmuka pengguna yang ramah untuk penggunaan yang mudah

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/imhunterand/whatsapp-forensic-tool.git
    cd whatsapp-forensic-tool
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Jalankan aplikasi:
    ```bash
    python main.py
    ```

2. Gunakan GUI untuk memuat file backup WhatsApp dan memulai analisis.

## Struktur Proyek

- `main.py`: Titik masuk untuk aplikasi.
- `db_extractor.py`: Modul untuk mengekstrak pesan yang dihapus dari database.
- `report_generator.py`: Modul untuk menghasilkan laporan forensik PDF.
- `gui.py`: Modul untuk antarmuka pengguna grafis.
- `requirements.txt`: Daftar dependensi.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
