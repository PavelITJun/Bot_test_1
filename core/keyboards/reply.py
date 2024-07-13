from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

# Создаём reply-кнопки
reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Кнопка 1'
        ),
        KeyboardButton(
            text='Кнопка 2'
        )
    ],
    [
        KeyboardButton(
            text='Кнопка 3'
        ),
        KeyboardButton(
            text='Кнопка 4'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose a button', selective=True)