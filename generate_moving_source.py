import astropy
from astropy.io import fits

hdul=fits.open("det_image_seq1_MIRIMAGE_F1280Wexp1.fits")
data=hdul[1].data                                  

import numpy as np
from numpy import empty

diff=empty([25,25,14])

for k in range (14): 
     temp=np.array(data[0,k+1,535:560,695:720]-data[0,k,535:560,695:720])    
     for j in range (25): 
         for i in range (25):  
              diff[i,j,k]=temp[i,j]
            

for f in range (1,15): 
     data[0,f,535:560,695:720]=data[0,f,619:644,699:724] 
     for n in range (14): 
         for m in range(25): 
          for l in range(25): 
               data[0,f,535+m,695+l+f]=diff[l,m,n]+data[0,f,581,699]

mv_source=np.array(data[:,:,:,:])
hdu=fits.PrimaryHDU(mv_source)
hdul=fits.HDUList([hdu])
hdul.writeto("mv_source.fits")

