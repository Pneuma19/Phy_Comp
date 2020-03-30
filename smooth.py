import matplotlib.pyplot as plt
import math as m
import csv
import os
from astropy.io import fits
import numpy as np


def smooth(wavelength, norm_flux):
  smooth_flux = []
  smooth_wavelength = []
  r = int(input("Please enter a r value: "))
  alpha = (1.0) / (2.0 * r + 1.0)
  j = r
  k = r

  while j < len(norm_flux) - r:
    dummy = 0
    dummy = sum(norm_flux[(j-r):(j+r+1)])
    smooth_flux.append(alpha * dummy)
    j += 1

  while k < len(wavelength) -r :
    dummy = 0
    dummy = sum(wavelength[(k-r):(k+r+1)])
    smooth_wavelength.append(alpha * dummy)
    k += 1

  smooth_wavelength = np.asarray(smooth_wavelength)
  smooth_flux = np.asarray(smooth_flux)
  return smooth_wavelength, smooth_flux

  

  
