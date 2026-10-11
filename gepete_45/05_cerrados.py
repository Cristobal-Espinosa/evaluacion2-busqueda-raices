import os
import numpy as np
from funciones import *
from metodos import biseccion, falsa_posicion

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

metodos_nombres = ["biseccion", "falsa_posicion"]

for m in range(2):
    nombre_metodo = metodos_nombres[m]
    print("METODO:", nombre_metodo.upper())
    print("tol =", tol, " max_iter =", max_iter)
    print()

    resumen = []

    for i in range(6):
        f = funciones[i]
        a = intervalos[i][0]
        b = intervalos[i][1]
        raiz_real = raices[i]

        if m == 0:
            raiz, pasos, convergio = biseccion(f, a, b, tol, max_iter)
        else:
            raiz, pasos, convergio = falsa_posicion(f, a, b, tol, max_iter)

        print("Funcion", i + 1, ":", nombres[i], " f(x) =", formulas[i])
        print("Intervalo [a, b] = [", a, ",", b, "]")

        # si no hay cambio de signo el metodo no se puede aplicar
        if raiz is None:
            print("NO APLICA: f(a)*f(b) > 0, no hay cambio de signo en el intervalo")
            print()
            resumen.append([nombres[i], 0, "nan", "nan", False])
            continue

        iteraciones = len(pasos)
        error = abs(raiz - raiz_real)

        if convergio:
            print("Convergio: raiz =", raiz, " iteraciones =", iteraciones, " error =", error)
        else:
            print("NO convergio. Ultimo x =", raiz, " iteraciones =", iteraciones, " error =", error)
        print()

        # pasos de esta funcion: n, x, |x - raiz| (para el grafico de convergencia)
        filas = []
        for p in pasos:
            filas.append([p[0], p[2], abs(p[2] - raiz_real)])
        ruta = os.path.join(carpeta_data, "pasos_" + nombre_metodo + "_" + nombres[i] + ".csv")
        np.savetxt(ruta, np.array(filas), delimiter=",", header="n,x,error", comments="")

        resumen.append([nombres[i], iteraciones, raiz, error, convergio])

    # resumen del metodo
    archivo = open(os.path.join(carpeta_data, "resumen_" + nombre_metodo + ".csv"), "w")
    archivo.write("funcion,iteraciones,raiz,error,convergio\n")
    for r in resumen:
        archivo.write(r[0] + "," + str(r[1]) + "," + str(r[2]) + "," + str(r[3]) + "," + str(r[4]) + "\n")
    archivo.close()

    print("CSV guardados en src/data/")
    print()