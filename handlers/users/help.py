from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from keyboards.inline.buttons import help_button


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "<i><b>Botimizni ishlatish uchun pastdagi tugmani bosib biron bir chatni tanlang va ishlatishni boshlang.👇 \n\n¯\_(ツ)_/¯</b></i>"
    
    await message.answer(f"{text}", reply_markup=help_button)
