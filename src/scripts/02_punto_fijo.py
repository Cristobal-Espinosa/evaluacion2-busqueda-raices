import os
import numpy as np
from funciones import *
from metodos import punto_fijo

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

# las g(x) y los valores iniciales estan en funciones.py

print("METODO: PUNTO FIJO")
print("tol =", tol, " max_iter =", max_iter)
print()

resumen = []

for i in range(6):
    g = gs[i]
    x0 = x0_abiertos[i]
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
        filas.append([p[0], p[2], abs(p[2] - raiz_real), p[3]])
    ruta = os.path.join(carpeta_data, "pasos_punto_fijo_" + nombres[i] + ".csv")
    np.savetxt(ruta, np.array(filas), delimiter=",", header="n,x,error,dif", comments="")

    resumen.append([nombres[i], iteraciones, raiz, error, convergio])

# resumen del metodo
archivo = open(os.path.join(carpeta_data, "resumen_punto_fijo.csv"), "w")
archivo.write("funcion,iteraciones,raiz,error,convergio\n")
for r in resumen:
    archivo.write(r[0] + "," + str(r[1]) + "," + str(r[2]) + "," + str(r[3]) + "," + str(r[4]) + "\n")
archivo.close()

print("CSV guardados en src/data/")