from aiogram.types import Message, FSInputFile
from aiogram import Bot

# Функция, возвращающая фото по адресу
async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(path=r'')
    await bot.send_photo(message.chat.id, photo, caption="It is the requested photo img1.jpg")