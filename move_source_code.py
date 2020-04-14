import astropy
from astropy.io import fits

import numpy as np
import math

import function_move_source as fl

flag_collapse_source=True # True if script is used to collapse a source
input1="/home/stella/point_sources/sim1/det_images/mv_source_final.fits" # path of the input file
output1="/home/stella/point_sources/sim1/det_images/col_source_final.fits" # path of the output file
vel=3 # velocity in pixels/frame 
theta=math.pi/6 # angle (rads) between source's direction and positive x-axis  


hdul=fits.open(input1)
if flag_collapse_source:
	data=hdul[0].data  
	theta=theta-math.pi
else:
	data=hdul[1].data

mv_source_final=fl.move_source(data,vel,theta)

hdu=fits.PrimaryHDU(mv_source_final)
hdul=fits.HDUList([hdu])
hdul.writeto(output1)
	

