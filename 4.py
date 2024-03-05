import cv2
import numpy as np

# Load an image
img = cv2.imread('image.jpg')

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized_img = cv2.equalizeHist(gray_img)

# Apply Gaussian blur
gaussian_img = cv2.GaussianBlur(equalized_img, (5, 5), 0)
median_img = cv2.medianBlur(equalized_img, 5)

# Apply Sobel edge detection
sobelx = cv2.Sobel(gaussian_img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gaussian_img, cv2.CV_64F, 0, 1, ksize=5)
edges = cv2.sqrt(cv2.addWeighted(cv2.pow(sobelx, 2), 1.0, cv2.pow(sobely, 2), 1.0, 0.0))


#Convolution
# Define a kernel
kernel = np.ones((3,3),np.float32)/9
# Apply convolution
convolved_image = cv2.filter2D(img, -1, kernel)


# Display the result
cv2.imshow('Original Image', img)
cv2.imshow('Equalized Image', equalized_img)
cv2.imshow('Gaussian Blurred Image', gaussian_img)
cv2.imshow('Median Blurred Image', median_img)
cv2.imshow('Convolved Image', convolved_image)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
