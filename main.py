from PIL import Image
import os

def combine(image_paths,fileName):
    # Open images and get their dimensions
    images = [Image.open(img_path) for img_path in image_paths]
    widths, heights = zip(*(i.size for i in images))

    # Calculate the total width and maximum height
    total_width = sum(widths)
    max_height = max(heights)

    # Create a new blank image with the calculated dimensions
    new_image = Image.new('RGBA', (total_width, max_height))

    # Paste images side by side onto the new image
    x_offset = 0
    for img in images:
        new_image.paste(img, (x_offset, 0))
        x_offset += img.width

    # Save the final image
    new_image.save(f"./combined/{fileName} [{len(image_paths)} files {list(set(widths))[0]}x{list(set(heights))[0]} per image].png")

    # Optionally, you can display the image
    # new_image.show()



if(os.path.isdir("combined")):
    pass
else:
    os.mkdir("./combined")
    
# List of image file paths
for main in os.listdir("./images"):
    for sub in os.listdir(f"./images/{main}"):
        image_paths = []
        for file in os.listdir(f"./images/{main}/{sub}"):
            image_paths.append(f"./images/{main}/{sub}/{file}")    
        combine(image_paths,sub)

