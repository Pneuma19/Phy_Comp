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

import norm as nm
import smooth as sm
import readfits as rdf
import plot as pt

#Open and read the fits file
wavelength, flux = rdf.readfits()


x = wavelength
y = flux

#Normalizing
norm_flux = nm.norm(flux)




#Smoothing
smooth_wavelength, smooth_flux = sm.smooth(wavelength, norm_flux)


#Plotting the data
pt.plot(wavelength, flux, smooth_wavelength, smooth_flux)

#format(new_wavelength, '.10f')
#format(new_flux, '.10f')

#Writing to Text file
L=len(new_flux)
def form_e(q):
    a = '%E' % q
    return a.split('E')[0].rstrip('0').rstrip('0').rstrip('.')+'E'+a.split('E')[1]


with open('Luke2020', 'w') as f:
    f.write("HD6268 (Flux) (Lin           npts="+str(L) +"\n")
    for i in range(0, L):
        f.write("%6s" % ("")) 
        f.write("%8s" % (form_e(new_wavelength[i])))
        f.write("%20s" % (form_e(new_flux[i])))
        f.write("\n")


