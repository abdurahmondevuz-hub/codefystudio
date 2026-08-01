from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def categories_kb(categories: list[dict]) -> InlineKeyboardMarkup:
    buttons = []
    for cat in categories:
        buttons.append([InlineKeyboardButton(
            text=f"📁 {cat['name']}", callback_data=f"cat_{cat['id']}"
        )])
    buttons.append([InlineKeyboardButton(text="📋 Barcha loyihalar", callback_data="cat_all")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def projects_list_kb(projects: list[dict], back_callback: str = "back_cats") -> InlineKeyboardMarkup:
    buttons = []
    for proj in projects:
        title = proj['title'][:32] + "..." if len(proj['title']) > 35 else proj['title']
        buttons.append([InlineKeyboardButton(
            text=f"🔹 {title}", callback_data=f"proj_{proj['id']}"
        )])
    buttons.append([InlineKeyboardButton(text="◀️ Orqaga", callback_data=back_callback)])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def project_detail_kb(project: dict) -> InlineKeyboardMarkup:
    buttons = []
    row = []
    if project.get("telegram_bot_url"):
        row.append(InlineKeyboardButton(text="🤖 Bot", url=project["telegram_bot_url"]))
    if project.get("website_url"):
        row.append(InlineKeyboardButton(text="🌐 Sayt", url=project["website_url"]))
    if row:
        buttons.append(row)
    if project.get("github_url"):
        buttons.append([InlineKeyboardButton(text="💻 GitHub kodi", url=project["github_url"])])
    buttons.append([InlineKeyboardButton(text="◀️ Orqaga", callback_data="back_cats")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
