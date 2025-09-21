"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    import csv 
    conteo= {}
    with open("files/input/data.csv", newline='', encoding="utf-8") as archivo:
     lector = csv.reader(archivo,  delimiter="\t")  
     for fila in lector:
            if len(fila) > 0:
             tupla= fila [0]
             conteo[tupla]= conteo.get(tupla,0) + 1 
    return (sorted(conteo.items()))
print (pregunta_02())


                                               

