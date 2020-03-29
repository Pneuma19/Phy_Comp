import matplotlib.pyplot as plt
import math as m
import numpy as np



#Creating a lackbody Function
h = 6.626*10**-34
c = 3.0*10**8
k = 1.38*10**-23

def planck(wav,T):
    a=2.0*h*c**2
    b=h*c/(wav*k*T)
    intensity = a/( (wav**5) * (np.exp(b)-1.0))
    return intensity


