# File Name : decrypt_location.py
# Student Name: Drew Wolfe
# email:  wolfeaw@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   4/24/2025
# Course #/Section:   IS4010-002
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Decrypt location and movie from a .txt file
# and display a photo

# Brief Description of what this module does: Decrypts the location our group
# had to take a picture for

# Citations: https://chatgpt.com/
# Anything else that's relevant: n/a

import json

class LocationDecryptor:
    def __init__(self, encrypted_file_path, wordlist_file_path):
        # Initialize with the paths to the encrypted JSON file and the wordlist text file
        self.encrypted_file_path = encrypted_file_path
        self.wordlist_file_path = wordlist_file_path
        self.wordlist = self._load_wordlist()  # Load wordlist upon initialization

    def _load_wordlist(self):
        # Read the wordlist file and store each line as a word in a list
        with open(self.wordlist_file_path, 'r') as file:
            return [line.strip() for line in file]

    def get_location(self, group_name):
        # Open and parse the encrypted JSON file
        with open(self.encrypted_file_path, 'r') as f:
            encrypted_data = json.load(f)

        # Get list of indices corresponding to the group name
        indices = encrypted_data.get(group_name, [])

        # Convert indices to words using the wordlist
        decrypted_words = [self.wordlist[int(index)] for index in indices]

        # Return the decrypted location as a space-separated string
        return ' '.join(decrypted_words)
