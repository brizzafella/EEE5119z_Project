import numpy as np
import math

antena_area=0.0025
antenna_efficiency=0.511
antenna_diameter=0.05
def antenna_gain(wavelength):
	gain=antenna_efficiency*(math.pi*antenna_diameter/wavelength)**2
	return gain
def antenna_area(diameter):
	area=math.pi*(diameter/2)**2
	return area
def min_signal_power(power,gain,lamda,crosssection,Rmax):
	Pmin=((power*gain**2)*lamda**2)*crosssection/(4*math.pi*Rmax**4)
	return Pmin
def propagate(sig,w):
	time = np.arange(0, 20, 0.2)
	#signal=sig*np.cos(w*time)
	t = np.linspace(1, 100, 1000)
	x_volts = np.cos(w*t)
	x_volts=sig*x_volts
	return x_volts