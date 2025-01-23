from google.cloud import storage
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

def get_storage_client():
    """获取 Google Cloud Storage 客户端"""
    try:
        return storage.Client()
    except Exception as e:
        logger.error(f"Failed to create storage client: {e}")
        raise HTTPException(
            status_code=500,
            detail="Storage client initialization failed"
        ) 