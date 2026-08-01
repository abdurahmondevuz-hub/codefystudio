import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from db.queries import get_twohundered
from keyboards.main_menu import order_btn_kb
from config import MEDIA_BASE_URL

router = Router()

HOW_TEXT = """
📋 <b>QANDAY ISHLAYDI?</b>
━━━━━━━━━━━━━━━━━━━
Uzoq muzokarasiz — ssenariyni belgilaymiz, ko'rsatamiz, ishga tushiramiz.

<b>01 · 15 daqiqa — Ssenariyni belgilaymiz</b>
└ Mijoz yo'lini, kerakli funksiyalarni va murojaat qayerga tushishini aniqlaymiz.

<b>02 · Namuna — Ishlaydigan namunani ko'rsatamiz</b>
└ Ekranlar va asosiy logikani ishlab chiqishdan oldin tekshirib olasiz.

<b>03 · Ishga tushirish — Serverga joylab, sinovdan o'tkazamiz</b>
└ Telegram, baza va kerakli integratsiyalarni ulaymiz.
"""

ADVANTAGES_TEXT = """
⭐ <b>AFZALLIKLAR</b>
━━━━━━━━━━━━━━━━━━━
Nega aynan biz bilan ishlash kerak?
<i>Shunchaki kod yozmaymiz — biznesingiz uchun tayyor, xavfsiz va tezkor yechim taqdim etamiz.</i>

💻 <b>100% Manba kodi:</b>
└ Loyihangizning barcha kodi va fayllari to'liq sizga topshiriladi. Hech qanday yashirin cheklovlarsiz.

🖥 <b>Serverga bepul o'rnatish:</b>
└ Serverni sozlash, domenni ulash va botni bexato ishga tushirishda to'g'ridan-to'g'ri bepul amaliy yordam beramiz.

⚡ <b>Yuqori tezlik va xavfsizlik:</b>
└ Python & Django/Aiogram 3 texnologiyalari asosida yozilgan kod yuqori yuklamalarga chidamli va o'ta tez ishlaydi.

🛡 <b>30 kunlik texnik kafolat:</b>
└ Loyiha topshirilgandan keyin ham 1 oy davomida bepul texnik yordam va maslahatlar taqdim etiladi.
"""

PRICING_TEXT = """
💰 <b>NARXLAR VA TARIFLAR</b>
━━━━━━━━━━━━━━━━━━━
Vazifangizga mos qulay yechim:

🤖 <b>TELEGRAM-BOTLAR:</b>

1️⃣ <b>Tayyor bot (Ommabop)</b>
└ Narxi: <b>200 000 so'm</b>
└ Kino/fayl yetkazish, anketa, oddiy menyu — shablon asosida tezkor ishga tushirish (1–2 kunda).

2️⃣ <b>Individual bot & Mini App (Contact Sales)</b>
└ Narxi: <b>Kelishilgan holda</b>
└ Katalog, kartochkalar, Mini App / Web-ilova, yozilish, statuslar, rollar, CRM va istalgan murakkab biznes-jarayon uchun.

🌐 <b>SAYTLAR:</b>

1️⃣ <b>Landing Page / Veb-sayt</b>
└ Narxi: <b>Kelishilgan holda</b>
└ Biznes taklifingiz, xizmatlaringiz, ariza formasi va Telegram ulanishi bilan zamonaviy responsive sayt.
"""

FAQ_TEXT = """
❓ <b>KO'P BERILADIGAN SAVOLLAR (FAQ)</b>
━━━━━━━━━━━━━━━━━━━

<b>Q: Qancha vaqt ketadi?</b>
A: Tayyor bot — 1–2 kun. Individual loyiha — hajmga qarab, oldindan aniq muddat kelishiladi.

<b>Q: To'lov va CRM ulash mumkinmi?</b>
A: Ha — Payme/Click to'lov tizimlari, jadval yoki CRM integratsiyasi individual loyihalarga kiritiladi.

<b>Q: Kontent va matnni ham tayyorlaysizmi?</b>
A: Asosiy tuzilmani taklif qilamiz, lekin yakuniy matn va rasmlarni mijoz bilan birga aniqlaymiz.

<b>Q: Bot bilan Mini App farqi nima?</b>
A: Bot — matn/tugmalar orqali muloqot. Mini App — Telegram ichida ochiladigan to'liq interfeys (katalog, savatcha va h.k.).
"""

CONTACT_TEXT = """
📩 <b>BOG'LANISH</b>
━━━━━━━━━━━━━━━━━━━
<b>Loyihangizni bugun boshlaymizmi?</b>
Bitta xabarda vazifani yozing — shaxsan javob beraman, format va narxni birga aniqlaymiz.

👨‍💻 <b>Murojaat qilish:</b> @abdurokhmandev
📢 <b>Telegram kanal:</b> @abdurahmondevuz
📍 <b>Manzil:</b> Tashkent, Uzbekistan
🕒 <b>Ish vaqti:</b> 09:00 — 22:00
"""


@router.message(F.text.in_({"💡 Qanday ishlaydi", "Qanday ishlaydi", "📋 Qanday ishlaydi"}))
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


@router.message(F.text.in_({"💵 Narxlar", "Narxlar", "💰 Narxlar"}))
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


@router.message(F.text.in_({"📞 Bog'lanish", "Bog'lanish", "📩 Bog'lanish"}))
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
        "G'oyangizni aytishingiz bilan format va narxni birga aniqlaymiz!"
    )
    await message.answer(text, reply_markup=order_btn_kb(), parse_mode="HTML")


@router.message(F.text.in_({"⚡ 200k Botlar", "Bot loyihalarim", "🚀 Bot loyihalarim", "200minglik botlar"}))
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
            "⚡ <b>200 000 SO'MLIK TARIF BOTLARI</b>\n"
            "━━━━━━━━━━━━━━━━━━━\n"
            "Tayyor shablon asosida — 1–2 kunda tezkor ishga tushadi:\n\n"
            "🎬 <b>Kino bot:</b> Foydalanuvchi kod yuboradi, bot mos kinoni topib beradi.\n"
            "📥 <b>Video yuklovchi bot:</b> Instagram, YouTube va TikTok tarmoqlaridan videolarni yuklab beradi.\n"
            "🎵 <b>Musiqa topuvchi bot:</b> Ovoz, matn yoki nom bo'yicha qo'shiqlarni izlab topib beradi.\n"
            "📋 <b>Anketa & Qabul boti:</b> Foydalanuvchilar murojaat va anketalarini yig'ib beradi.\n"
        )
        await target.answer(text, reply_markup=order_btn_kb(), parse_mode="HTML")
