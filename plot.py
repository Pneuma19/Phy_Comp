import numpy as np
import matplotlib.pyplot as plt



def plot(wavelength, flux, smooth_wavelength, smooth_flux):
    
    plt.subplot(1,2,1)
    plt.plot(wavelength, flux, color = 'r', linewidth = 2.0)
    plt.title("Raw Wavelength vs Flux", size = 30)
    plt.xlabel("Wavelength (Ångstroms)", size = 30)
    plt.ylabel("Flux", size = 30)
    plt.xticks(size=20)
    plt.xticks(size=20)
    
    plt.subplot(1,2,2)
    plt.plot(smooth_wavelength, smooth_flux, color='r', linewidth=2.0)
    plt.title("Normalized/Smoothed Wavelength vs Flux", size=30)
    plt.xlabel("Wavelength (Ångstroms)", size = 30)
    plt.ylabel("Flux", size =30)
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    

    plt.show()

