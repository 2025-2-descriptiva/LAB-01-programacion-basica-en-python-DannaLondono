def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    import csv 
    
    conteo = {}
    with open("C:/Users/DANNA/Documents/GitHub/LAB-01-programacion-basica-en-python-DannaLondono/files/input/data.csv", 
              newline='', encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter="\t")
        for fila in lector:
            letra = fila[0]
            numero = int(fila[1])

            if letra not in conteo:
                conteo[letra] = [numero, numero]  # [min, max]
            else:
                # actualizar mínimo
                if numero < conteo[letra][0]:
                    conteo[letra][0] = numero
                # actualizar máximo
                if numero > conteo[letra][1]:
                    conteo[letra][1] = numero

    # Retornar lista de tuplas en orden alfabético: (letra, max, min)
    resultado = [(letra, conteo[letra][1], conteo[letra][0]) for letra in sorted(conteo.keys())]
    return resultado


# Ejemplo de ejecución
print(pregunta_05())
