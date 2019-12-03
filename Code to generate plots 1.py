import astropy
from astropy.io import fits

hdul=fits.open("det_image_seq1_MIRIMAGE_F1280Wexp1.fits")
hdul.info() 

data=hdul[1].data                                  #access SCI

import numpy as np

plot2d=np.array(data[0,14,535:560,695:720])        #source located in ds9
hdu=fits.PrimaryHDU(plot2d)                        #saved to a new file
hdul=fits.HDUList([hdu])
hdul.writeto("plot2d.fits")

plot1d=np.array(data[0,:,547,707])                 #one of the four brightest pixels
x_axis=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imgplot=plt.imshow(plot2d)
plt.imshow(plot2d,cmap="hot")
plt.colorbar()
plt.title("2D Plot of source's brightness")        #export plot
plt.savefig("plot2d.png")
plt.close()

plt.plot(x_axis,plot1d,'r')
plt.xlabel("frame number")
plt.ylabel("pixel value")
plt.title("Flux from 1 pixel of the source")       #export plot
plt.savefig("plot1d.png")

