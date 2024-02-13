import cv2
import wget

wget.download("https://images.unsplash.com/photo-1532103050105-860af53bc6aa?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=robert-v-ruggiero-gwI6TcYPEUA-unsplash.jpg&w=640", "image.jpg")

# Load an image
img = cv2.imread('image.jpg')

# Display the image
cv2.imshow('Image', img)

# Wait for any key to be pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()