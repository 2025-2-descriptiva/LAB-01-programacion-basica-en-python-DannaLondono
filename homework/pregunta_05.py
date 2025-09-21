"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    import csv 
    
    conteo = {}
    with open("files/input/data.csv", 
              newline='', encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        for fila in lector:
            letra = fila[0]
            numero = int(fila[1])

            if letra not in conteo:
                conteo[letra] = [numero, numero] 
            else:
                
                if numero < conteo[letra][0]:
                    conteo[letra][0] = numero
             
                if numero > conteo[letra][1]:
                    conteo[letra][1] = numero

    resultado = [(letra, conteo[letra][1], conteo[letra][0]) for letra in sorted(conteo.keys())]
    return resultado


# Ejemplo de ejecución
print(pregunta_05())
