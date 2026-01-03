from utils.extract import scrape_main
from utils.transform import transform_to_dataframe, transform_data
from utils.load_csv import save_to_csv
from utils.load_gsheets import save_to_google_sheets
from utils.load_postgres import save_to_postgresql


def main():
    # DI REVISI
    BASE_URL = "https://fashion-studio.dicoding.dev/"

    # EXTRACT
    data = scrape_main(BASE_URL)

    if not data:
        print("Tidak ada data yang ditemukan")
        return

    print(f"TOTAL DATA HASIL EXTRACT: {len(data)}")

    # TRANSFORM
    df = transform_to_dataframe(data)
    df = transform_data(df, 16000)

    # VALIDASI HASIL
    print("\nJUMLAH DATA AKHIR SETELAH TRANSFORM:", df.shape)

    print("\nDATA TERATAS")
    print(df.head(10))

    print("\nINFO DATA")
    print(df.info())

    # LOAD
    # CSV
    save_to_csv(df)

    # Google Sheets
    save_to_google_sheets(
        df,
        spreadsheet_id="15wpKWMwAUKTjqZe3i6thrZ8fbpnc20GGSU_wWO8tkwA"
    )

    # PostgreSQL
    save_to_postgresql(
        df,
        db_url="postgresql+psycopg2://developer:qwerty@localhost:5432/productsdb",
        table_name="products"
    )

if __name__ == "__main__":
    main()