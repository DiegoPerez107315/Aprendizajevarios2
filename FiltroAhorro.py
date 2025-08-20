import numpy as np
import matplotlib.pyplot as plt

bolsa = np.linspace(0,720,12)
filtro = np.array([169,169,169,169,169,169,169,169,239,239,239,239])

plt.plot(bolsa, label='Bolsa de Ahorro')
plt.plot(filtro, label='Filtro de Ahorro')
plt.xlabel('Meses')
plt.ylabel('Cantidad')
plt.title('Comparativa de Ahorro')
plt.legend()
plt.show()