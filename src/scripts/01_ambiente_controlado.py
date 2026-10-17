import os
import numpy as np

# carpeta donde se guardan los csv
carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

from funciones import *

print("Tolerancia:", tol)
print("Maximo de iteraciones:", max_iter)
print()

# ---------- demostrar que hay raiz en el rango (Bolzano) y generar csv ----------
for i in range(6):
    f = funciones[i]
    df = derivadas[i]
    a = intervalos[i][0]
    b = intervalos[i][1]

    print("Funcion", i + 1, ":", nombres[i], " f(x) =", formulas[i])
    print("Intervalo [a, b] = [", a, ",", b, "]")
    print("f(a) =", f(a), " f(b) =", f(b))
    print("f(a)*f(b) =", f(a) * f(b))

    if nombres[i] == "raiz_doble":
        print("No hay cambio de signo (f(a)*f(b) > 0), Bolzano no se puede usar")
        print("Pero en x = 2: f(2) =", f(2.0), " f'(2) =", df(2.0), "-> la curva toca el eje x (raiz doble)")
    else:
        if f(a) * f(b) < 0:
            print("Hay cambio de signo, por Bolzano existe una raiz en [a, b]")
        else:
            print("OJO: no hay cambio de signo en este intervalo")
    print("Estimacion inicial (abiertos): x0 =", x0_abiertos[i])
    print("Secante: x0 =", x0_secante[i], " x1 =", x1_secante[i])
    print("Punto fijo: g(x) =", formulas_g[i])
    print()

    # csv con columnas (x, f(x))
    x = np.linspace(a, b, 200)
    y = f(x)
    datos = np.column_stack((x, y))
    ruta = os.path.join(carpeta_data, "funcion_" + nombres[i] + ".csv")
    np.savetxt(ruta, datos, delimiter=",", header="x,f(x)", comments="")

print("CSV guardados en src/data/")