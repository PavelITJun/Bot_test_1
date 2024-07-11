from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Payment by tg bot',
        description='2 rub',
        payload='Payment with a bot',
        provider_token='381764678:TEST:89689',
        currency='rub',
        prices=[
            LabeledPrice(
                label='200 rub',
                amount=20000
            )
        ],
        request_timeout=30
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successfull_payment(message: Message):
    msg = f'Thanks for payment {message.successful_payment.total_amount // 100} {message.successful_payment.currency}'
    await message.answer(msg)
