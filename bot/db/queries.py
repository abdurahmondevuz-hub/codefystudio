import aiosqlite
import sys
from pathlib import Path

# Bot ichidan import qilish uchun path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import DB_PATH


async def get_categories() -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            'SELECT id, name, slug FROM app_category ORDER BY "order", name'
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def get_projects_by_category(category_id: int) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """SELECT id, title, short_description, cover_image, price, delivery_time
               FROM app_myproject
               WHERE category_id = ? AND is_active = 1
               ORDER BY created_at DESC""",
            (category_id,)
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def get_all_projects() -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """SELECT id, title, short_description, cover_image, price, delivery_time
               FROM app_myproject WHERE is_active = 1
               ORDER BY created_at DESC"""
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def get_project_detail(project_id: int) -> dict | None:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            """SELECT p.id, p.title, p.short_description, p.full_description,
                      p.cover_image, p.telegram_bot_url, p.website_url,
                      p.github_url, p.technologies, p.price, p.delivery_time,
                      c.name as category_name
               FROM app_myproject p
               LEFT JOIN app_category c ON p.category_id = c.id
               WHERE p.id = ? AND p.is_active = 1""",
            (project_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return dict(row) if row else None


async def get_reviews() -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT name, kasb, stars, izoh FROM app_izohlar LIMIT 5"
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]


async def get_twohundered() -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT id, image, name, desc FROM app_twohundered"
        ) as cursor:
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
