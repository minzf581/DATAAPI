"""测试配置文件"""
import pytest
import asyncio
import logging
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from unittest.mock import MagicMock
from typing import AsyncGenerator
from app.main import app
from app.database.database import Base, get_db, async_session_factory
from app.storage.client import get_storage_client

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def event_loop():
    """创建一个session作用域的事件循环"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_engine():
    """创建测试数据库引擎"""
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:postgres@localhost:5432/test_db",
        echo=True,
        future=True,
        pool_pre_ping=True,
        pool_recycle=1800,
    )
    
    # 创建所有表
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    # 清理
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()

@pytest.fixture
async def test_db(test_engine):
    """创建测试数据库会话"""
    TestingSessionLocal = sessionmaker(
        test_engine, 
        class_=AsyncSession, 
        expire_on_commit=False
    )
    
    async with TestingSessionLocal() as session:
        try:
            yield session
        finally:
            await session.rollback()
            await session.close()

@pytest.fixture
def mock_storage_client():
    """创建模拟存储客户端"""
    mock_client = MagicMock()
    mock_bucket = MagicMock()
    mock_blob = MagicMock()
    
    mock_client.bucket.return_value = mock_bucket
    mock_bucket.blob.return_value = mock_blob
    mock_blob.upload_from_string.return_value = None
    
    # 设置mock客户端的属性以避免认证
    mock_client.credentials = None
    mock_client._credentials = None
    mock_client._http = None
    
    app.dependency_overrides[get_storage_client] = lambda: mock_client
    yield mock_client
    del app.dependency_overrides[get_storage_client]

@pytest.fixture
def test_file():
    """创建测试文件数据"""
    return b"test data"

@pytest.fixture
def test_client(test_db):
    """创建测试客户端"""
    logger.info("创建测试客户端")
    
    async def override_get_db():
        try:
            yield test_db
        except Exception:
            await test_db.rollback()
            raise
            
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as client:
        yield client
    
    del app.dependency_overrides[get_db] 