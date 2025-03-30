import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 0.25, 200)
y = x + np.exp(x,(3 * np.ones(200)))

fig, ax = plt.subplots()
ax.set_title('VIB3705-3 Load vs. Deflection')
ax.set_xlabel('Deflection (inches)')
ax.set_ylabel('Load (lbf)')
ax.plot(x, y)
plt.savefig("vib3705-3_load_v_deflection.svg")
plt.show()
