import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.main_menu import main_menu_kb, inline_start_kb

router = Router()

WELCOME_TEXT = """
╔══════════════════════════╗
   ⚡ <b>CODEFY APP</b> ga xush kelibsiz!
╚══════════════════════════╝

Salom, <b>{name}</b>! 👋

Men — <b>Abdurahmon</b>, professional Full-Stack dasturchiman. 👨‍💻
Sizning g'oyangizni zamonaviy vebsayt va yuqori tezlikda ishlovchi Telegram bot ko'rinishida sifatli yaratib beraman.

<b>🛠 Qanday xizmatlar ko'rsataman?</b>
├ 🤖 Har qanday murakkablikdagi Telegram botlar
├ 🌐 Zamonaviy, responsive vebsaytlar va WebApplar
├ ⚡ 200 000 so'mdan boshlanadigan tayyor sifatli botlar
└ 🔧 CRM va avtomatlashtirish tizimlari

👇 <b>Menyudan kerakli bo'limni tanlang:</b>
"""


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        WELCOME_TEXT.format(name=message.from_user.full_name),
        reply_markup=main_menu_kb(),
        parse_mode="HTML"
    )
    # Inline menu ham birga ko'rsatiladi
    await message.answer(
        "⚡ <b>Tezkor navigatsiya menyusi:</b>",
        reply_markup=inline_start_kb(),
        parse_mode="HTML"
    )
