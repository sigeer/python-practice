from Crypto.Cipher import DES
import hashlib
import base64

key = hashlib.md5('123456789'.encode()).hexdigest()[:8].encode()

def pad(text):
    # 如果text不是8的倍数【加密文本text必须为8的倍数！】，补足为8的倍数
    len_txt = len(text)
    if len_txt % 8 == 0:
        return text
    
    return text +  ' ' * (8 - len_txt % 8)


des = DES.new(key, DES.MODE_CBC, iv=key)  # 创建DES实例
text = 'Python rocks!'
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text.encode())  # 加密
print(encrypted_text)
encrypted_b64 = base64.b64encode(encrypted_text).decode()
print(encrypted_b64)

print(base64.b64decode(encrypted_b64))
des_decode = DES.new(key, DES.MODE_CBC, iv=key)
plain_text = des_decode.decrypt(encrypted_text).decode().rstrip(' ')  # 解密
print(plain_text)