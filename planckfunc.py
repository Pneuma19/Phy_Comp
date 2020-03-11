import matplotlib.pyplot as plt
import math as m
import numpy as np



#Creating a Blackbody Function
h = 6.626e-34
c = 3.0e*8
k = 1.38e-23

def planck(wav,T):
    a=2.0*h*c**2
    b=h*c/(wav*k*T)
    intensity = a/( (wav**5) * (np.exp(b)-1.0))
    return intensity


