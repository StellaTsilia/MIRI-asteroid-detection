import astropy
from astropy.io import fits                                 

import numpy as np

mx=20
my=20
nz=5
px0=mx/2
py0=my/2

px0=int(round(px0))
py0=int(round(py0))

if px0+nz>mx
     print("Error: toy model's frame size should be bigger") 
     raise KeyboardInterrupt

toy=np.empty([nz,my,mx])

toy[0,py0,px0]=1

for k in range(1,nz):     
        toy[k,:,:]=toy[k-1,:,:]  
        toy[k,py0,px0+k]=1          

mv_source_simple=np.array(toy[:,:,:])
hdu=fits.PrimaryHDU(mv_source_simple)
hdul=fits.HDUList([hdu])
hdul.writeto("mv_source_simple.fits") 
