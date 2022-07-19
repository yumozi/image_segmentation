import cv2
import argparse
import numpy as np
import os

IMG_PATH = "images/"
OUTPUT_PATH = "outputs/"
KERNEL = np.ones((3,3), np.uint8)

def load_images(path):
    '''Return an array of tuples with all the images in the given path and their filename'''
    images = []
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path, filename))
        images.append((img, filename))
    return images

if __name__=='__main__':

    # Argument Parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--save", dest="save", 
                        help="Set this to True if you want the output masks to be saved.",
                        default=False, type=bool)
    parser.add_argument("-d", "--display", dest="display", 
                        help="Set this to True if you want each mask to be displayed after creating it",
                        default=False, type=bool)
    args = parser.parse_args()

    images = load_images(IMG_PATH)

    for image, filename in images:

        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Create a mask that looks for red at the beginning of the hue spectrum
        mask1 = cv2.inRange(hsv_image, (0, 160, 80), (1, 255, 255))

        # Create a mask that looks for red at the end of the hue spectrum
        mask2 = cv2.inRange(hsv_image, (175, 160, 80), (180, 255, 255))

        # Combine two masks 
        mask = mask1 + mask2

        # Use Closing to remove noise from mask 
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, KERNEL)

        # If the mask needs to be saved
        if args.save:
            cv2.imwrite(os.path.join(OUTPUT_PATH, filename), mask)

        # If the mask needs to be displayed
        if args.display:
            cv2.imshow("mask", mask)
            cv2.waitKey()
            cv2.destroyAllWindows()


