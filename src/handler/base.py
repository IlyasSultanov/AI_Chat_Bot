from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

router = Router()


@router.message(Command("start", "help"))
async def start_command(message: Message):
    help_text = (
        "🤖 <b>ChatGPT Bot</b>\n\n"
        "Просто напишите мне сообщение, и я отвечу с помощью AI!\n\n"
        "Команды:\n"
        "/start - Начальное сообщение\n"
        "/help - Помощь\n"
        "/clear - Очистить контекст"
    )
    await message.answer(help_text, parse_mode=ParseMode.HTML)
