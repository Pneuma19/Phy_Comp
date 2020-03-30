from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import math as m
import numpy as np
from scipy.interpolate import UnivariateSpline
import csv
import os
from astropy.io import fits
from decimal import Decimal




def norm(flux):
  Length_flux = len(flux)
  flux_max = max(flux)
  flux_min = min(flux)
  norm_flux = []
  for i in range(0, Length_flux):
    norm_flux.append((flux[i] - flux_min) / (flux_max - flux_min))
  return norm_flux
