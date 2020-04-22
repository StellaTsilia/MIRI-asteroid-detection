import astropy
from astropy.io import fits

import numpy as np
import math

import function_move_source as fl

flag_move_source=True # True if script is used to move a source
input1="/home/stella/point_sources/sim1/det_images/det_image_seq1_MIRIMAGE_F1280Wexp1.fits" # path of the input file
output1="/home/stella/point_sources/sim1/det_images/mv_source_final.fits" # path of the output file
vel=3 # velocity in pixels/frame 
theta=math.pi/6-math.pi # angle (rads) between source's direction and positive x-axis  


hdul=fits.open(input1)
data=hdul[1].data
pixeldq=hdul[2].data

if flag_move_source: 
	theta=theta+math.pi

mv_source_final=fl.move_source(data,vel,theta)

hdul[1].data=mv_source_final

nz=mv_source_final.shape[1]-1	
mask=np.where(np.isnan(mv_source_final[0,nz,:,:]),1,0)
hdul[2].data=np.where(pixeldq==0,mask,pixeldq)

hdul.writeto(output1)

