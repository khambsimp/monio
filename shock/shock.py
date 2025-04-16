import math
import matplotlib.pyplot as plt
import numpy as np

# Qualification Shock Test
v = 10.0 # m/s
nat_freq = 100 # rad/s
zeta = 0.2 #
g = 1.0 # 1 G drop
damp_freq = nat_freq * math.sqrt(1 - (zeta ** 2))

x = np.linspace(0.0, 0.1, 200)
part2_num = (v*nat_freq*((2*(zeta**2)) - 1)) - (g*zeta)
part2_denum = math.sqrt(1 - (zeta ** 2))
part2 = (part2_num/part2_denum)*np.sin(damp_freq*x)
part1 = (g - (2*zeta*nat_freq*v))*np.cos(damp_freq*x)
y = (np.exp(-zeta*nat_freq*x))*(part1 + part2)

fig1, ax1 = plt.subplots()
ax1.set_title('VIB3705-3 Normalized Accel vs. Time Shock')
ax1.set_xlim(xmin = 0.0, xmax = 0.10)
ax1.set_ylim(ymin = -100.0, ymax = 100.0)
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Normalized Acceleration')
