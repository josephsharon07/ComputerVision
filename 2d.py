import cv2

# Load an image (in grayscale)
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply thresholding
_, thresholded_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Display the thresholded image
cv2.imshow('Thresholded Image', thresholded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
