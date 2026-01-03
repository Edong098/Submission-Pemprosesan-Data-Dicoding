# Cara Menjalankan Skrip ETL Pipeline

Jalankan perintah berikut pada terminal di direktori project:

python main.py

# Cara Menjalankan Unit Test

Untuk menjalankan seluruh unit test pada folder tests, gunakan perintah berikut:

python -m pytest

# Cara Menjalankan Test Coverage

Untuk melihat cakupan pengujian (test coverage), jalankan perintah berikut:

coverage run -m pytest
coverage report

# Konfigurasi dan Penyimpanan ke PostgreSQL

Pastikan PostgreSQL sudah berjalan dan database telah dibuat.
Contoh URL koneksi database:

postgresql+psycopg2://developer:qwerty@localhost:5432/productsdb

Penyimpanan ke PostgreSQL dilakukan dengan memanggil fungsi:
save_to_postgres(df, db_url)

Fungsi ini menggunakan SQLAlchemy untuk menyimpan data hasil transformasi
ke dalam tabel PostgreSQL secara otomatis.

# URL Google Sheets

https://docs.google.com/spreadsheets/d/15wpKWMwAUKTjqZe3i6thrZ8fbpnc20GGSU_wWO8tkwA
