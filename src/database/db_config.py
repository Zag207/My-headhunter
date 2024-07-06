from src.load_env_vars import DB_ACCESS
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

async_engine = create_async_engine(
    url=f"sqlite+aiosqlite:///{DB_ACCESS}",
    echo=True,
)

async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
