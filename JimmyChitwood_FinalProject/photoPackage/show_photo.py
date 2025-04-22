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

from PIL import Image

class PhotoDisplayer:
    def __init__(self, photo_path):
        self.photo_path = photo_path

    def display_photo(self):
        image = Image.open(self.photo_path)
        image.show()
