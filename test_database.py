import asyncio
from src.core.database import db, Base
from src.models import User, Chat
from src.utils.logger import log

async def main():
    log.info("Testing database initialize")
    await db.create_tables()

    log.info(f"User table created: {User.__tablename__}")
    log.info(f"Chat table: {Chat.__tablename__}")

    log.info(f"User columns: {[col.name for col in User.__table__.columns]}")
    log.info(f"Chat columns: {[col.name for col in Chat.__table__.columns]}")

    await db.close()
    log.info("Database test passed")

if __name__ == "__main__":
    asyncio.run(main())
