from astropy.io import fits
from decimal import Decimal



def write_txt(smooth_wavelength, smooth_flux, star_name, number_of_variables, wavelength, flux):
  L = len(wavelength)
  def form_e(q):
      a = '%E' % q
      return a.split('E')[0].rstrip('0').rstrip('0').rstrip('.')+'E'+a.split('E')[1]

  text_file = input("Please name the text file that the data will be written to (for plain text file): ")
  
  

  with open(text_file, 'w') as f:
      f.write("#This is wavelength and flux data for the star: " +str(star_name) +"\n")
      f.write("        Wavelength          Flux \n")
      for i in range (0, number_of_variables):
          f.write("%6s" % (""))
          f.write("%8s" % (form_e(smooth_wavelength[i])))
          f.write("%20s" % (form_e(smooth_flux[i])))
          f.write("\n")


  with open('raw_data.txt', 'w') as f:
      f.write("#Raw data of wavelength and flux data for the star: " +str(star_name) +"\n")
      f.write("        Wavelength          Flux \n")
      for i in range (0, L):
          f.write("%6s" % (""))
          f.write("%8s" % (form_e(wavelength[i])))
          f.write("%20s" % (form_e(flux[i])))
          f.write("\n")
