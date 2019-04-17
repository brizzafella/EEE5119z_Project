#the modules we shall need
import numpy as np
import matplotlib.pyplot as plt
import math
import transmitter
import antenna
import reciever
import scipy as sy
import scipy.fftpack as syfp
import pylab as pyl



#create a transmitter and generate a pulsed waveform
c=2.998e8
transmitted_signal=transmitter.generator()
t = np.linspace(1, 100, 1000)

plt.subplot(3,1,1)
plt.plot(t, transmitted_signal)
plt.title('transmitted Signal')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
plt.show()
peak_power=transmitter.power
frequency=transmitter.frequency
wavelength=transmitter.wavelength_calc(frequency)
print("Peak Power:")
print(peak_power)
print("Operating Frequency:")
print(frequency)
print("Wavelength:")
print(wavelength)
#create an antenna and propagate the wave form
antenna_area=antenna.antena_area
antenna_gain=antenna.antenna_gain(antenna_area,wavelength)
#create targets and positions then give positions random velocities
target_position=np.array([100,100,100])
target_velocity=np.array([100,180,120])
range=100
mag = np.sqrt(target_velocity.dot(target_velocity))
maximum_velocity=50  # this is the maximum speed limit and now we want to calculate the maximum doppler shift allowed
print("Maximum speed in m/s:")
print(maximum_velocity)
doppler_shift_limit=2*maximum_velocity/wavelength
print("Doppler frequency corresponding to maximum speed limit:")
print(doppler_shift_limit)
w=2*math.pi*frequency
amplified_wave= antenna.propagate(transmitted_signal,w)# transmit the wave to the target
plt.subplot(3,1,1)
plt.plot(t, amplified_wave)
plt.title('transmitted Signal')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
plt.show()

time=t-2*range/c
reflected=np.cos(w*time)
plt.subplot(3,1,1)
plt.plot(t, reflected)
plt.title('Reflected Signal')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
plt.show()
#create the reflected wave from the targets

#recieve the wave in the reciever then perform signal procession techniques on it.
# Do FFT analysis of array
FFT = sy.fft(reflected)
dt=0.02
# Getting the related frequencies
freqs = syfp.fftfreq(len(reflected))
# Create subplot windows and show plot
plt.subplot(3,1,1)
plt.plot(t, freqs)
plt.title('Reflected Signal')
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
plt.show()
