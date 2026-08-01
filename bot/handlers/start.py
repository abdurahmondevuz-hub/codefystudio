import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.main_menu import main_menu_kb

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    name = message.from_user.full_name
    text = (
        f"👋 Salom, <b>{name}</b>!\n\n"
        f"🚀 <b>CodefyStudio</b> botiga xush kelibsiz!\n\n"
        f"Bu yerda siz bizning barcha loyihalarimiz bilan tanishishingiz, "
        f"mijozlar izohlarini o'qishingiz va rasmiy saytimizga o'tishingiz mumkin.\n\n"
        f"👇 Quyidagi menyudan tanlang:"
    )
    await message.answer(text, reply_markup=main_menu_kb(), parse_mode="HTML")
