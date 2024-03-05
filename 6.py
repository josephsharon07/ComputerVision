import numpy as np
import cv2
import matplotlib.pyplot as plt

def segment_image(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    # Create a mask
    mask = np.zeros(img.shape[:2],np.uint8)

    # Initialize background and foreground models
    bgd_model = np.zeros((1,65),np.float64)
    fgd_model = np.zeros((1,65),np.float64)

    # Define the rectangle for initial segmentation
    rect = (50,50,img.shape[1]-50,img.shape[0]-50)

    # Apply GrabCut algorithm
    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Create mask where sure and likely background are 0 and the rest is 1
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

    # Multiply input image with mask to get segmented image
    segmented_img = img*mask2[:,:,np.newaxis]

    return segmented_img

# Path to your input image
image_path = 'image.jpg'

# Perform segmentation
segmented_image = segment_image(image_path)

# Display the segmented image
plt.imshow( cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
