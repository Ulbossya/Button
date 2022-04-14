

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Almaty"),
            KeyboardButton(text="Semei"),

        ],
        [
            KeyboardButton(text="Nur-Sultan"),
            KeyboardButton(text="Shymkent"),

        ],
        [
            KeyboardButton(text="Oral"),
            KeyboardButton(text="Turkistan"),
            KeyboardButton(text="Karagandy"),

        ],
    ],
    resize_keyboard=True
)

