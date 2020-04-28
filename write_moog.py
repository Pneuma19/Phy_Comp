from astropy.io import fits
from decimal import Decimal



def write_moog(smooth_wavelength, smooth_flux):
  number_of_variables = 0
  L = len(smooth_wavelength)
  
  def form_e(q):
      a = '%E' % q
      return a.split('E')[0].rstrip('0').rstrip('0').rstrip('.')+'E'+a.split('E')[1]

  text_file = input("Please name the text file that the data will be written to (for MOOG): ")  
  star_name = input("Please enter the name of the star (example: HD6268): ")
  
  while number_of_variables <= 0 or number_of_variables > L:
    dummy  = input("Please enter the number of variables you want to write to the text files (for ALL the data points type 'All'): ")
    if dummy == 'All' or dummy == 'all':
      number_of_variables = int(L)
    elif int(dummy) < L and int(dummy) > 0:
      number_of_variables = int(dummy)
    else:
      number_of_variables = -1
      print("You have chosen an improper number. Please select a new number.\n")
    

  with open(text_file, 'w') as f:
      f.write(str(star_name) +" (Flux) (Lin          npts=" +str(number_of_variables)  +"\n")
      for i in range (0, number_of_variables):
          f.write("%6s" % (""))
          f.write("%8s" % (form_e(smooth_wavelength[i])))
          f.write("%20s" % (form_e(smooth_flux[i])))
          f.write("\n")
  return star_name, number_of_variables
