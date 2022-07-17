import cv2
# import argparse
import matplotlib.pyplot as plt
import numpy as np
import os

IMG_PATH = "images/"

# arguments
# parser = argparse.ArgumentParser()
# parser.add_argument("-s", "--src", dest="src", 
#                     help="Specify a source image, otherwise use all images by default",
#                     default="ALL", type=str)


def load_images(path):
    '''Load all images from the given path and return an array'''
    images = []
    for file in os.listdir(path):
        img = cv2.imread(os.path.join(path, file))
        images.append(img)
    return images

images = load_images(IMG_PATH)

kernel = np.ones((5,5), np.uint8)

for image in images:
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(hsv_image, (0, 140, 70), (5, 255, 255))
    mask2 = cv2.inRange(hsv_image, (170, 140, 70), (180, 255, 255))
    mask = mask1 + mask2

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


    cv2.imshow("orange", mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


