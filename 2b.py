import cv2

# Load an image
img = cv2.imread('image.jpg')

# Define the region of interest (ROI)
x, y, w, h = 100, 100, 200, 200
cropped_img = img[y:y+h, x:x+w]

# Display the cropped image
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
