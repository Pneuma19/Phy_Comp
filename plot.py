import numpy as np
import matplotlib.pyplot as plt



def plot(wavelength, flux, smooth_wavelength, smooth_flux):
    plt.subplot(1,2,1)
    plt.plot(wavelength, flux)
    plt.title("Raw Wavelength vs Flux")
    plt.xlabel("Wavelength (Ångstroms)")
    plt.ylabel("Flux")

    plt.subplot(1,2,2)
    plt.plot(smooth_wavelength, smooth_flux)
    plt.title("Normalized/Smoothed Wavelength vs Flux")
    plt.xlabel("Wavelength (Ångstroms)")
    plt.ylabel("Flux")

    plt.show()
