import pytest
from app.models.data import Dataset
from datetime import datetime
from sqlalchemy import select

def test_dataset_model_creation():
    """测试创建数据集模型"""
    dataset = Dataset(
        description="Test dataset",
        privacy_algorithm="AES",
        access_policy="private",
        file_path="test/path/file.txt",
        encryption_metadata={
            "algorithm": "AES-EAX",
            "key": "test_key",
            "nonce": "test_nonce",
            "tag": "test_tag"
        }
    )
    
    assert dataset.description == "Test dataset"
    assert dataset.privacy_algorithm == "AES"
    assert dataset.access_policy == "private"
    assert dataset.file_path == "test/path/file.txt"
    assert dataset.encryption_metadata == {
        "algorithm": "AES-EAX",
        "key": "test_key",
        "nonce": "test_nonce",
        "tag": "test_tag"
    }
    assert isinstance(dataset.created_at, datetime)
    assert isinstance(dataset.updated_at, datetime)

@pytest.mark.asyncio
async def test_dataset_db_operations(test_db):
    """测试数据集数据库操作"""
    # 创建测试数据集
    dataset = Dataset(
        description="Test dataset",
        privacy_algorithm="AES",
        access_policy="private",
        file_path="test/path/file.txt",
        encryption_metadata={
            "algorithm": "AES-EAX",
            "key": "test_key",
            "nonce": "test_nonce",
            "tag": "test_tag"
        }
    )
    
    # 添加到数据库
    test_db.add(dataset)
    await test_db.commit()
    await test_db.refresh(dataset)
    
    # 验证数据集已被创建
    result = await test_db.execute(select(Dataset).filter_by(id=dataset.id))
    db_dataset = result.scalar_one()
    assert db_dataset.description == "Test dataset"
    assert db_dataset.privacy_algorithm == "AES"
    
    # 更新数据集
    db_dataset.description = "Updated test dataset"
    await test_db.commit()
    await test_db.refresh(db_dataset)
    
    # 验证更新
    result = await test_db.execute(select(Dataset).filter_by(id=dataset.id))
    updated_dataset = result.scalar_one()
    assert updated_dataset.description == "Updated test dataset"
    
    # 删除数据集
    await test_db.delete(db_dataset)
    await test_db.commit()
    
    # 验证删除
    result = await test_db.execute(select(Dataset).filter_by(id=dataset.id))
    assert result.first() is None 