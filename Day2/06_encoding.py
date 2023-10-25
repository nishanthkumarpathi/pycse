import base64

def encode_base64(data):
    return base64.b64encode(data.encode()).decode()

def decode_base64(data):
    return base64.b64decode(data.encode()).decode()

encoded = encode_base64("secret")
print(encoded)  # Outputs: c2VjcmV0

decoded = decode_base64(encoded)
print(decoded)  # Outputs: secret