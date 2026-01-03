import pandas as pd  # type: ignore
import re


def transform_to_dataframe(data):
    try:
        if not data:
            return pd.DataFrame()
        return pd.DataFrame(data)
    except Exception as e:
        print(f"Error DataFrame: {e}")
        return pd.DataFrame()


def transform_data(df, exchange_rate):
    try:
        # BASIC CLEANING
        df = df.dropna()
        df = df.drop_duplicates()

        # TITLE
        df["Title"] = df["Title"].astype(str).str.strip()
        df = df[df["Title"] != "Unknown Product"]

        # PRICE → RUPIAH
        df["Price"] = (
            df["Price"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
        )

        df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
        df = df[df["Price"].notna()]
        df["Price"] = df["Price"] * exchange_rate

        # RATING → FLOAT
        def clean_rating(x):
            x = str(x)
            match = re.search(r"\d+(\.\d+)?", x)
            return float(match.group()) if match else None

        df["Rating"] = df["Rating"].apply(clean_rating)
        df = df[df["Rating"].notna()]
        df["Rating"] = df["Rating"].apply(lambda x: float(x) if str(x).replace(".", "", 1).isdigit() else 0.0)


        # COLORS → INT
        df["Colors"] = (
            df["Colors"]
            .astype(str)
            .str.extract(r"(\d+)")
            .astype(int)
        )

        # SIZE & GENDER → STRING
        df["Size"] = df["Size"].astype(str).str.strip()
        df["Gender"] = df["Gender"].astype(str).str.strip()

        # TIMESTAMP → STRING
        df["Timestamp"] = df["Timestamp"].astype(str)

        # FINAL
        df = df.drop_duplicates(
            subset=["Title", "Price", "Rating", "Colors", "Size", "Gender"]
        )

        return df.reset_index(drop=True)

    except Exception as e:
        print(f"Error transform data: {e}")
        return df