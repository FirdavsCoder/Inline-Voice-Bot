from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
from data.config import ADMINS
from keyboards.inline.buttons import start_button


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if db.check_user(user_id=message.from_user.id):
        text = f"<b>Assalomu alaykum {message.from_user.full_name}</b>\nAgar botimizdan foydalana olmasangiz /help " \
               f"komandasini yuboring!\n\n<i>Botimizdan to'liq foydalanish uchun kanalimizga ham obuna bo'ling.</i>"
        await message.answer("<b>https://t.me/Firdavs_Yorkulov</b>\n\n🧑‍💻 <i>Admin: @Firdavs_Programmer</i>")
        await message.answer(f"{text}", reply_markup=start_button)
    else:
        db.add_user(user_id=message.from_user.id, user_fullname=message.from_user.full_name,
                    username=message.from_user.username)
        text = f"<b>Assalomu alaykum {message.from_user.full_name}</b>\nAgar botimizdan foydalana olmasangiz /help " \
               f"komandasini yuboring!\n\n<i>Botimizdan to'liq foydalanish uchun kanalimizga ham obuna bo'ling.</i>"
        await message.answer("<b>https://t.me/Firdavs_Yorkulov</b>\n\n🧑‍💻 <i>Admin: @Firdavs_Programmer</i>")
        await message.answer(f"{text}", reply_markup=start_button)
        await bot.send_message(chat_id=ADMINS[0],
                               text=f"👤 Yangi foydalanuvch: {message.from_user.get_mention()},\n📊 Bazada " \
                                    f"{db.count_users()[0]} ta foydalanuvchi bor!")
