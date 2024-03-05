import cv2

# Load an image
image = cv2.imread('image.jpg')

# Get the dimensions of the image
height, width, channels = image.shape

# Iterate through each pixel
for y in range(height):
    for x in range(width):
        b, g, r = image[y, x]

        # Do something with the color values, for example, print them
        print(f"Pixel at ({x}, {y}) - Red: {r}, Green: {g}, Blue: {b}")

# Show the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
