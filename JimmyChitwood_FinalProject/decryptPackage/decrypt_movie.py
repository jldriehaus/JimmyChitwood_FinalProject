# File Name : JimmyChitwood_FinalProject
# Student Name: Jack Driehaus
# email:  driehajl@mail.uc.edu
# Assignment Number: Assignment Final Project
# Due Date:   04/24/25
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  Decrypt text that shows a location and a movie title then take a picture there and have it display

# Brief Description of what this module does. Decrypts the code that shows the movie 
# Citations: https://chatgpt.com/

# Anything else that's relevant: 


import json
from cryptography.fernet import Fernet

class MovieDecryptor:
    """
    A class that handles decryption of an encrypted movie title for a given group using Fernet symmetric encryption.
    """
    def __init__(self, encrypted_file_path):
        """
        Initializes the MovieDecryptor with the path to the encrypted JSON file and sets up the Fernet object
        using the provided group key.

        Args: 
            encrypted_file_path (str): Path to the JSON file containing encrypted movie titles keyed by group name.
        """
        self.encrypted_file_path = encrypted_file_path
        # Fernet key used for decryption
        self.fernet_key = b"GusN5ceicQjGeKNr0gedUkjZ6h4I8xXm6Thx_issRko="
        # Fernet object handles the encryption/decryption logic
        self.fernet = Fernet(self.fernet_key)

    def decrypt_movie(self, group_name):
        """
        Decrypts the movie title associated with the given group name.

        Args:
            group_name (str): The name of the group to look up in the JSON file.

        Returns:
            str: The decrypted movie title if found and successfully decrypted;
                 otherwise, returns an error message.
        """
        # Load the encrypted movie titles from the JSON file
        with open(self.encrypted_file_path, 'r') as f:
            encrypted_data = json.load(f)
        
        # Retrieve the encrypted message for the group
        encrypted_message = encrypted_data.get(group_name, [None])[0]

        if encrypted_message:
            # Decode and decrypt the message using the Fernet key
            decrypted_bytes = self.fernet.decrypt(encrypted_message.encode())
            return decrypted_bytes.decode()
        else:
            return "No message found for group."
