from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from typing import Tuple, Dict
import base64

class EncryptionService:
    @staticmethod
    def generate_key(key_length: int = 32) -> bytes:
        """生成随机加密密钥"""
        return get_random_bytes(key_length)

    @staticmethod
    def encrypt_data(data: bytes, key: bytes) -> Tuple[bytes, Dict]:
        """
        使用AES加密数据
        返回: (加密数据, 加密元数据)
        """
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        # 将二进制数据转换为base64字符串以便存储
        metadata = {
            "nonce": base64.b64encode(nonce).decode('utf-8'),
            "tag": base64.b64encode(tag).decode('utf-8'),
            "key": base64.b64encode(key).decode('utf-8'),
            "algorithm": "AES-EAX"
        }
        
        return ciphertext, metadata

    @staticmethod
    def decrypt_data(encrypted_data: bytes, metadata: Dict) -> bytes:
        """
        使用存储的元数据解密数据
        """
        key = base64.b64decode(metadata["key"])
        nonce = base64.b64decode(metadata["nonce"])
        tag = base64.b64decode(metadata["tag"])
        
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        data = cipher.decrypt_and_verify(encrypted_data, tag)
        return data 