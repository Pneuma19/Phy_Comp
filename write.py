from astropy.io import fits
from decimal import Decimal



def write(smooth_wavelength, smooth_flux):

  def form_e(q):
      a = '%E' % q
      return a.split('E')[0].rstrip('0').rstrip('0').rstrip('.')+'E'+a.split('E')[1]

  text_file = input("Please name the text file that the data will be written to: ")
  star_name = input("Please enter the name of the star (example: HD6268): ")
  number_of_variables = int(input("Please enter the number of variables you want to write to the text file: ")) 

  with open(text_file, 'w') as f:
      f.write(str(star_name) +" (Flux) (Lin          npts=" +str(number_of_variables)  +"\n")
      for i in range (0, number_of_variables):
          f.write("%6s" % (""))
          f.write("%8s" % (form_e(smooth_wavelength[i])))
          f.write("%20s" % (form_e(smooth_flux[i])))
          f.write("\n")
