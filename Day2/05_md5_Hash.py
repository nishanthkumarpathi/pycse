import hashlib

def generate_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

print(generate_md5("password"))