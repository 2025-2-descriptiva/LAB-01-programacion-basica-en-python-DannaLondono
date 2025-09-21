"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv 
    suma = 0
    with open("C:/Users/DANNA/Documents/GitHub/LAB-01-programacion-basica-en-python-DannaLondono/files/input/data.csv", newline='', encoding="utf-8") as archivo:
        lector = csv.reader(archivo,  delimiter="\t")  
        for fila in lector:
            if len(fila) > 1:   
                suma += int(fila[1])
    return suma

print("RTA:", pregunta_01())
        