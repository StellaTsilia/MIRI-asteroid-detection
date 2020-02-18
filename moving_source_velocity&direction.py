import astropy
from astropy.io import fits

hdul=fits.open("det_image_seq1_MIRIMAGE_F1280Wexp1.fits")
data=hdul[1].data                                  

import numpy as np
import math

nx=25 # number of POI pixels along x axis
ny=25 # number of POI pixels along y axis
nz=data.shape[1]-1 # number of frames within the ramp - 1
x0=695 # x coordinate (using zero indexing) of first pixel in POI
y0=535 # y coordinate (using zero indexing) of first picel in POI

mx=500 # number of pixels in toy model's frame along x axis
my=500 # number of pixels in toy model's frame along y axis
px0=(mx-nx)/2 # x coordinate (using zero indexing) of POI's first pixel within toy model frame  
py0=(my-ny)/2 # y coordinate (using zero indexing) of POI's first pixel within toy model frame  

px0=int(round(px0))
py0=int(round(py0))

vel=3 # velocity in pixels/frame
theta=3*math.pi/2 # angle (rads) between source's direction and positive x-axis 

velx=vel*math.cos(theta)
vely=vel*math.sin(theta)

velx=int(round(velx))
vely=int(round(vely))

if px0+nx+velx*nz>mx or py0+ny+vely*nz>my: 
     print("Error: toy model's frame size should be bigger") 
     raise KeyboardInterrupt 

diff=np.empty([nx,ny,nz])

for k in range(nz): 
     diff[:,:,k]=data[0,k+1,y0:y0+ny,x0:x0+nx]-data[0,k,y0:y0+ny,x0:x0+nx] 
          
toy=np.empty([nz,my,mx])

for i in range(ny):   
    for j in range(nx): 
             toy[0,py0+i,px0+j]=data[0,0,y0+i,x0+j] 
    
for k in range(1,nz): 
     toy[k,:,:]=toy[k-1,:,:] 
     for n in range (nz): 
        for m in range(ny): 
           for l in range(nx): 
              toy[k,py0+m+vely*k,px0+l+velx*k]=toy[k,py0+m+vely*k,px0+l+velx*k]+diff[l,m,n]          

mv_source3=np.array(toy[:,:,:])
hdu=fits.PrimaryHDU(mv_source3)
hdul=fits.HDUList([hdu])
hdul.writeto("mv_source3.fits")
