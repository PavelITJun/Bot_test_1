import datetime
from aiogram.types import Message
from aiogram import Bot
from core.dao.gspread import *

# проверяем введённую дату. Если валидная - добавляем в таблицу
async def check_if_data(message: Message, bot: Bot):
    try:
        date_format = "%d.%m.%y"
        datetime.datetime.strptime(message.text, date_format)
        await bot.send_message(message.chat.id, 'Дата верна')
        sheet = get_sheet().open('Bot').sheet1
        col_values = sheet.col_values(2)
        first_empty_row = len(col_values) + 1
        sheet.update_cell(first_empty_row, 2, message.text)

    except ValueError:
        print(message.text)
        await bot.send_message(message.chat.id, 'Неверный формат даты')
