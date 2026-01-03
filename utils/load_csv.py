import pandas as pd  # type: ignore

def save_to_csv(df, filename="products.csv"):
    """Menyimpan DataFrame ke file CSV"""
    try:
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Error simpan CSV: {e}")