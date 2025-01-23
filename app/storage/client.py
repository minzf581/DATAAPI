"""存储客户端模块"""
from google.cloud import storage
from fastapi import Depends
from functools import lru_cache

@lru_cache()
def get_storage_client():
    """获取存储客户端"""
    return storage.Client() 