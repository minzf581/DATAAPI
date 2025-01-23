from cryptography.fernet import Fernet
import base64
import os

def generate_encryption_key():
    """生成加密密钥"""
    return Fernet.generate_key().decode()

def encrypt_data(data: bytes, key: str) -> bytes:
    """使用给定的密钥加密数据"""
    f = Fernet(key.encode())
    return f.encrypt(data)

def decrypt_data(encrypted_data: bytes, key: str) -> bytes:
    """使用给定的密钥解密数据"""
    f = Fernet(key.encode())
    return f.decrypt(encrypted_data) 