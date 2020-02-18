import astropy
from astropy.io import fits                                 

import numpy as np
import math

mx=100
my=100
nz=5
px0=mx/2
py0=my/2

px0=int(round(px0))
py0=int(round(py0))

vel=3
theta=math.pi/3 

velx=vel*math.cos(theta)
vely=vel*math.sin(theta)

velx=int(round(velx))
vely=int(round(vely))

if px0+velx*nz>mx or py0+vely*nz>my:
     print("Error: toy model's frame size should be bigger") 
     raise KeyboardInterrupt

toy=np.empty([nz,my,mx])

toy[0,py0,px0]=1

for k in range(1,nz):     
        toy[k,:,:]=toy[k-1,:,:]  
        toy[k,py0+vely*k,px0+velx*k]=1          

mv_source_simple_vel_dir=np.array(toy[:,:,:])
hdu=fits.PrimaryHDU(mv_source_simple_vel_dir)
hdul=fits.HDUList([hdu])
hdul.writeto("mv_source_simple_vel_dir.fits") 
