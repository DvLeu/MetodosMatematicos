""""
crecimiento poblacional de una población en función del tiempo.
Utilizando : bibliotecas NumPy, SciPy y Matplotlib
Utilizando la ecuacion resuelta .

"""
import math
import matplotlib.pyplot as plt

def crecimientoPoblacional(t, k, xm, x0):
    ecuacion = xm / (1 + (xm / x0 - 1) * math.exp(-k * t))
    return ecuacion
k = 1
xm = 25
valoresx0 = [10, 25, 50]
tiempos = [t for t in range(7)]
poblaciones = []
for x0 in valoresx0:
    poblacion = [crecimientoPoblacional(t, k, xm, x0) for t in tiempos]
    poblaciones.append(poblacion)

for i, x0 in enumerate(valoresx0):
    plt.plot(tiempos, poblaciones[i], label=f'x0={x0}, k={k}')

plt.xlabel('Tiempo (t)')
plt.ylabel('Población')
plt.title('Modelo de Crecimiento Poblacional')
plt.legend()
plt.grid(True)
plt.show()
#Para imprimir las iteraciones.
for i, x0 in enumerate(valoresx0):
    for t, poblacion in zip(tiempos, poblaciones[i]):
        print(f'Población para x0={x0}, k={k}, t={t+1}: {poblacion}')