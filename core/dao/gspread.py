import gspread
from oauth2client.service_account import ServiceAccountCredentials


async def get_sheet():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("", scope)
    client = gspread.authorize(creds)
    return client