# Importing Modules
import matplotlib.pyplot as plt
import csv
import os
from astropy.io import fits
from decimal import Decimal
import math as m
import numpy as np


def readfits():
  path = input("Please define a path for the fits file: ")
  os.chdir(path)
  fif = input("Please enter the name of the fits file: ")
  hdul = fits.open(fif)
  hdul.info()
  data = fits.getdata(fif)
  header = fits.getheader(fif)

  wavelength = np.array(data[0][0])
  flux = np.array(data[0][1])

  return wavelength, flux
































 
