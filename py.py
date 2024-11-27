def rot47(text):
    return ''.join(
        [chr(33 + ((ord(char) - 33 + 47) % 94)) if 33 <= ord(char) <= 126 else char for char in text]
    )

# Texto cifrado
cipher_text = "h3rg3i_a4cvj4v3"

# Descifrar
decoded_text = rot47(cipher_text)
print(decoded_text)
