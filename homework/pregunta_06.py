"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    import csv
    conteo = {}
    with open("C:/Users/DANNA/Documents/GitHub/LAB-01-programacion-basica-en-python-DannaLondono/files/input/data.csv", 
              newline='', encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        for fila in lector:
            diccionario = fila[4].split(",")
            for elemento in diccionario:
                clave, valor = elemento.split(":")
                valor = int(valor)

                if clave not in conteo:

                    conteo[clave] = [valor, valor] 
                else:
                    
                    if valor < conteo[clave][0]:
                        conteo[clave][0] = valor
                 
                    if valor > conteo[clave][1]:
                        conteo[clave][1] = valor
    resultado = [(clave, conteo[clave][0], conteo[clave][1]) for clave in sorted(conteo.keys())]                       
    return resultado
print (pregunta_06())



        