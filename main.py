from aiogram import F, Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging
from core.filters.date import check_if_data
from core.handlers.basic import *
from core.settings import settings
from aiogram.filters import Command
from core.handlers.pay import *
from core.handlers.send_media import *
from core.handlers.sheets import *

 
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot is started')


async def stop_bot(bot):
    await bot.send_message(settings.bots.admin_id, text='Bot is stopped')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s"
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(button1, F.text=='Кнопка 1')
    dp.message.register(order, F.text=='Кнопка 2')
    dp.message.register(successfull_payment, F.successful_payment)
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(get_photo, F.text=='Кнопка 3')
    dp.message.register(get_A2, F.text=='Кнопка 4')
    dp.message.register(check_if_data)



    try:
        await dp.start_polling(bot)
    finally:
        await dp.session_close()



if __name__ == '__main__':
    asyncio.run(start())
