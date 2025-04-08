import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 0.20, 200)
y = 965 * (x + np.power(x,3))

fig, ax = plt.subplots()
ax.set_title('VIB3705-3 Load vs. Deflection')

ax.set_xlim(xmin = 0.0, xmax = 0.25)
ax.set_ylim(ymin = 0.0, ymax = 250)
ax.set_xlabel('Deflection (inches)')
ax.set_ylabel('Load (lbf)')

ax.plot(x, y)
plt.grid(True)
plt.savefig("vib3705-3_load_v_deflection.pdf")
plt.show()
