import os
from google.oauth2.service_account import Credentials  # type: ignore
from googleapiclient.discovery import build  # type: ignore


def save_to_google_sheets(df, spreadsheet_id, sheet_name="Sheet1"):
    """Simpan DataFrame ke Google Sheets"""
    try:
        # Ambil path root project
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(base_dir, "./google-sheets-api.json")

        creds = Credentials.from_service_account_file(
            json_path,
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )

        service = build("sheets", "v4", credentials=creds)

        values = [df.columns.tolist()] + df.values.tolist()
        body = {"values": values}

        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_name}!A1",
            valueInputOption="RAW",
            body=body
        ).execute()

        print("Data berhasil disimpan ke Google Sheets")

    except Exception as e:
        print(f"Error Google Sheets: {e}")
