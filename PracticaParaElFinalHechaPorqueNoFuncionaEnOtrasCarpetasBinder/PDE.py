import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x=np.linspace(0.0, np.pi/2.0, 1000)
y=np.cos(x)

plt.figure()
plt.plot(x, y, color="green")
plt.savefig("Prueba de Binder.pdf")

print("gracias Diosito lo logramos, funciona!!!!!:)")