### Usage
Run "run.py" to use the program.

run.py takes two optional arguments, "--save/-s" and "--display/-d", which are both set to False by default. Setting --save to True will make the program save masks to the OUTPUT_PATH defined in run.py. Setting --display to True will make the program display each mask after it's done processing. 

### Libraries 
opencv-python
argparse
numpy
os

### How it works
My program first creates rough masks by picking out areas that best match the color of the barrels using HSV thresholding. Then, I use morphological closing to reduce the amount of noise in the masks.

### Improvements
Currently, the main issue with my solution is that there are too many false positive blobs in the masks. To deal with this, I plan to use contour detection to remove the blobs with relatively smaller areas in each mask.

