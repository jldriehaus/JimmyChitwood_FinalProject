# show_photo.py
# Madison Geier
# geierml@mail.uc.edu
# Final
# 04-24-25
# IS4010 002
# Spring 2025
# Brief Description of the assignment:  Final project scavenger hunt

# Brief Description of what this module does. Shows the picture we took from our location in the scavenger hunt
# Citations: chat gpt +

# Anything else that's relevant: n/a

from PIL import Image, ImageOps

class PhotoDisplayer:
    def __init__(self, image_path):
        self.image_path = image_path
        
    def display_photo(self):
        try:
            image = Image.open(self.image_path)

            # This automatically rotates based on EXIF data
            image = ImageOps.exif_transpose(image)

            image.show()
        except Exception as e:
            print(f"Error displaying photo: {e}")
