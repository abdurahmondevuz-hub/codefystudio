from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def categories_kb(categories: list[dict]) -> InlineKeyboardMarkup:
    """Kategoriyalar — har biri alohida rangli emoji bilan"""
    color_icons = ["🟣", "🔵", "🟢", "🟡", "🟠", "🔴", "⚪", "🟤"]
    buttons = []
    for i, cat in enumerate(categories):
        icon = color_icons[i % len(color_icons)]
        buttons.append([InlineKeyboardButton(
            text=f"{icon} {cat['name']}",
            callback_data=f"cat_{cat['id']}"
        )])
    buttons.append([
        InlineKeyboardButton(text="📋 Barcha loyihalar", callback_data="cat_all")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def projects_list_kb(projects: list[dict], back_callback: str = "back_cats") -> InlineKeyboardMarkup:
    """Loyihalar ro'yxati"""
    icons = ["⚡", "🔥", "💎", "🚀", "✨", "🌟", "💡", "🎯"]
    buttons = []
    for i, proj in enumerate(projects):
        icon = icons[i % len(icons)]
        title = proj['title'][:30] + "..." if len(proj['title']) > 33 else proj['title']
        buttons.append([InlineKeyboardButton(
            text=f"{icon} {title}",
            callback_data=f"proj_{proj['id']}"
        )])
    buttons.append([
        InlineKeyboardButton(text="◀️ Kategoriyalar", callback_data=back_callback)
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def project_detail_kb(project: dict) -> InlineKeyboardMarkup:
    """Loyiha havolalari"""
    buttons = []

    # Asosiy havolalar
    link_row = []
    if project.get("telegram_bot_url"):
        link_row.append(InlineKeyboardButton(text="🤖 Bot", url=project["telegram_bot_url"]))
    if project.get("website_url"):
        link_row.append(InlineKeyboardButton(text="🌐 Sayt", url=project["website_url"]))
    if link_row:
        buttons.append(link_row)

    if project.get("github_url"):
        buttons.append([
            InlineKeyboardButton(text="💻 GitHub — kodni ko'rish", url=project["github_url"])
        ])

    # Buyurtma tugmasi
    buttons.append([
        InlineKeyboardButton(
            text="📩 Buyurtma berish",
            url="https://t.me/abdurahmondevuz"
        )
    ])

    buttons.append([
        InlineKeyboardButton(text="◀️ Orqaga", callback_data="back_cats")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_cats_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="◀️ Kategoriyalarga qaytish", callback_data="back_cats")
        ]]
    )
