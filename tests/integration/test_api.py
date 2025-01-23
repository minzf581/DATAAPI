"""集成测试"""
import pytest
from fastapi import status
import logging

# 配置日志记录器
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_health_check(test_client):
    """测试健康检查接口"""
    response = test_client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "healthy"}

def test_upload_data_success(test_client, mock_storage_client, test_file):
    """测试成功上传数据"""
    files = {"data_file": ("test.csv", test_file, "text/csv")}
    data = {
        "data_description": "Test dataset description",
        "privacy_algorithm": "AES",
        "access_policy": "public"
    }
    
    response = test_client.post("/api/data/upload", files=files, data=data)
    
    assert response.status_code == status.HTTP_200_OK
    assert "dataset_id" in response.json()
    assert "storage_path" in response.json()
    
    # 验证mock调用
    mock_storage_client.bucket.assert_called_once_with("your-bucket-name")
    mock_storage_client.bucket().blob.assert_called_once()
    mock_storage_client.bucket().blob().upload_from_string.assert_called_once()

def test_upload_data_invalid_request(test_client):
    """测试上传无效数据"""
    response = test_client.post("/api/data/upload", files={}, data={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_upload_data_storage_error(test_client, mock_storage_client, test_file):
    """测试存储错误情况"""
    # 设置mock抛出异常
    mock_storage_client.bucket().blob().upload_from_string.side_effect = Exception("Storage error")
    
    files = {"data_file": ("test.csv", test_file, "text/csv")}
    data = {
        "data_description": "Test dataset description",
        "privacy_algorithm": "AES",
        "access_policy": "public"
    }
    
    response = test_client.post("/api/data/upload", files=files, data=data)
    
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR 