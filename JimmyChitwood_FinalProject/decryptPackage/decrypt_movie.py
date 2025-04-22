import json
from cryptography.fernet import Fernet

class MovieDecryptor:
    def __init__(self, encrypted_file_path):
        self.encrypted_file_path = encrypted_file_path
        # Replace the string below with the actual Fernet key you get from the instructor
        self.fernet_key = b"GusN5ceicQjGeKNr0gedUkjZ6h4I8xXm6Thx_issRko="
        self.fernet = Fernet(self.fernet_key)

    def decrypt_movie(self, group_name):
        with open(self.encrypted_file_path, 'r') as f:
            encrypted_data = json.load(f)

        encrypted_message = encrypted_data.get(group_name, [None])[0]
        if encrypted_message:
            decrypted_bytes = self.fernet.decrypt(encrypted_message.encode())
            return decrypted_bytes.decode()
        else:
            return "No message found for group."
