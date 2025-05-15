import hashlib

res = hashlib.md5("hello".encode()).hexdigest()
print(res)