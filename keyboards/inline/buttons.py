from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔗 Kanalga o'tish!", url="https://t.me/Firdavs_yorkulov")
        ]
    ]
)

help_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔥 Foydalanish", switch_inline_query="")
        ]
    ]
)
