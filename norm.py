# Importing Modules
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import math as m
import numpy as np
from scipy.interpolate import UnivariateSpline
import csv
import os
from astropy.io import fits
from decimal import Decimal

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


x =np.array(data[0][0])
y =np.array(data[0][1])
Length_y=len(y)

y_max=max(y)
y_min=min(y)
norm_y=[]

for i in range(0,Length_y):
  norm_y.append((y[i]-y_min)/(y_max-y_min))

plt.plot(x,norm_y)
plt.show()






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
        f.write("%20s" % (form_e(norm_y[i])))
        f.write("\n")
