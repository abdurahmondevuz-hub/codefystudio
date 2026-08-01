import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from db.queries import get_categories
from keyboards.project_kb import categories_kb

router = Router()


@router.message(F.text == "📂 Loyihalar")
async def show_categories(message: Message):
    categories = await get_categories()
    if not categories:
        await message.answer("😔 Hozircha kategoriyalar mavjud emas.")
        return
    await message.answer(
        "📂 <b>Kategoriyalardan birini tanlang:</b>",
        reply_markup=categories_kb(categories),
        parse_mode="HTML"
    )


@router.callback_query(F.data == "back_cats")
async def back_to_categories(callback: CallbackQuery):
    categories = await get_categories()
    if not categories:
        await callback.message.edit_text("😔 Hozircha kategoriyalar mavjud emas.")
        return
    await callback.message.edit_text(
        "📂 <b>Kategoriyalardan birini tanlang:</b>",
        reply_markup=categories_kb(categories),
        parse_mode="HTML"
    )
    await callback.answer()
