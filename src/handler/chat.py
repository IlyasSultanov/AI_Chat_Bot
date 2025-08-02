from aiogram import Router, F
from aiogram.types import Message
from aiogram.enums import ParseMode

from service.open_api import open_api_service

router = Router()


@router.message(F.text & ~F.text.startswith('/'))
async def handle_message(message: Message):
    try:
        await message.bot.send_message(message.chat.id, "")
        response = await open_api_service.complete_prompt(message.text)
        await message.answer(response[:4000], parse_mode=ParseMode.HTML)
    except Exception as e:
        await message.answer("⚠️ Произошла ошибка", e)
