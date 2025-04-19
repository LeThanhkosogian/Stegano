from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

# Hàm mã hóa thông điệp bằng AES-256
def encrypt_message(message, password):
    key = hashlib.sha256(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC)
    padded_message = pad(message.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_message)
    return base64.b64encode(cipher.iv + ciphertext).decode('utf-8')
