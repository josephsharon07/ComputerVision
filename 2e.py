import cv2

# Load an image (in grayscale)
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply thresholding
_, thresholded_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresholded_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
contour_img = cv2.drawContours(cv2.cvtColor(img, cv2.COLOR_GRAY2BGR), contours, -1, (0, 255, 0), 2)

# Display the image with contours
cv2.imshow('Contour Image', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
