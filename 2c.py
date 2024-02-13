import cv2

# Load an image
img = cv2.imread('image.jpg')

# Resize the image
resized_img = cv2.resize(img, (300, 200))

# Display the resized image
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
