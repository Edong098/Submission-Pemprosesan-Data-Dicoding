from sqlalchemy import create_engine  # type: ignore

def save_to_postgresql(df, db_url, table_name="products"):
    """
    Simpan DataFrame ke PostgreSQL
    """
    try:
        engine = create_engine(db_url)

        with engine.connect() as conn:
            df.to_sql(
                table_name,
                con=conn,
                if_exists="append",
                index=False
            )

        print("Data berhasil disimpan ke PostgreSQL")

    except Exception as e:
        print(f"Error PostgreSQL: {e}")