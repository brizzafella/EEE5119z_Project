import numpy as np
import math

c=2.998e8

def doppler_frequency(velocity,wavelength):
	fd=2*velocity/wavelength
	return fd
def doppler_frequency_max(PRF):
	fdmax=PRF/2
	return fdmax
def unambigious_range(PRF):
	rua=c/PRF
	return rua
def range(deltat):
	range=c*deltat/2
	return range
def intensity(power,gain,range):
	intensity=power*gain/(4*math.pi*range**2)
	return intensity
def received_power(power,gain,area,cross_section,range):
	r_power=(power*gain**2)*area*cross_section/(((4*math.pi)**3)*range**4)
	return r_power
def range_resolution(pulse_length):
	resolution=c*pulse_length
	return resolution