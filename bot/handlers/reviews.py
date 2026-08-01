import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router, F
from aiogram.types import Message
from db.queries import get_reviews
from keyboards.main_menu import website_btn_kb, order_btn_kb

router = Router()


@router.message(F.text.in_({"⭐ Izohlar", "💬 Sharhlar", "Sharhlar"}))
async def show_reviews(message: Message):
    reviews = await get_reviews()
    if not reviews:
        await message.answer("😔 Hozircha izohlar mavjud emas.", reply_markup=order_btn_kb())
        return

    header = (
        "💬 <b>MIJOZLAR SHARHLARI & IZOHLARI</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n"
    )

    cards = []
    for r in reviews:
        card = (
            f"{r.get('stars', '⭐')}\n"
            f"👤 <b>{r.get('name', '')}</b>\n"
            f"💼 <i>{r.get('kasb', '')}</i>\n\n"
            f"❝ {r.get('izoh', '')} ❞"
        )
        cards.append(card)

    full_text = header + "\n\n━━━━━━━━━━━━━━━━━━━\n\n".join(cards)
    await message.answer(full_text, reply_markup=order_btn_kb(), parse_mode="HTML")


@router.message(F.text == "🌐 Saytga o'tish")
async def go_to_website(message: Message):
    text = (
        "🌐 <b>CODEFY APP</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n\n"
        "Rasmiy saytimizda barcha loyihalar,\n"
        "narxlar va to'liq ma'lumotlar!\n\n"
        "👇 Tugmani bosib o'ting:"
    )
    await message.answer(text, reply_markup=website_btn_kb(), parse_mode="HTML")
