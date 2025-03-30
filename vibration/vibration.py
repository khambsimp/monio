import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 0.25, 200)
y = x + np.exp(x,3)

fig, ax = plt.subplots()
ax.set_title('VIB3705-3 Load vs. Deflection')
ax.xlabel('Deflection (inches)')
ax.ylabel('Load (lbf)')
ax.plot(x, y)
plt.savefig("vib3705-3_load_v_deflection.svg")
plt.show()
