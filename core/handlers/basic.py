from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=reply_keyboard)
    

async def button1(message: Message, bot: Bot):
    await message.answer(f'Ленина 1 в Новороссийске: https://yandex.ru/maps/970/novorossiysk/house/prospekt_lenina_1/Z04YcQ9jTkIHQFpufXtxdHlrZA==/?ll=37.830808%2C44.693967&z=12.13')




