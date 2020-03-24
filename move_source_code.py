import astropy
from astropy.io import fits

import numpy as np
import math


hdul=fits.open("/home/stella/point_sources/sim1/det_images/det_image_seq1_MIRIMAGE_F1280Wexp1.fits")  
data=hdul[1].data
vel=3 # velocity in pixels/frame 
theta=math.pi/6 # angle (rads) between source's direction and positive x-axis  

import function_move_source as fl 
fl.move_source(data,vel,theta)

