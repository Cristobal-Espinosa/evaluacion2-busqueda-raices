import os
import numpy as np
from funciones import *
from metodos import secante

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

# estimaciones iniciales x0 y x1 de cada funcion
# (uso los extremos del intervalo; en la raiz doble x0 = 1.2 y x1 = 1.5)
x0s = [1, 1.2, 2, 0, 0, 0.1]
x1s = [2, 1.5, 3, 1, 1, 1]

print("METODO: SECANTE")
print("tol =", tol, " max_iter =", max_iter)
print()

resumen = []

for i in range(6):
    f = funciones[i]
    x0 = x0s[i]
    x1 = x1s[i]
    raiz_real = raices[i]

    raiz, pasos, convergio = secante(f, x0, x1, tol, max_iter)
    iteraciones = len(pasos)
    error = abs(raiz - raiz_real)

    print("Funcion", i + 1, ":", nombres[i], " f(x) =", formulas[i])
    print("x0 =", x0, " x1 =", x1)
    if convergio:
        print("Convergio: raiz =", raiz, " iteraciones =", iteraciones, " error =", error)
    else:
        print("NO convergio. Ultimo x =", raiz, " iteraciones =", iteraciones, " error =", error)
    print()

    # pasos de esta funcion: n, x, |x - raiz| (para el grafico de convergencia)
    filas = []
    for p in pasos:
        filas.append([p[0], p[2], abs(p[2] - raiz_real)])
    ruta = os.path.join(carpeta_data, "pasos_secante_" + nombres[i] + ".csv")
    np.savetxt(ruta, np.array(filas), delimiter=",", header="n,x,error", comments="")

    resumen.append([nombres[i], iteraciones, raiz, error, convergio])

# resumen del metodo
archivo = open(os.path.join(carpeta_data, "resumen_secante.csv"), "w")
archivo.write("funcion,iteraciones,raiz,error,convergio\n")
for r in resumen:
    archivo.write(r[0] + "," + str(r[1]) + "," + str(r[2]) + "," + str(r[3]) + "," + str(r[4]) + "\n")
archivo.close()

print("CSV guardados en src/data/")