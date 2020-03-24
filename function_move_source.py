import astropy
from astropy.io import fits

import numpy as np
import math

from scipy.ndimage.interpolation import shift


def move_source(data,vel,theta):

	nz=data.shape[1]-1 # number of frames within the ramp - 1
	ny=data.shape[2] # number of pixels along y axis (1024 by default)
	nx=data.shape[3] # number of pixels along x axis (1032 by default)
	exp=data.shape[0] # number of exposures 
	
	velx=vel*math.cos(theta)
	vely=vel*math.sin(theta)
	
	
	diff=np.empty([exp,nz,ny,nx])
	
	for w in range(exp):
		for k in range(nz): 
			diff[w,k,:,:]=data[w,k+1,:,:]-data[w,k,:,:] 
	
	for w in range(exp):
		for k in range(nz):
			diff[w,k,:,:]=shift(diff[w,k,:,:], (vely*(k+1),velx*(k+1)), order=3, mode='constant', cval=0.0, prefilter=True)
	
	
	toy=np.empty([exp,nz+1,ny,nx])   
	
	for w in range(exp):
		toy[w,0,:,:]=data[w,0,:,:] 

	for w in range(exp):    
		for k in range(1,nz+1): 
			toy[w,k,:,:]=toy[w,k-1,:,:]+diff[w,k-1,:,:]
			  
	
	mv_source_final=np.array(toy[:,:,:])
	hdu=fits.PrimaryHDU(mv_source_final)
	hdul=fits.HDUList([hdu])
	hdul.writeto("/home/stella/point_sources/sim1/det_images/mv_source_final.fits")
	

