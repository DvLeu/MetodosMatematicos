""""
crecimiento poblacional de una población en función del tiempo.
Utilizando : bibliotecas NumPy, SciPy y Matplotlib
Utilizando la ecuacion sin resolver.
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def crecimientoPoblacional(t, x, k, xm):
    dxdt = k * x * (1 - x / xm)
    return dxdt

k = 1
xm = 25
tiempo = (0, 7)
xcero = [10, 25, 50]

plt.figure(figsize=(8, 6))

for i in xcero:
    sol = solve_ivp(crecimientoPoblacional, tiempo, [i], args=(k, xm), t_eval=np.linspace(0, 7, 100))
    plt.plot(sol.t, sol.y[0], label=f'x0 = {i},  k={k}')
    poblacion_final = sol.y[0][-1]
    # Para imprimir las iteraciones.
    print(f'Población final para x0={i}, k={k}: {poblacion_final}')

plt.title('UNADM Crecimiento poblacional ')
plt.xlabel('T')
plt.ylabel('Poblacion')
plt.legend()
plt.grid(True)
plt.show()
