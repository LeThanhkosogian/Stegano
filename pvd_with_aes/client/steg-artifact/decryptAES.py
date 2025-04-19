from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

# Hàm giải mã thông điệp bằng AES-256
def decrypt_message(encrypted_message, password):
    if not encrypted_message:
        return "Giải mã thất bại: Không có dữ liệu để giải mã"
    try:
        encrypted_data = base64.b64decode(encrypted_message)
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        key = hashlib.sha256(password.encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        padded_message = cipher.decrypt(ciphertext)
        message = unpad(padded_message, AES.block_size).decode('utf-8')
        return message
    except Exception as e:
        return f"Giải mã thất bại: {str(e)}"
