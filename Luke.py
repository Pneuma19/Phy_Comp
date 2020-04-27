# Importing Modules
import norm as nm
import smooth as sm
import readfits as rdf
import plot as pt
import write_moog as wtm
import write as wt

#Open and read the fits file
wavelength, flux = rdf.readfits()

#Normalizing
norm_flux = nm.norm(flux)

#Smoothing
smooth_wavelength, smooth_flux = sm.smooth(wavelength, norm_flux)

#Plotting the data
pt.plot(wavelength, flux, smooth_wavelength, smooth_flux)

#Writing to Text file (For moog)
star_name, number_of_variables = wtm.write_moog(smooth_wavelength, smooth_flux)

#Writing to a plain text file (with header)
wt.write_txt(smooth_wavelength, smooth_flux, star_name, number_of_variables)
