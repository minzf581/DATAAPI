from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import get_settings
from typing import AsyncGenerator
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = get_settings()
DATABASE_URL = settings.DATABASE_URL

# 创建数据库引擎
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
    pool_pre_ping=True,
    pool_recycle=1800,
)

# 创建会话工厂
async_session_factory = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# 创建基类
Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """获取数据库会话"""
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            logger.error(f"数据库会话错误: {str(e)}")
            await session.rollback()
            raise 