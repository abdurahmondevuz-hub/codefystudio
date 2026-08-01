from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import SITE_URL


def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📂 Loyihalar"), KeyboardButton(text="⭐ Izohlar")],
            [KeyboardButton(text="🌐 Saytga o'tish")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Menyudan tanlang...",
    )


def website_btn_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="🌐 codefy.uz — rasmiy sayt", url=SITE_URL)
        ]]
    )
