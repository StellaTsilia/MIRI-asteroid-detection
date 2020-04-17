import astropy
from astropy.io import fits

import numpy as np
import math

import function_move_source as fl

flag_collapse_source=False # True if script is used to collapse a source
input1="/home/stella/point_sources/sim1/det_images/det_image_seq1_MIRIMAGE_F1280Wexp1.fits" # path of the input file
output1="/home/stella/point_sources/sim1/det_images/mv_source_final.fits" # path of the output file
vel=3 # velocity in pixels/frame 
theta=math.pi/6 # angle (rads) between source's direction and positive x-axis  


hdul=fits.open(input1)
hdr=hdul[0].header
data=hdul[1].data

if flag_collapse_source: 
	theta=theta-math.pi

mv_source_final=fl.move_source(data,vel,theta)

primary_hdu=fits.PrimaryHDU(header=hdr)
image_hdu=fits.ImageHDU(mv_source_final)
hdul=fits.HDUList([primary_hdu,image_hdu])
hdul.writeto(output1)
	

