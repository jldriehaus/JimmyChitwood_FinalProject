# main.py
# Name: Connor Thomas
# Email: thoma5cg@mail.uc.edu
# Assignment Number: Group Final Project
# Due Date: 4/24/25
# Course #/Section: IS4010/002
# Semester/Year: 2nd/4th
# Brief description of the assignment: Decrypt text that shows a location and a movie title then take a picture there and have it display
# Brief description of what this module does: This module decrypts a location and movie title for a specific person and displays a related photo using local encrypted files.
# Citations: ChatGPT
# Anything else that's relevant:

import os
from decryptPackage.decrypt_location import LocationDecryptor
from decryptPackage.decrypt_movie import MovieDecryptor
from photoPackage.show_photo import PhotoDisplayer

if __name__ == "__main__":
    try:
        # Get absolute path to the folder containing this file
        base_path = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_path, "..", "data")

        print(f"Looking for files in: {data_path}")

        # Decrypt location
        encrypted_json_path = os.path.join(data_path, "EncryptedGroupHints Spring 2025.json")
        uce_path = os.path.join(data_path, "UCEnglish.txt")
        print(f"Encrypted JSON path: {encrypted_json_path}")
        print(f"UCEnglish path: {uce_path}")

        location_decryptor = LocationDecryptor(encrypted_json_path, uce_path)
        location = location_decryptor.get_location("Jimmy Chitwood")
        print(f"\nDecrypted Location: {location}")

        # Decrypt movie
        movie_json_path = os.path.join(data_path, "TeamsAndEncryptedMessagesForDistribution.json")
        movie_decryptor = MovieDecryptor(movie_json_path)
        decrypted_movie = movie_decryptor.decrypt_movie("Jimmy Chitwood")
        print(f"\nDecrypted Movie Title: {decrypted_movie}")

        # Display photo
        photo_path = os.path.join(data_path, "group_photo.jpg")
        print(f"\nLoading photo from: {photo_path}")
        photo_displayer = PhotoDisplayer(photo_path)
        photo_displayer.display_photo()

    except Exception as e:
        print(f"\nAn error occurred:\n{e}")

    input("\nPress Enter to exit...")


