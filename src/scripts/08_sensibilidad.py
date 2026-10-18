import os
import numpy as np
from funciones import *
from metodos import *

np.seterr(all="ignore")   # para que no avise cuando un metodo se sale del dominio (log o raiz de negativos)

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

# distintos valores iniciales x0 para cada funcion (metodos abiertos)
x0s = [[0.5, 1, 1.5, 2, 3],
       [0.5, 1.2, 1.9, 3, 5],
       [0.5, 1, 2.5, 4, 8],
       [-2, 0, 0.5, 1, 5],
       [-2, 0, 0.5, 1, 3],
       [0.01, 0.1, 0.5, 1, 3]]

# distintos intervalos [a, b] para cada funcion (metodos cerrados)
# el ultimo de cada lista no tiene cambio de signo
intervalos2 = [[(1, 2), (0, 4), (1.5, 1.6), (2, 3)],
               [],
               [(2, 3), (1, 10), (2.9, 2.95), (3, 5)],
               [(0, 1), (-2, 5), (0.5, 0.6), (1, 2)],
               [(0, 1), (-1, 3), (0.7, 0.75), (1, 2)],
               [(0.1, 1), (0, 4), (0.64, 0.65), (1, 2)]]

# ---------- metodos abiertos: distintos x0 ----------
print("METODOS ABIERTOS: iteraciones segun x0 (la secante usa x1 = x0 + 0.5)")
print()
archivo = open(os.path.join(carpeta_data, "sensibilidad_abiertos.csv"), "w")
archivo.write("funcion,x0,punto_fijo,newton,newton_mejorado,secante\n")

for i in range(6):
    print("Funcion", i + 1, ":", nombres[i])
    for x0 in x0s[i]:
        x0 = np.float64(x0)
        textos = []

        raiz, pasos = punto_fijo(gs[i], x0, tol, max_iter)
        if len(pasos) > 0 and pasos[-1][3] < tol:
            textos.append(str(len(pasos)))
        else:
            textos.append("no converge")

        raiz, pasos, convergio = newton(funciones[i], derivadas[i], x0, tol, max_iter)
        if convergio:
            textos.append(str(len(pasos)))
        else:
            textos.append("no converge")

        raiz, pasos, convergio = newton_mejorado(funciones[i], derivadas[i], derivadas2[i], x0, tol, max_iter)
        if convergio:
            textos.append(str(len(pasos)))
        else:
            textos.append("no converge")

        raiz, pasos, convergio = secante(funciones[i], x0, x0 + 0.5, tol, max_iter)
        if convergio:
            textos.append(str(len(pasos)))
        else:
            textos.append("no converge")

        print("x0 =", float(x0), "| punto fijo:", textos[0], "| newton:", textos[1], "| newton mejorado:", textos[2], "| secante:", textos[3])
        archivo.write(nombres[i] + "," + str(float(x0)) + "," + textos[0] + "," + textos[1] + "," + textos[2] + "," + textos[3] + "\n")
    print()
archivo.close()

# ---------- metodos cerrados: distintos intervalos ----------
print("METODOS CERRADOS: iteraciones segun el intervalo")
print()
archivo = open(os.path.join(carpeta_data, "sensibilidad_cerrados.csv"), "w")
archivo.write("funcion,a,b,biseccion,falsa_posicion\n")

for i in range(6):
    if len(intervalos2[i]) == 0:
        continue      # la raiz doble no tiene intervalo con cambio de signo
    print("Funcion", i + 1, ":", nombres[i])
    for par in intervalos2[i]:
        a = np.float64(par[0])
        b = np.float64(par[1])
        textos = []

        raiz, pasos, convergio = biseccion(funciones[i], a, b, tol, max_iter)
        if raiz is None:
            textos.append("no aplica")
        else:
            textos.append(str(len(pasos)))

        raiz, pasos, convergio = falsa_posicion(funciones[i], a, b, tol, max_iter)
        if raiz is None:
            textos.append("no aplica")
        else:
            textos.append(str(len(pasos)))

        print("[", float(a), ",", float(b), "] | biseccion:", textos[0], "| falsa posicion:", textos[1])
        archivo.write(nombres[i] + "," + str(float(a)) + "," + str(float(b)) + "," + textos[0] + "," + textos[1] + "\n")
    print()
archivo.close()

print("CSV guardados en src/data/")

# ---------- punto fijo en la raiz doble: dos g distintas ----------
print()
print("PUNTO FIJO EN LA RAIZ DOBLE (x0 = 1.2)")
print()

def g_original(x): return (x**2 + 4) / 4    # tiene |g'(2)| = 1

casos = [["(x^2+4)/4", g_original, 100],
         ["(x^2+4)/4", g_original, 5000],
         ["(x+2)/2", gs[1], 100]]

archivo = open(os.path.join(carpeta_data, "sensibilidad_punto_fijo_raiz_doble.csv"), "w")
archivo.write("g,max_iter,iteraciones,convergio,error_real\n")
for caso in casos:
    raiz, pasos = punto_fijo(caso[1], np.float64(1.2), tol, caso[2])
    convergio = pasos[-1][3] < tol
    error_real = abs(raiz - 2.0)
    print("g(x) =", caso[0], "| max_iter =", caso[2], "| iteraciones =", len(pasos), "| convergio =", convergio, "| error real =", error_real)
    archivo.write(caso[0] + "," + str(caso[2]) + "," + str(len(pasos)) + "," + str(convergio) + "," + str(error_real) + "\n")
archivo.close()
print()
print("CSV guardado en src/data/sensibilidad_punto_fijo_raiz_doble.csv")
