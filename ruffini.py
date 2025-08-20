import numpy as np
import matplotlib.pyplot as plt

coeficientes = np.array([1, -4,5,12])
último = int(coeficientes[-1])

# Divisores positivos del último coeficiente
if último == 0:
	# 0 tiene infinitos divisores; representamos con array vacío o [0]
	x = np.array([0])
else:
	x = np.array([d for d in range(1, abs(último) + 1) if último % d == 0])

array = np.concatenate((-x, x))
print("Todos los divisores:", array)

def ruffini(coeficientes, divisores):
    """Devuelve los divisores (candidatos) que son raíces (remainder = 0).

    Implementación correcta de la división sintética (Ruffini) para evaluar
    p(d). Si el resto (último valor) es 0, d es raíz del polinomio.
    coeficientes: array de mayor a menor grado.
    divisores: candidatos a probar.
    """
    n = len(coeficientes)
    raices = []
    for d in divisores:
        # b almacenará los coeficientes resultantes de la división sintética
        b0 = coeficientes[0]
        b = [b0]
        # Recorremos desde el segundo coeficiente (i=1) hasta el final
        for i in range(1, n):
            b.append(coeficientes[i] + d * b[i-1])
        resto = b[-1]
        if resto == 0:
            raices.append(int(d))
    return raices

print('Posibles soluciones:', ruffini(coeficientes, array))

