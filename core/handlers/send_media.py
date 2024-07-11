from aiogram.types import Message, FSInputFile
from aiogram import Bot


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(path=r'C:\Users\PC\Desktop\img1.jpg')
    await bot.send_photo(message.chat.id, photo, caption="It is the requested photo img1.jpg")