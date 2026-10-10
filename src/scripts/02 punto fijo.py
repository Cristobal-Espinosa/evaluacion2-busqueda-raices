import os
import numpy as np
from funciones import *
from metodos import punto_fijo

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

# para punto fijo hay que despejar x = g(x) de f(x) = 0
# elegi cada g para que |g'(x)| < 1 cerca de la raiz (condicion de convergencia)
def g1(x): return np.cbrt(x + 2)              # x^3 = x + 2
def g2(x): return (x**2 + 4) / 4              # (x-2)^2 = 0  ->  x = (x^2 + 4)/4
def g3(x): return 4 - np.log(x)               # ln(x) = 4 - x
def g4(x): return np.exp(-x)                  # x = e^(-x)
def g5(x): return np.cos(x)                   # x = cos(x)
def g6(x): return x - 0.8 * (np.sqrt(x) - np.cos(x))   # x = x - 0.8 f(x)

gs = [g1, g2, g3, g4, g5, g6]
formulas_g = ["(x+2)^(1/3)", "(x^2+4)/4", "4 - ln(x)", "e^(-x)", "cos(x)", "x - 0.8*(sqrt(x) - cos(x))"]

# valor inicial de cada funcion (la raiz doble parte en 1.2 como pide el enunciado)
x0s = [1.5, 1.2, 2.5, 0.5, 0.5, 0.5]

print("METODO: PUNTO FIJO")
print("tol =", tol, " max_iter =", max_iter)
print()

resumen = []

for i in range(6):
    g = gs[i]
    x0 = x0s[i]
    raiz_real = raices[i]

    raiz, pasos = punto_fijo(g, x0, tol, max_iter)
    iteraciones = len(pasos)
    convergio = pasos[-1][3] < tol
    error = abs(raiz - raiz_real)

    print("Funcion", i + 1, ":", nombres[i], " f(x) =", formulas[i])
    print("g(x) =", formulas_g[i], "  x0 =", x0)
    print("|g'(x)| aprox en la raiz:", abs((g(raiz_real + 1e-6) - g(raiz_real - 1e-6)) / 2e-6))
    if convergio:
        print("Convergio: raiz =", raiz, " iteraciones =", iteraciones, " error =", error)
    else:
        print("NO convergio en", max_iter, "iteraciones. Ultimo x =", raiz, " error =", error)
    print()

    # pasos de esta funcion: n, x, |x - raiz| (para el grafico de convergencia)
    filas = []
    for p in pasos:
        filas.append([p[0], p[2], abs(p[2] - raiz_real)])
    ruta = os.path.join(carpeta_data, "pasos_punto_fijo_" + nombres[i] + ".csv")
    np.savetxt(ruta, np.array(filas), delimiter=",", header="n,x,error", comments="")

    resumen.append([nombres[i], iteraciones, raiz, error, convergio])

# resumen del metodo
archivo = open(os.path.join(carpeta_data, "resumen_punto_fijo.csv"), "w")
archivo.write("funcion,iteraciones,raiz,error,convergio\n")
for r in resumen:
    archivo.write(r[0] + "," + str(r[1]) + "," + str(r[2]) + "," + str(r[3]) + "," + str(r[4]) + "\n")
archivo.close()

print("CSV guardados en src/data/")