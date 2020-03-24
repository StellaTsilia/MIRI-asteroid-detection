import astropy
from astropy.io import fits

import numpy as np
import math


hdul=fits.open("/home/stella/point_sources/sim1/det_images/mv_source_final.fits")  
data=hdul[0].data
vel=3 # velocity in pixels/frame 
theta=math.pi/6-math.pi # angle (rads) between source's direction and positive x-axis  

import function_collapse_source as fl 
fl.collapse_source(data,vel,theta)
