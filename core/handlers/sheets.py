from aiogram.types import Message
from aiogram import Bot
from core.dao.gspread import get_sheet


SPREADSHEET_URL = ''

# Получаем значение ячейки A2
async def get_A2(message: Message, bot: Bot):
    sheet = get_sheet().open('Bot').sheet1
    value = sheet.acell('A2').value
    await bot.send_message(message.chat.id, value)
    