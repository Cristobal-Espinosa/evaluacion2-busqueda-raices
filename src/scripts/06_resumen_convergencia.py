import os

carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")

metodos_nombres = ["biseccion", "falsa_posicion", "punto_fijo", "secante", "newton", "newton_mejorado"]

# junto los resumen_<metodo>.csv en un solo archivo
salida = open(os.path.join(carpeta_data, "resumen_convergencia.csv"), "w")
salida.write("metodo,funcion,iteraciones,raiz,error,convergio\n")

print("RESUMEN DE CONVERGENCIA")
print()

for metodo in metodos_nombres:
    archivo = open(os.path.join(carpeta_data, "resumen_" + metodo + ".csv"))
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas[1:]:      # salto el encabezado
        linea = linea.strip()
        salida.write(metodo + "," + linea + "\n")

        partes = linea.split(",")
        print(metodo, "|", partes[0], "| iteraciones =", partes[1], "| error =", partes[3], "| convergio =", partes[4])
    print()

salida.close()
print("CSV guardado en src/data/resumen_convergencia.csv")