from aiogram.types import Message
from aiogram import Bot
from gspread import Cell, Client, Spreadsheet, Worksheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials


SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1e0_kBIu2YdZL1sCdlvluM7LMqYS5p4NgkyWZ91vMz38/edit?gid=0#gid=0'


async def get_A2(message: Message, bot: Bot):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("./service.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open('Bot').sheet1
    value = sheet.acell('A2').value
    await bot.send_message(message.chat.id, value)
    