from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
MEDIA_DIR = ROOT_DIR / "media"
DATABASE_URL = f"sqlite+aiosqlite:///{ROOT_DIR}/db.sqlite3"
CHUNKS_QUANTITY = 100
