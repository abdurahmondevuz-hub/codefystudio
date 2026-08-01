from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def categories_kb(categories: list[dict]) -> InlineKeyboardMarkup:
    """Kategoriyalar — primary rang va Orqaga tugmasi bilan"""
    buttons = []
    icons = ["☕", "🌐", "🤖", "📱", "🛠", "💎", "🔥", "🎯"]
    for i, cat in enumerate(categories):
        icon = icons[i % len(icons)]
        buttons.append([InlineKeyboardButton(
            text=f"{icon}  {cat['name']}",
            callback_data=f"cat_{cat['id']}",
            style="primary",
        )])
    buttons.append([InlineKeyboardButton(
        text="📋  Barcha loyihalar",
        callback_data="cat_all",
        style="primary",
    )])
    # Orqaga qaytish tugmasi
    buttons.append([InlineKeyboardButton(
        text="◀️  Orqaga",
        callback_data="main_menu_back",
        style="danger",
    )])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def projects_list_kb(projects: list[dict], back_callback: str = "back_cats") -> InlineKeyboardMarkup:
    """Loyihalar ro'yxati"""
    buttons = []
    for proj in projects:
        title = proj['title'][:30] + "..." if len(proj['title']) > 33 else proj['title']
        buttons.append([InlineKeyboardButton(
            text=f"⚡  {title}",
            callback_data=f"proj_{proj['id']}",
        )])
    buttons.append([InlineKeyboardButton(
        text="◀️  Orqaga",
        callback_data=back_callback,
        style="danger",
    )])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def project_detail_kb(project: dict) -> InlineKeyboardMarkup:
    """Loyiha havolalari"""
    buttons = []

    # Havola tugmalari (agar kiritilgan bo'lsa)
    link_row = []
    if project.get("telegram_bot_url"):
        link_row.append(InlineKeyboardButton(
            text="🤖  Bot",
            url=project["telegram_bot_url"],
            style="primary",
        ))
    if project.get("website_url"):
        link_row.append(InlineKeyboardButton(
            text="🌐  Sayt",
            url=project["website_url"],
            style="primary",
        ))
    if link_row:
        buttons.append(link_row)

    if project.get("github_url"):
        buttons.append([InlineKeyboardButton(
            text="💻  GitHub — kodni ko'rish",
            url=project["github_url"],
        )])

    # Buyurtma tugmasi — success (yashil)
    buttons.append([InlineKeyboardButton(
        text="📩  Buyurtma berish",
        url="https://t.me/abdurokhmandev",
        style="success",
    )])

    # Orqaga — danger (qizil)
    buttons.append([InlineKeyboardButton(
        text="◀️  Orqaga",
        callback_data="back_cats",
        style="danger",
    )])

    return InlineKeyboardMarkup(inline_keyboard=buttons)
