import astropy
from astropy.io import fits

import numpy as np
import math
from scipy import interpolate

#If on a different path use the following:
#import sys  
#sys.path.append('/home/stella/point_sources/sim1/det_images')

def get_data():
	hdul=fits.open("/home/stella/point_sources/sim1/det_images/det_image_seq1_MIRIMAGE_F1280Wexp1.fits")  
	data=hdul[1].data
	vel=3 # velocity in pixels/frame  
	theta=3*math.pi/2 # angle (rads) between source's direction and positive x-axis  
	return data,vel,theta





