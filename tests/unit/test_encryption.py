import pytest
from app.services.encryption import EncryptionService

def test_generate_key():
    """测试密钥生成"""
    key_length = 32
    key = EncryptionService.generate_key(key_length)
    assert len(key) == key_length
    assert isinstance(key, bytes)

def test_encrypt_decrypt_data():
    """测试数据加密和解密"""
    # 准备测试数据
    test_data = b"This is a test message"
    key = EncryptionService.generate_key()
    
    # 加密数据
    encrypted_data, metadata = EncryptionService.encrypt_data(test_data, key)
    
    # 验证加密结果
    assert encrypted_data != test_data
    assert isinstance(encrypted_data, bytes)
    assert "nonce" in metadata
    assert "tag" in metadata
    assert "key" in metadata
    assert "algorithm" in metadata
    assert metadata["algorithm"] == "AES-EAX"
    
    # 解密数据
    decrypted_data = EncryptionService.decrypt_data(encrypted_data, metadata)
    
    # 验证解密结果
    assert decrypted_data == test_data

def test_encryption_different_keys():
    """测试使用不同密钥加密的结果不同"""
    test_data = b"This is a test message"
    key1 = EncryptionService.generate_key()
    key2 = EncryptionService.generate_key()
    
    encrypted_data1, _ = EncryptionService.encrypt_data(test_data, key1)
    encrypted_data2, _ = EncryptionService.encrypt_data(test_data, key2)
    
    assert encrypted_data1 != encrypted_data2

def test_encryption_same_data():
    """测试相同数据使用相同密钥加密的结果不同（由于随机nonce）"""
    test_data = b"This is a test message"
    key = EncryptionService.generate_key()
    
    encrypted_data1, _ = EncryptionService.encrypt_data(test_data, key)
    encrypted_data2, _ = EncryptionService.encrypt_data(test_data, key)
    
    assert encrypted_data1 != encrypted_data2

def test_decrypt_with_wrong_metadata():
    """测试使用错误的元数据解密"""
    test_data = b"This is a test message"
    key = EncryptionService.generate_key()
    
    encrypted_data, metadata = EncryptionService.encrypt_data(test_data, key)
    
    # 修改元数据中的tag
    metadata["tag"] = "invalid_tag"
    
    with pytest.raises(ValueError):
        EncryptionService.decrypt_data(encrypted_data, metadata) 