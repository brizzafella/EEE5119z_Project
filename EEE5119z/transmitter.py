import numpy as np

#constants
power=10e-3
frequency=10.525e9
c=2.998e8
period=9.5011876e-11
ppi=9.5011876e-11
dc=1 #because we have a continous wave
def generator():
	t = np.linspace(1, 100, 1000)
	x_volts = 10*np.sin(t/(2*np.pi))
	return x_volts 
def frequency_calc():
	return frequency
def wavelength_calc(frequenc):
	lamda=c/frequenc
	return lamda
def pulseduration(pulse_length):
	duration =2*pulselength/c
	return duration
def pulselength(duration):
	length=c*duration/2
	return length
def dutycycle(pulse_length,ppi):
	dc=pulse_length/ppi
	return dc
def poweraverage(power):
	pav=power*dc
	return pav
def prf(ipp):
	prf=1/ipp
	return prf
def IPP(PRF):
	ipp=1/PRF
	return ipp
	