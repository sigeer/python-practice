import hashlib

def encrypt_pwd(pwd: str, uid: int):
    salt = hashlib.md5(pwd.encode()).hexdigest()[:8]
    return hashlib.sha256(f"{pwd}_{salt}_{uid}".encode()).hexdigest()

pwd = "aA123456"
print(encrypt_pwd(pwd, 1))

t1 = "123456789"
print(hashlib.md5(t1.encode()).hexdigest())
