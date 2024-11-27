from Crypto.Cipher import AES
from binascii import unhexlify

# Datos proporcionados
cipher_text_hex = "8d9850c884aa4e8a4b73ca422ebb0195"
key_hex = "02672469526323625526541869952461"
iv_hex = "84532186251485468562186856456566"

# Convertir de hexadecimal a bytes
cipher_text = unhexlify(cipher_text_hex)
key = unhexlify(key_hex)
iv = unhexlify(iv_hex)

# Crear el descifrador AES en modo CBC
cipher = AES.new(key, AES.MODE_CBC, iv)

# Descifrar el mensaje
decrypted_text = cipher.decrypt(cipher_text)

# Mostrar el texto descifrado
print(decrypted_text.decode('utf-8').strip())
