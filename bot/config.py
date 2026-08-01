import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Bot token — Railway da Variable sifatida qo'shiladi
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

# DB yo'li — Django loyihasi bilan bir xil BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH: str = os.getenv("DB_PATH", str(BASE_DIR / "db.sqlite3"))

# Media fayllar Railway Volume orqali xizmat qiladi
MEDIA_BASE_URL: str = os.getenv("MEDIA_BASE_URL", "https://codefy.uz/media")
SITE_URL: str = "https://codefy.uz"

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable topilmadi!")
