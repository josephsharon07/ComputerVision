import cv2

# Load an image
img = cv2.imread('image.jpg')

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set up the detector with default parameters
detector = cv2.SimpleBlobDetector_create()

# Detect blobs
keypoints = detector.detect(gray_img)

# Draw detected blobs as red circles
blob_img = cv2.drawKeypoints(img, keypoints, None, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the image with blobs
cv2.imshow('Blob Image', blob_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
