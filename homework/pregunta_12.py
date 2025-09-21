"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    import csv 
    conteo = {}
    with open("C:/Users/DANNA/Documents/GitHub/LAB-01-programacion-basica-en-python-DannaLondono/files/input/data.csv", 
              newline='', encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        for fila in lector:
            letra = fila[0]
            columna5 = fila[4].split(",") 
            suma_columna5 = sum(int(item.split(":")[1]) for item in columna5)
            conteo[letra] = conteo.get(letra, 0) + suma_columna5

    return dict(sorted(conteo.items()))
print(pregunta_12())
