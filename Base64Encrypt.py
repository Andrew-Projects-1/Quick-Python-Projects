import base64

def encrypt(plaintext):
    encoded_string = base64.b64encode(plaintext.encode('utf-8'))
    return encoded_string.decode('utf-8')

def decrypt(encrypted_string):
    decoded_string = base64.b64decode(encrypted_string.encode('utf-8'))
    return decoded_string.decode('utf-8')

# Test the function
plaintext = "This is a secret message"
print(f"Original String: {plaintext}")
encrypted_string = encrypt(plaintext)
print(f"Encrypted string: {encrypted_string}")
decrypted_string = decrypt(encrypted_string)
print(f"Decrypted string: {decrypted_string}")
