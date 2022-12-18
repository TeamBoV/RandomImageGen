import random
from PIL import Image
import sys

# Check if the user has provided the desired resolution as a command line argument
if len(sys.argv) < 3:
    print("Please provide the desired width and height as command line arguments.")
    sys.exit()

# Get the desired width and height from the command line arguments
width = int(sys.argv[1])
height = int(sys.argv[2])

# Create a new image with the specified width and height
image = Image.new("RGB", (width, height))

# Generate a random color for each pixel in the image
for x in range(width):
    for y in range(height):
        image.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# Save the image to a file in PNG format
image.save("random_image.png")
