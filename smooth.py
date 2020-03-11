import matplotlib.pyplot as plt
import math as m
import csv
import os
from astropy.io import fits
import numpy as np


# Define the path
path = "/home/slogle/Astro"

# Tell it where to look for the fits file
os.chdir(path)

# Give the file a name and define the path
fif = 'test1.fits'

# Extracting the data from the fits file
hdul = fits.open(fif)
hdul.info()
data = fits.getdata(fif)
header = fits.getheader(fif)


wavelength =np.array(data[0][0])
flux =np.array(data[0][1])


x1=[]
x1.extend(range(1,31))
x1=np.asarray(x1)

r=int(input("Please enter a r value: "))

alpha=(1.0)/(2.0*r+1.0)


new_flux=[]
new_wavelength=[]
j=r
k=r


while j<len(flux)-r:
  t=0
  t=sum(flux[(j-r):(j+r+1)])
  new_flux.append(alpha*t)
  j+=1

while k<len(wavelength)-r:
  t=0
  t=sum(wavelength[(k-r):(k+r+1)])
  new_wavelength.append(alpha*t)
  k+=1

new_wavelength=np.asarray(new_wavelength)
new_flux=np.asarray(new_flux)

plt.plot(new_wavelength,new_flux)
plt.show()
#print(len(new_wavelength))
#print(len(new_flux))
