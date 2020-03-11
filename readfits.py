# Importing Modules
import matplotlib.pyplot as plt
import csv
import os
from astropy.io import fits
from decimal import Decimal
import math as m
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


x = data[0][0]
y = data[0][1]

#Normalizing
Length_y=len(y)

y_max=max(y)
y_min=min(y)
norm_y=[]

for i in range(0,Length_y):
  norm_y.append((y[i]-y_min)/(y_max-y_min))

#plt.plot(x,norm_y)
#plt.show()



#Creating a Blackbody function
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(wav, T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity

# generate x-axis in increments from 1nm to 3 micrometer in 1 nm increments
# starting at 1 nm to avoid wav = 0, which would result in division by zero.
wavelengths = np.arange(1e-9, 3e-6, 1e-9) 

# intensity at 4000K, 5000K, 6000K, 7000K
intensity4000 = planck(wavelengths, 10000.)
#intensity5000 = planck(wavelengths, 5000.)
#intensity6000 = planck(wavelengths, 6000.)
#intensity7000 = planck(wavelengths, 7000.)


plt.plot(wavelengths*1e9, intensity4000, 'r-')
plt.plot(x,norm_y)

# show the plot
#plt.axis([2000, 3250, 0, 1])
plt.show()



'''
n = 3
L = 500


def form_e(q):
    a = '%E' % q
    return a.split('E')[0].rstrip('0').rstrip('0').rstrip('.')+'E'+a.split('E')[1]


with open('Luke2020', 'w') as f:
    f.write("HD6268 (Flux) (Lin           npts=500\n")
    for i in range(0, L):
        f.write("%6s" % ("")) 
        f.write("%8s" % (form_e(x[i])))
        f.write("%20s" % (form_e(y[i])))
        f.write("\n")
'''
