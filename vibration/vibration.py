import math
import matplotlib.pyplot as plt
import numpy as np

# Acceptance Tensile Test

x = np.linspace(0, 0.20, 200)
y = 965 * (x + np.power(x,3))

fig, ax = plt.subplots()
ax.set_title('VIB3705-3 Load vs. Deflection')

ax.set_xlim(xmin = 0.0, xmax = 0.25)
ax.set_ylim(ymin = 0.0, ymax = 250)
ax.set_xlabel('Deflection (inches)')
ax.set_ylabel('Load (lbf)')

ax.plot(x, y)
ax.grid(True)
fig.savefig("vib3705-3_load_v_deflection.pdf")

# Acceptance Dynamic Test
# Tansmissibility vs. Frequency
zeta = 0.13

non_dim_frequency = np.linspace(0,2,200)
transmiss_num = 1 + ((2 * zeta * non_dim_frequency) ** 2)
transmiss_denom = (((1 - (non_dim_frequency ** 2)) ** 2)
    + ((2 * zeta * non_dim_frequency) ** 2))
transmissibility = np.sqrt(transmiss_num/transmiss_denom)

fig2, ax2 = plt.subplots()
ax2.set_title('VIB3705-3 Transmissibility vs. Non-dimensional Frequency')

ax2.set_xlim(xmin = 0.0, xmax = 2.0)
ax2.set_ylim(ymin = 0.0, ymax = 4.25)
ax2.set_xlabel('Non-dimensional Frequency')
ax2.set_ylabel('Transmissibility')

ax2.plot(non_dim_frequency, transmissibility)
ax2.grid(True)
fig2.savefig("vib3705-3_transmissibility_v_nondimensional_frequency.pdf")

# Phase Response vs. Frequency
ph_non_dim_freq_p1 = np.linspace(0.0,0.99,100)
ph_non_dim_freq_p2 = np.linspace(1.01,2.0,100)
phase_response_p1_sum1 = - np.atan(2 * zeta * ph_non_dim_freq_p1)
phase_response_p1_sum2 = np.atan((2 * zeta * ph_non_dim_freq_p1)/
(1 - (ph_non_dim_freq_p1 ** 2)))
phase_response_p1 = phase_response_p1_sum1 + phase_response_p1_sum2
phase_response_p2_sum1 = - np.atan(2 * zeta * ph_non_dim_freq_p2)
phase_response_p2_sum2 = np.atan((2 * zeta * ph_non_dim_freq_p2)/
(1 - (ph_non_dim_freq_p2 ** 2)))
phase_response_p2 = phase_response_p2_sum1 + phase_response_p2_sum2
+ ((phase_response_p1[-1] - phase_response_p2_sum1[0] -
phase_response_p2_sum2[0]) * np.ones(100))
ph_non_dim_freq = np.concatenate((ph_non_dim_freq_p1, ph_non_dim_freq_p2))
phase_response = np.concatenate((phase_response_p1, phase_response_p2))

fig3, ax3 = plt.subplots()
ax3.set_title('VIB3705-3 Phase vs. Frequency')

# ax.set_xlim(xmin = 0.0, xmax = 0.25)
# ax.set_ylim(ymin = 0.0, ymax = 250)
ax3.set_xlabel('Phase Angle')
ax3.set_ylabel('Frequency (Hz)')

ax3.plot(ph_non_dim_freq, phase_response)
ax3.grid(True)
fig3.savefig("vib3705-3_phase_v_frequency.pdf")
