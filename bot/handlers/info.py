import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from db.queries import get_twohundered
from keyboards.main_menu import order_btn_kb, website_btn_kb
from config import MEDIA_BASE_URL

router = Router()

HOW_TEXT = """
💡 <b>QANDAY ISHLAYMIZ?</b>
━━━━━━━━━━━━━━━━━━━

1️⃣ <b>Topshiriq (TZ) berish:</b>
Siz o'z loyihangiz va g'oyangiz haqida batafsil aytasiz.

2️⃣ <b>Loyihani muhokama qilish:</b>
Narxi, bajarilish muddati va zaruriy funksiyalar aniqlanadi.

3️⃣ <b>Dasturlash & Test:</b>
Loyiha eng zamonaviy texnologiyalarda tez va sifatli yoziladi.

4️⃣ <b>Topshirish & Qo'llab-quvvatlash:</b>
Loyiha serverga joylanadi va 1 oy bepul texnik yordam beriladi!
"""

ADVANTAGES_TEXT = """
⭐ <b>BIZNING AFZALLIKLARIMIZ</b>
━━━━━━━━━━━━━━━━━━━

⚡ <b>Tezkorlik:</b> Loyihalar belgilangan muddatda to'liq topshiriladi.
🛡 <b>Xavfsizlik:</b> 100% ishonchli va toza kod.
🎨 <b>Individual dizayn:</b> Har bir mijoz uchun alohida yondashuv.
💰 <b>Hamyonbop narxlar:</b> Sifat va narx mutanosibligi.
👨‍💻 <b>Shaxsiy ko'mak:</b> Har bir mijoz bilan bevosita dasturchi muloqot qiladi.
"""

PRICING_TEXT = """
💵 <b>XIZMATLAR VA NARXLAR</b>
━━━━━━━━━━━━━━━━━━━

🤖 <b>Telegram Botlar:</b>
└ 200 000 so'mdan boshlab

🌐 <b>Vebsaytlar (Landing / Portfolio):</b>
└ 500 000 so'mdan boshlab

📱 <b>Telegram Mini Apps (WebApps):</b>
└ 800 000 so'mdan boshlab

🔧 <b>CRM & Murakkab Tizimlar:</b>
└ Kelishilgan holda
"""

FAQ_TEXT = """
❓ <b>KO'P BERILADIGAN SAVOLLAR (FAQ)</b>
━━━━━━━━━━━━━━━━━━━

<b>Q: Loyiham qancha vaqtda tayyor bo'ladi?</b>
A: Oddiy botlar 1-2 kunda, murakkab vebsayt va tizimlar 3-7 kunda tayyor bo'ladi.

<b>Q: To'lov tartibi qanday?</b>
A: 50% oldindan to'lov, qolgan 50% loyiha to'liq topshirilgandan keyin.

<b>Q: Keyinchalik qo'llab-quvvatlaysizmi?</b>
A: Ha! Barcha loyihalarga 1 oy bepul texnik yordam beriladi.
"""

CONTACT_TEXT = """
📞 <b>BOG'LANISH VA ALOQA</b>
━━━━━━━━━━━━━━━━━━━

👨‍💻 <b>Dasturchi:</b> Abdurahmon
💬 <b>Telegram:</b> @abdurahmondevuz
🌐 <b>Rasmiy sayt:</b> https://codefy.uz
⏱ <b>Ish vaqti:</b> 09:00 - 22:00 (Har kuni)
"""


@router.message(F.text.in_({"💡 Qanday ishlaydi", "Qanday ishlaydi"}))
async def show_how(message: Message):
    await message.answer(HOW_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")


@router.callback_query(F.data == "info_how")
async def cb_show_how(callback: CallbackQuery):
    await callback.message.answer(HOW_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")
    await callback.answer()


@router.message(F.text.in_({"⭐ Afzalliklar", "Afzalliklar"}))
async def show_advantages(message: Message):
    await message.answer(ADVANTAGES_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")


@router.callback_query(F.data == "info_advantages")
async def cb_show_advantages(callback: CallbackQuery):
    await callback.message.answer(ADVANTAGES_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")
    await callback.answer()


@router.message(F.text.in_({"💵 Narxlar", "Narxlar"}))
async def show_pricing(message: Message):
    await message.answer(PRICING_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")


@router.callback_query(F.data == "info_pricing")
async def cb_show_pricing(callback: CallbackQuery):
    await callback.message.answer(PRICING_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")
    await callback.answer()


@router.message(F.text.in_({"❓ FAQ", "FAQ"}))
async def show_faq(message: Message):
    await message.answer(FAQ_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")


@router.callback_query(F.data == "info_faq")
async def cb_show_faq(callback: CallbackQuery):
    await callback.message.answer(FAQ_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")
    await callback.answer()


@router.message(F.text.in_({"📞 Bog'lanish", "Bog'lanish"}))
async def show_contact(message: Message):
    await message.answer(CONTACT_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")


@router.callback_query(F.data == "info_contact")
async def cb_show_contact(callback: CallbackQuery):
    await callback.message.answer(CONTACT_TEXT, reply_markup=order_btn_kb(), parse_mode="HTML")
    await callback.answer()


@router.message(F.text.in_({"📝 Buyurtma berish", "Buyurtma berish"}))
async def show_order(message: Message):
    text = (
        "📝 <b>BUYURTMA BERISH</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n\n"
        "Loyiha boshlash uchun menga Telegram orqali yozing.\n"
        "G'oyangizni aytishingiz bilan narxi va muddatini hisoblab beraman!"
    )
    await message.answer(text, reply_markup=order_btn_kb(), parse_mode="HTML")


@router.message(F.text.in_({"⚡ 200k Botlar", "Bot loyihalarim", "200minglik botlar"}))
async def show_twohundred(message: Message):
    await send_twohundred_info(message)


@router.callback_query(F.data == "info_twohundred")
async def cb_show_twohundred(callback: CallbackQuery):
    await send_twohundred_info(callback.message)
    await callback.answer()


async def send_twohundred_info(target):
    bots = await get_twohundered()

    if bots:
        for b in bots:
            text = (
                f"⚡ <b>{b['name'].upper()}</b>\n"
                f"💰 Narxi: <b>200 000 so'm</b>\n"
                f"━━━━━━━━━━━━━━━━━━━\n\n"
                f"{b['desc']}"
            )
            img = b.get("image")
            if img:
                photo_url = f"{MEDIA_BASE_URL}/{img}"
                try:
                    await target.answer_photo(
                        photo=photo_url,
                        caption=text,
                        reply_markup=order_btn_kb(),
                        parse_mode="HTML"
                    )
                    continue
                except Exception:
                    pass
            await target.answer(text, reply_markup=order_btn_kb(), parse_mode="HTML")
    else:
        text = (
            "⚡ <b>200 000 SO'MLIK BOTLAR</b>\n"
            "━━━━━━━━━━━━━━━━━━━\n\n"
            "Atigi <b>200 000 so'mga</b> quyidagi tayyor botlarni yaratib beraman:\n\n"
            "🔹 <b>Vizitka Bot:</b> Shaxsiy brend yoki biznes uchun axborot boti.\n"
            "🔹 <b>Katalog Bot:</b> Mahsulot va xizmatlarni ko'rsatish boti.\n"
            "🔹 <b>Qabul & Azo boti:</b> Foydalanuvchilar arizalarini yig'uvchi bot.\n"
            "🔹 <b>Feedback / Aloqa boti:</b> Mijozlar xabarlarini admin panelliga yuboruvchi bot.\n\n"
            "⚡ Har bir bot 1 kunda topshiriladi!"
        )
        await target.answer(text, reply_markup=order_btn_kb(), parse_mode="HTML")
