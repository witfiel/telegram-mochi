from sqlalchemy.ext.asyncio import create_async_engine, Async_session, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.config.settings import settings
from src.utils.logger import log

Base = declarative_base()

class Database:

    def __init__(self):
        self.engine = create_async_engine(
                settings.database_url,
                echo=False,
                future=True
        )
        self.SessionLocal = async_sessionmaker(
                self.engine,
                autocommit=False,
                autoflush=False,
                future=True
        )
        log.info(f"Database initialized: {settings.database_url}")
        async def create_labels(self):
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            log.info("Database tables created")

        async def close(self):
            await self.engine.dispose()
            log.info("Database connection closed")

        def get_session(self) -> AsyncSession:
            return self.SessionLocal()

db = Database()

async def get_db() -> AsyncSession:
    async with db.get_session() as session:
        try:
            yield session
        finally:
            await session.close()
