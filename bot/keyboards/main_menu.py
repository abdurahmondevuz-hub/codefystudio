from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton
)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import SITE_URL


def main_menu_kb() -> ReplyKeyboardMarkup:
    """Asosiy reply klaviatura"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🚀 Bot loyihalarim"),
                KeyboardButton(text="⚡ 200k Botlar"),
            ],
            [
                KeyboardButton(text="📋 Qanday ishlaydi"),
                KeyboardButton(text="⭐ Afzalliklar"),
            ],
            [
                KeyboardButton(text="💰 Narxlar"),
                KeyboardButton(text="❓ FAQ"),
            ],
            [
                KeyboardButton(text="📩 Bog'lanish"),
                KeyboardButton(text="📝 Buyurtma berish"),
            ],
            [
                KeyboardButton(text="💬 Sharhlar"),
                KeyboardButton(text="🌐 Saytga o'tish"),
            ],
        ],
        resize_keyboard=True,
        persistent=True,
        input_field_placeholder="Menyudan bo'limni tanlang...",
    )


def inline_start_kb() -> InlineKeyboardMarkup:
    """Start xabarida chiqadigan inline tugmalar"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🚀 Bot loyihalarim", callback_data="cat_all", style="primary"),
                InlineKeyboardButton(text="⚡ 200k Botlar", callback_data="info_twohundred", style="success"),
            ],
            [
                InlineKeyboardButton(text="📋 Qanday ishlaydi", callback_data="info_how"),
                InlineKeyboardButton(text="⭐ Afzalliklar", callback_data="info_advantages"),
            ],
            [
                InlineKeyboardButton(text="💰 Narxlar", callback_data="info_pricing"),
                InlineKeyboardButton(text="❓ FAQ", callback_data="info_faq"),
            ],
            [
                InlineKeyboardButton(text="📝 Buyurtma berish", url="https://t.me/abdurokhmandev", style="success"),
                InlineKeyboardButton(text="📩 Bog'lanish", callback_data="info_contact", style="primary"),
            ],
            [
                InlineKeyboardButton(text="🌐 codefy.uz", url=SITE_URL, style="primary"),
            ]
        ]
    )


def website_btn_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🌐 codefy.uz — rasmiy sayt",
                    url=SITE_URL,
                    style="primary",
                )
            ],
            [
                InlineKeyboardButton(text="◀️ Orqaga", callback_data="main_menu_back", style="danger")
            ]
        ]
    )


def order_btn_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📝 Buyurtma berish (Telegram)",
                    url="https://t.me/abdurokhmandev",
                    style="success",
                )
            ],
            [
                InlineKeyboardButton(text="◀️ Orqaga", callback_data="main_menu_back", style="danger")
            ]
        ]
    )
