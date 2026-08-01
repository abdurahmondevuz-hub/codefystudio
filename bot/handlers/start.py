import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.main_menu import main_menu_kb

router = Router()

WELCOME_TEXT = """
╔══════════════════════════╗
   ⚡ <b>CODEFY APP</b> ga xush kelibsiz!
╚══════════════════════════╝

Salom, <b>{name}</b>! 👋

Biz — <b>professional dasturchilar jamoasi</b>.
Sizning g'oyangizni haqiqiy mahsulotga aylantiramiz.

<b>🛠 Nima qilamiz?</b>
├ 🤖 Telegram botlar
├ 🌐 Web saytlar
├ 📱 Mobile ilovalar
└ 🔧 Avtomatlashtirish

👇 <b>Menyudan tanlang:</b>
"""


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        WELCOME_TEXT.format(name=message.from_user.full_name),
        reply_markup=main_menu_kb(),
        parse_mode="HTML"
    )
