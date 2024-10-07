"""
Sin el uso de librerías en Python programe el percentil y cuartil de cada columna. Que distribución se puede aplicar en su caso normal, Bernoulli, gaussiana, poisson, otros. Indique la razón de su uso graficando con matplotlib.
"""

import csv

# Función para calcular percentil
def calcular_percentil(datos, percentil):
    datos_ordenados = sorted(datos)
    k = (len(datos_ordenados) - 1) * (percentil / 100)
    f = int(k)
    c = k - f
    if f + 1 < len(datos_ordenados):
        return datos_ordenados[f] + (c * (datos_ordenados[f + 1] - datos_ordenados[f]))
    else:
        return datos_ordenados[f]

# Función para calcular cuartiles
def calcular_cuartiles(datos):
    q1 = calcular_percentil(datos, 25)
    q2 = calcular_percentil(datos, 50)
    q3 = calcular_percentil(datos, 75)
    return q1, q2, q3

# Cargar datos del archivo CSV
def cargar_datos_csv(nombre_archivo):
    datos = {}
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')
        for fila in lector_csv:
            for columna, valor in fila.items():
                if columna not in datos:
                    datos[columna] = []
                # Intentar convertir los valores numéricos, ignorar no numéricos
                try:
                    datos[columna].append(float(valor))
                except ValueError:
                    pass
    return datos

# Calcular percentiles y cuartiles para cada columna
def procesar_datos(datos):
    resultados = {}
    for columna, valores in datos.items():
        if valores:
            q1, q2, q3 = calcular_cuartiles(valores)
            resultados[columna] = {
                'Q1': q1,
                'Q2': q2,
                'Q3': q3,
                'Percentil 90': calcular_percentil(valores, 90)
            }
    return resultados

# Cargar y procesar el archivo
nombre_archivo = 'data.csv'
datos = cargar_datos_csv(nombre_archivo)
resultados = procesar_datos(datos)

# Mostrar resultados
for columna, valores in resultados.items():
    print(f"Columna: {columna}")
    for clave, valor in valores.items():
        print(f"  {clave}: {valor}")
