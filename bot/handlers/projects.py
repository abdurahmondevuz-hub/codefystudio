import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from db.queries import get_projects_by_category, get_all_projects, get_project_detail
from keyboards.project_kb import projects_list_kb, project_detail_kb
from config import MEDIA_BASE_URL

router = Router()


@router.callback_query(F.data == "cat_all")
async def show_all_projects(callback: CallbackQuery):
    projects = await get_all_projects()
    if not projects:
        await callback.message.edit_text("😔 Hozircha loyihalar yo'q.")
        return
    text = (
        f"🗂 <b>BARCHA LOYIHALAR</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n\n"
        f"Jami: <b>{len(projects)} ta</b> loyiha\n\n"
        f"Batafsil ko'rish uchun tanlang 👇"
    )
    await callback.message.edit_text(text, reply_markup=projects_list_kb(projects), parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data.startswith("cat_"))
async def show_projects_by_category(callback: CallbackQuery):
    cat_id = int(callback.data.split("_")[1])
    projects = await get_projects_by_category(cat_id)
    if not projects:
        await callback.message.edit_text(
            "😔 Bu kategoriyada hozircha loyihalar yo'q.\n\n"
            "Tez orada yangi loyihalar qo'shiladi! 🔜",
            reply_markup=None
        )
        await callback.answer()
        return
    text = (
        f"🗂 <b>LOYIHALAR</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n\n"
        f"Jami: <b>{len(projects)} ta</b> loyiha\n\n"
        f"Batafsil ko'rish uchun tanlang 👇"
    )
    await callback.message.edit_text(text, reply_markup=projects_list_kb(projects), parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data.startswith("proj_"))
async def show_project_detail(callback: CallbackQuery):
    proj_id = int(callback.data.split("_")[1])
    project = await get_project_detail(proj_id)

    if not project:
        await callback.answer("Loyiha topilmadi!", show_alert=True)
        return

    # Chiroyli karta
    lines = [
        f"⚡ <b>{project['title'].upper()}</b>",
        "━━━━━━━━━━━━━━━━━━━",
    ]

    if project.get("category_name"):
        lines.append(f"📁 <i>{project['category_name']}</i>")
    lines.append("")

    desc = project.get("full_description") or project.get("short_description") or ""
    if desc:
        lines.append(f"📝 {desc}")
        lines.append("")

    lines.append("━━━━━━━━━━━━━━━━━━━")

    if project.get("technologies"):
        lines.append(f"🛠 <b>Stack:</b>  {project['technologies']}")

    if project.get("price"):
        lines.append(f"💰 <b>Narxi:</b>  {project['price']}")

    if project.get("delivery_time"):
        lines.append(f"⏱ <b>Muddat:</b>  {project['delivery_time']}")

    lines.append("━━━━━━━━━━━━━━━━━━━")
    lines.append("🔗 Havolalar ↓")

    text = "\n".join(lines)
    kb = project_detail_kb(project)
    cover = project.get("cover_image")

    if cover:
        photo_url = f"{MEDIA_BASE_URL}/{cover}"
        try:
            await callback.message.answer_photo(
                photo=photo_url,
                caption=text,
                reply_markup=kb,
                parse_mode="HTML"
            )
            try:
                await callback.message.delete()
            except TelegramBadRequest:
                pass
        except Exception:
            await callback.message.edit_text(text, reply_markup=kb, parse_mode="HTML")
    else:
        await callback.message.edit_text(text, reply_markup=kb, parse_mode="HTML")

    await callback.answer()
