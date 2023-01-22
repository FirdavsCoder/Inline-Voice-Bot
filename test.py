# from loader import db

# print(db.search(query="%N%"))

# import telebot

# bot = telebot.TeleBot("5902270251:AAE35OE2hi-uwdlG5p-ydXjSo_qrZgD0UHI")

# @bot.message_handler(text='salom')
# def start(message):
#     bot.send_message(message.chat.id,"Salom")

# bot.polling()


from aiogram import types, Bot, Dispatcher, executor

bot = Bot(token = "5902270251:AAE35OE2hi-uwdlG5p-ydXjSo_qrZgD0UHI")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)