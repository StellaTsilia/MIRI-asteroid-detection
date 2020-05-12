import astropy
from astropy.io import fits

import numpy as np
import math


input2="/home/stella/point_sources/sim1/det_images/mv_source_final_dqinitstep.fits" # path of the input file
output2="/home/stella/point_sources/sim1/det_images/mv_source_pipeline.fits" # path of the output file


hdul=fits.open(input2)
data=hdul[1].data
pixeldq=hdul[2].data

nz=data.shape[1]-1	
mask=np.where(np.isnan(data[0,nz,:,:]),1,0)
hdul[2].data=np.where(pixeldq==0,mask,pixeldq)

hdul.writeto(output2)

