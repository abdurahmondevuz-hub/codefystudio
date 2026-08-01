import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router, F
from aiogram.types import Message
from db.queries import get_reviews
from keyboards.main_menu import website_btn_kb

router = Router()


@router.message(F.text == "⭐ Izohlar")
async def show_reviews(message: Message):
    reviews = await get_reviews()
    if not reviews:
        await message.answer("😔 Hozircha izohlar mavjud emas.")
        return

    parts = ["⭐ <b>Mijozlar izohlari</b>\n"]
    for r in reviews:
        parts.append(
            f"{r.get('stars', '')}\n"
            f"👤 <b>{r.get('name', '')}</b> — <i>{r.get('kasb', '')}</i>\n"
            f"💬 {r.get('izoh', '')}"
        )
    await message.answer("\n\n➖➖➖➖➖\n\n".join(parts), parse_mode="HTML")


@router.message(F.text == "🌐 Saytga o'tish")
async def go_to_website(message: Message):
    await message.answer(
        "🌐 <b>codefy.uz</b> — rasmiy saytimiz.\n\nBarcha loyihalar, narxlar va biz haqimda to'liq ma'lumot!",
        reply_markup=website_btn_kb(),
        parse_mode="HTML"
    )
