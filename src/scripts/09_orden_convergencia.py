import os
import numpy as np
from funciones import *

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

metodos_nombres = ["biseccion", "falsa_posicion", "punto_fijo", "secante", "newton", "newton_mejorado"]

# orden de convergencia estimado con los errores de cada paso:
# p = ln(e_(n+1) / e_n) / ln(e_n / e_(n-1))
# se usan solo errores mayores a 1e-13 (mas chicos son ruido de redondeo)
# tambien se calcula el factor promedio de reduccion del error por iteracion

print("ORDEN DE CONVERGENCIA ESTIMADO")
print()

archivo = open(os.path.join(carpeta_data, "orden_convergencia.csv"), "w")
archivo.write("metodo,funcion,puntos,orden,factor\n")

for metodo in metodos_nombres:
    for i in range(6):
        ruta = os.path.join(carpeta_data, "pasos_" + metodo + "_" + nombres[i] + ".csv")
        if not os.path.exists(ruta):
            print(metodo, "|", nombres[i], "| sin datos (no aplica)")
            continue

        datos = np.loadtxt(ruta, delimiter=",", skiprows=1, ndmin=2)
        error = datos[:, 2]
        error = error[error > 1e-13]

        ordenes = []
        for k in range(1, len(error) - 1):
            if error[k + 1] < error[k] and error[k] < error[k - 1]:
                ordenes.append(np.log(error[k + 1] / error[k]) / np.log(error[k] / error[k - 1]))

        if len(ordenes) > 0:
            orden = np.median(ordenes)
        else:
            orden = float("nan")

        if len(error) > 1:
            factor = (error[-1] / error[0]) ** (1 / (len(error) - 1))
        else:
            factor = float("nan")

        print(metodo, "|", nombres[i], "| puntos usados =", len(ordenes), "| orden =", round(orden, 2), "| factor =", round(factor, 3))
        archivo.write(metodo + "," + nombres[i] + "," + str(len(ordenes)) + "," + str(orden) + "," + str(factor) + "\n")

archivo.close()
print()
print("CSV guardado en src/data/orden_convergencia.csv")
