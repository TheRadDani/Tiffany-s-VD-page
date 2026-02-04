import os
from PIL import Image

# Folder containing images
input_folder = "./images"

# Target dimensions from CSS container
target_width = 400
target_height = 300

def resize_image(image_path):
    with Image.open(image_path) as img:
        # Preserve aspect ratio while fitting into target box
        img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)

        # Create a new background with target size
        background = Image.new("RGB", (target_width, target_height), (255, 255, 255))
        
        # Center the resized image on the background
        offset_x = (target_width - img.width) // 2
        offset_y = (target_height - img.height) // 2
        background.paste(img, (offset_x, offset_y))

        # Overwrite the original file
        background.save(image_path)

def main():
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            resize_image(input_path)
            print(f"Resized and overwritten: {filename}")

if __name__ == "__main__":
    main()
