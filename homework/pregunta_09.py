"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    import csv 
    
    conteo = {}
    with open("files/input/data.csv", 
              newline='', encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        for fila in lector:
            diccionario = fila[4].split(",")
            for elemento in diccionario:
                clave, _ = elemento.split(":")
                if clave not in conteo:
                    conteo[clave] = 1
                else:
                    conteo[clave] += 1  
    resultado= conteo
    return resultado
print(pregunta_09())