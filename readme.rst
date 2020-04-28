This is code for my undergraduate research project.
The purpose of the research project is to determine heavy elemental abundances of stars found in the Halo Region of the
Milky Way Galaxy. The objective of the program is to have a more intuitive way of extracting data from a fits file and processing that data. Then format the data for MOOG to read the data.
The program, spectrum.py, when ran will prompt the user to input a path. The user must input a path to where the fits file is located. So for example on my computer I would input the following: "/home/slogle/Astro" (note: without the quotes). Then enter file's name; for example: "HD6268.fits" .

After this it will prompt the user to input a "r-value". This is for the box-car smoothing process. Depending on the "r-value" that is chosen, will affect how much the spectrum is smoothed. Then the data is run through a normalizing function to place the y-axis between 1 and 0. After this a graph will appear showing the raw spectral data and the new normalized/smoothed data.

Next the user will be prompted to name the file that will be formatted for MOOG. This would look like: "moog.txt" .
Then the user will be asked to input the name of the star.
Next the user will be asked how many data points they want to be written to all of the text files. The program will loop until the user gives an appropriate choice. If the user wants all the data they can simply type "All" or "all" .
Then the user will be asked to name the plain text file. This is just a general text file with a header that can be used for a more general purpose. For example this file can be called "data.txt" .

The program will always write a file called "raw_data.txt" that will always contain the orignal data extracted from the fits file.

Code written by: Luke Ogle
