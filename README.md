### Usage
Run run.py to use the program. 

By default, run.py will process images under the path "images/". This can be changed by changing the IMG_PATH in run.py. 

run.py takes two optional arguments, "--save/-s" and "--display/-d", which are both set to False by default. Setting --save to True will make the program save masks to the OUTPUT_PATH ("outputs/" by default) defined in run.py. Setting --display to True will make the program display each mask after it's done processing. 

Note that if the OUTPUT_PATH doesn't exist, nothing will be saved. 

### Libraries 
opencv-python
argparse
numpy
os

### How it works
My program first creates rough masks by picking out areas that best match the color of the barrels using HSV thresholding. Then, I use morphological closing to reduce the amount of noise in the masks.

### Improvements
Currently, the main issue with my solution is that there are too many false positive blobs in the masks. To deal with this, I plan to use contour detection to remove the blobs with relatively smaller areas in each mask.

