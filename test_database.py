import asyncio
from src.core.database import db
from src.utils.logger import log

async def main():
    log.info("Testing database initialize")
    await db.create_tables()
    await db.close()
    log.info("Database test passed")

if __name__ == "__main__":
    asyncio.run(main())
