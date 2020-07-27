# tsilia@mail.strw.leidenuniv.nl  
# 2020/07/27

import astropy
from astropy.io import fits

import numpy as np
import math

input2="/home/stella/point_sources/2006_QG93_40f/det_images/col_source_final_dqinitstep.fits" # path of the input file
output2="/home/stella/point_sources/2006_QG93_40f/det_images/col_source_pipeline.fits" # path of the output file

# open FITS file
hdul=fits.open(input2)
data=hdul[1].data
pixeldq=hdul[2].data

# apply mask 
nz=data.shape[1]-1	
mask=np.where(np.isnan(data[0,nz,:,:]),1,0)
hdul[2].data=np.where(pixeldq==0,mask,pixeldq)

# save data
hdul.writeto(output2)

