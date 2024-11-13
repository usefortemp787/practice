from PIL import Image

def normalize_image(imgPath, opPath, newMin, newMax):
    original_image = Image.open(imgPath).convert("L")
    width, height = original_image.size

    min_pixel = 255
    max_pixel = 0
    pixels = original_image.load()

    for y in range(height):
        for x in range(width):
            pixel_value = pixels[x, y]
            if pixel_value < min_pixel:
                min_pixel = pixel_value
            if pixel_value > max_pixel:
                max_pixel = pixel_value

    print("Image minimum pixel value:", min_pixel)
    print("Image maximum pixel value:", max_pixel)

    for y in range(height):
        for x in range(width):
            origiPixel = pixels[x, y]
            normalizedPixel = int(((origiPixel - min_pixel) * (newMax - newMin)) / (max_pixel - min_pixel) + newMin)
            pixels[x, y] = normalizedPixel

    original_image.save(opPath)
    print(f"normalized image saved as '{opPath}'.")

newMin = int(input("enter the new_min (e.g., 0): "))
newMax = int(input("Enter the new_max (e.g., 255): "))

normalize_image("input_image.png", "normalized_image.png", newMin, newMax)
