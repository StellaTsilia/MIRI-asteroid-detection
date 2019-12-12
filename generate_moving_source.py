import astropy
from astropy.io import fits

hdul=fits.open("det_image_seq1_MIRIMAGE_F1280Wexp1.fits")
data=hdul[1].data                                  

import numpy as np

nx = 25 # number of POI pixels along x axis
ny = 25 # number of POI pixels along y axis
nz = 14 # number of frames within the ramp - 1
### nz could be set from data.shape instead of hardwiring it!
### not sure if I'm confusing x and y here, to be checked
x0 = 695 # x coordinate of first pixel in POI
y0 = 535 # y coordinate of first picel in POI

diff=np.empty([ny,nx,ny])

for k in range (nz):
     diff[:,:,k] = data[0,k+1,y0:y0+ny,x0:x0+nx] - data[0,k,y0:y0+ny,x0:x0+nx]
            

for f in range (1,nz+1):
     ### Why is this???
     data[0,f,535:560,695:720]=data[0,f,619:644,699:724] 
     for n in range (nz): 
         for m in range(ny): 
          for l in range(nx): 
               data[0,f,y0+m,x0+l+f]=diff[l,m,n]+data[0,f,581,699]

mv_source=np.array(data[:,:,:,:])
hdu=fits.PrimaryHDU(mv_source)
hdul=fits.HDUList([hdu])
hdul.writeto("mv_source.fits")

