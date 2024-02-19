import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib

def aes_encrypt(key, plaintext):
    # 创建 AES 密钥对象
    aes_key = key[:32]  # AES-256 需要一个 32 字节的密钥
    backend = default_backend()
    cipher = Cipher(algorithms.AES(aes_key), modes.ECB(), backend=backend)
    
    # 创建加密器并加密数据
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # 使用 base64 进行编码，并返回加密后的结果（包括 IV）
    encrypted_data = ciphertext
    return base64.b64encode(encrypted_data).decode()

def aes_decrypt(key, ciphertext: str):
    # 使用 base64 进行解码，并提取初始化向量（IV）
    encrypted_data = base64.b64decode(ciphertext)

    # 创建 AES 密钥对象
    aes_key = key[:32]  # AES-256 需要一个 32 字节的密钥
    backend = default_backend()
    cipher = Cipher(algorithms.AES(aes_key), modes.ECB(), backend=backend)
    
    # 创建解密器并解密数据
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # 去除填充数据，并返回解密结果
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()
    return data.decode()

# 用于测试的密钥和明文数据
key = hashlib.md5(b'KEY').hexdigest().upper().encode()
plaintext = 'aaa'

# 加密数据并将结果转换为字符串形式
encrypted_data = aes_encrypt(key, plaintext.encode())
print("加密后的数据:", encrypted_data)

# 解密数据
decrypted_data = aes_decrypt(key, encrypted_data)
print("解密后的数据:", decrypted_data)
