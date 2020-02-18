import astropy
from astropy.io import fits                                 

import numpy as np

mx=50
my=20
nz=5
px0=mx/2
py0=my/2

px0=int(round(px0))
py0=int(round(py0))

vel=3

if px0+vel*nz>mx:
     print("Error: toy model's frame size should be bigger") 
     raise KeyboardInterrupt

toy=np.empty([nz,my,mx])

toy[0,py0,px0]=1

for k in range(1,nz):     
        toy[k,:,:]=toy[k-1,:,:]  
        toy[k,py0,px0+vel*k]=1          

mv_source_simple_vel=np.array(toy[:,:,:])
hdu=fits.PrimaryHDU(mv_source_simple_vel)
hdul=fits.HDUList([hdu])
hdul.writeto("mv_source_simple_vel.fits") 
