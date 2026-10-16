import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from funciones import *

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")
carpeta_assets = os.path.join(os.path.dirname(__file__), "..", "assets")

metodos_nombres = ["biseccion", "falsa_posicion", "punto_fijo", "secante", "newton", "newton_mejorado"]

# ---------- GRAFICO 1: cada funcion con su raiz marcada ----------
for i in range(6):
    datos = np.loadtxt(os.path.join(carpeta_data, "funcion_" + nombres[i] + ".csv"), delimiter=",", skiprows=1)
    x = datos[:, 0]
    y = datos[:, 1]

    plt.figure(figsize=(7, 4))
    plt.plot(x, y, label="f(x) = " + formulas[i])
    plt.axhline(0, color="black", linewidth=0.8)
    plt.plot(raices[i], 0, "ro", label="raiz = " + str(round(raices[i], 6)))

    if nombres[i] == "raiz_doble":
        plt.annotate("tangencia al eje x\n(raiz doble)", xy=(raices[i], 0), xytext=(1.5, 0.55),
                     arrowprops=dict(arrowstyle="->"))

    plt.title("Funcion " + str(i + 1) + ": " + nombres[i] + " con su raiz marcada")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(carpeta_assets, "funcion_" + nombres[i] + ".png"), dpi=120)
    plt.close()

print("Grafico 1 listo: funciones con su raiz")

# ---------- GRAFICO 2: |error| vs iteracion (escala log) por funcion ----------
for i in range(6):
    plt.figure(figsize=(7, 4))

    for metodo in metodos_nombres:
        ruta = os.path.join(carpeta_data, "pasos_" + metodo + "_" + nombres[i] + ".csv")
        if not os.path.exists(ruta):
            continue      # el metodo no aplica en esta funcion (no hay csv)

        datos = np.loadtxt(ruta, delimiter=",", skiprows=1, ndmin=2)
        iteracion = datos[:, 0] + 1
        error = datos[:, 2]
        error = np.maximum(error, 1e-17)    # los errores 0 no se pueden graficar en escala log

        plt.plot(iteracion, error, marker="o", markersize=3, label=metodo)

    plt.yscale("log")
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))    # solo iteraciones enteras en el eje x
    plt.title("Convergencia en " + nombres[i] + ": f(x) = " + formulas[i])
    plt.xlabel("Iteracion")
    plt.ylabel("|error| = |x_n - raiz|  (escala log)")
    plt.legend()
    plt.grid(True, which="both", alpha=0.4)
    plt.savefig(os.path.join(carpeta_assets, "convergencia_" + nombres[i] + ".png"), dpi=120)
    plt.close()

print("Grafico 2 listo: convergencia por funcion")

# ---------- GRAFICO 3: resumen de iteraciones por metodo y funcion ----------
archivo = open(os.path.join(carpeta_data, "resumen_convergencia.csv"))
lineas = archivo.readlines()
archivo.close()

# tabla[metodo][funcion] = (iteraciones, convergio)
tabla = {}
for metodo in metodos_nombres:
    tabla[metodo] = {}
for linea in lineas[1:]:
    partes = linea.strip().split(",")
    tabla[partes[0]][partes[1]] = (int(partes[2]), partes[5] == "True")

plt.figure(figsize=(12, 5))
ancho = 0.13
posiciones = np.arange(6)

for j in range(6):
    metodo = metodos_nombres[j]
    alturas = []
    for i in range(6):
        alturas.append(tabla[metodo][nombres[i]][0])

    barras = plt.bar(posiciones + j * ancho, alturas, ancho, label=metodo)

    # texto arriba de cada barra
    for i in range(6):
        iteraciones = tabla[metodo][nombres[i]][0]
        convergio = tabla[metodo][nombres[i]][1]
        if iteraciones == 0:
            texto = "no aplica"
        elif not convergio:
            texto = "no conv."
        else:
            texto = str(iteraciones)
        plt.text(posiciones[i] + j * ancho, iteraciones + 0.5, texto, ha="center", fontsize=7, rotation=90)

plt.xticks(posiciones + 2.5 * ancho, nombres)
plt.ylim(0, 115)
plt.title("Iteraciones por metodo y funcion (tol = 1e-6)")
plt.xlabel("Funcion")
plt.ylabel("Iteraciones")
plt.legend(ncol=3)
plt.grid(True, axis="y", alpha=0.4)
plt.savefig(os.path.join(carpeta_assets, "resumen_iteraciones.png"), dpi=120)
plt.close()

print("Grafico 3 listo: resumen de iteraciones")
print("Graficos guardados en src/assets/")