import os
import numpy as np
from funciones import *
from metodos import newton, newton_mejorado

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

# estimacion inicial de cada funcion (la raiz doble parte en 1.2 como pide el enunciado)
x0s = [1.5, 1.2, 2.5, 0.5, 0.5, 0.5]

metodos_nombres = ["newton", "newton_mejorado"]

for m in range(2):
    nombre_metodo = metodos_nombres[m]
    print("METODO:", nombre_metodo.upper())
    print("tol =", tol, " max_iter =", max_iter)
    print()

    resumen = []

    for i in range(6):
        f = funciones[i]
        df = derivadas[i]
        ddf = derivadas2[i]
        x0 = x0s[i]
        raiz_real = raices[i]

        if m == 0:
            raiz, pasos, convergio = newton(f, df, x0, tol, max_iter)
        else:
            raiz, pasos, convergio = newton_mejorado(f, df, ddf, x0, tol, max_iter)

        iteraciones = len(pasos)
        error = abs(raiz - raiz_real)

        print("Funcion", i + 1, ":", nombres[i], " f(x) =", formulas[i])
        print("x0 =", x0)
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