"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    import csv 
    conteo= {}
    with open("C:/Users/DANNA/Documents/GitHub/LAB-01-programacion-basica-en-python-DannaLondono/files/input/data.csv", newline='', encoding="utf-8") as archivo:
     lector = csv.reader(archivo,  delimiter="\t")  
     for fila in lector:
            
             tupla= fila [0]
             suma= int(fila [1]) 
             conteo[tupla]= conteo.get(tupla,0) + suma
    return (sorted(conteo.items()))
print (pregunta_03())

