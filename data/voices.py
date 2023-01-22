from aiogram import types
from loader import db


ovozlar = db.select_voices()
voices = []
for ovoz in ovozlar:
    voices.append(
        types.InlineQueryResultCachedVoice(
            id=f"{ovoz[0]}",
            voice_file_id=f"{ovoz[2]}",
            title=f"{ovoz[1]}"
        )
    )

