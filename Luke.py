# Importing Modules
import norm as nm
import smooth as sm
import readfits as rdf
import plot as pt
import write as wt

#Open and read the fits file
wavelength, flux = rdf.readfits()

#Normalizing
norm_flux = nm.norm(flux)

#Smoothing
smooth_wavelength, smooth_flux = sm.smooth(wavelength, norm_flux)

#Plotting the data
pt.plot(wavelength, flux, smooth_wavelength, smooth_flux)

#Writing to Text file
wt.write(smooth_wavelength, smooth_flux)
