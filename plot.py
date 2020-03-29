import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.io import fits
import planckfunc


path = "/home/slogle/Astro"
os.chdir(path)

fif = 'test1.fits'

hdul = fits.open(fif)
hdul.info()
data = fits.getdata(fif)


star_wavelength = np.array(data[0][0])
flux = np.array(data[0][1])

planck_wavelength = np.arange(1e-9, 3e-6, 1e-9)
intensity = []
Length_wavelength=len(star_wavelength)
#for i in range(0,Length_wavelength):
 #   dummy = planckfunc.planck(planck_wavelength[i],7000)
  #  intensity =  np.append(intensity, [[dummy]] )
intensity = planckfunc.planck(planck_wavelength,70000)

plt.plot(star_wavelength,flux)
plt.plot(planck_wavelength*1e9,intensity)
plt.show()
