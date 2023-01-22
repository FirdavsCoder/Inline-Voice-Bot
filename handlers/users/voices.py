from aiogram import types
from loader import db, bot, dp
from data.config import ADMINS
from states.AddVoice import AddVoiceState
from aiogram.dispatcher import FSMContext


@dp.message_handler(content_types=types.ContentTypes.VOICE, chat_id=ADMINS[0])
async def add_audio(message: types.Message, state: FSMContext):
    await AddVoiceState.audio.set()
    voice_id = message.voice.file_id
    await state.update_data({
        "audio": voice_id
    })
    await message.answer("Ovozning nomini kiriting!\n\nE'tiborli bo'ling siz kiritgan nom bilan ovoz izlanadi!")
    await AddVoiceState.next()


@dp.message_handler(state=AddVoiceState.name)
async def get_voice_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    db.add_audio(
        song_name=message.text,
        song_file=f"{data['audio']}"
    )
    await message.answer("Muvaffaqiyatli qo'shildi!")
    await state.finish()


@dp.inline_handler()
async def emty_query(query: types.InlineQuery):
    print("Working...")
    voices = []
    try:
        if query.query == '':
            for ovoz in db.select_voices():
                voices.append(
                    types.InlineQueryResultCachedVoice(
                        id=f"{ovoz[0]}",
                        voice_file_id=f"{ovoz[2]}",
                        title=f"{ovoz[1]}"
                    )
                )
            await query.answer(results=voices, cache_time=1)
        else:
            for ovoz in db.search(query=f"%{query.query}%"):
                voices.append(
                    types.InlineQueryResultCachedVoice(
                        id=f"{ovoz[0]}",
                        voice_file_id=f"{ovoz[2]}",
                        title=f"{ovoz[1]}"
                    )
                )
            await query.answer(voices)
    except Exception as err:
        await bot.send_message(chat_id=query.from_user.id, text=f"Xatolik ketdi: {err}")
