import csv
import math
import matplotlib.pyplot as plt

# Función para cargar datos del archivo CSV
def cargar_datos_csv(nombre_archivo):
    datos = {}
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')
        for fila in lector_csv:
            for columna, valor in fila.items():
                if columna not in datos:
                    datos[columna] = []
                try:
                    datos[columna].append(float(valor))
                except ValueError:
                    pass
    return datos

# Función para calcular la media y desviación estándar
def media(valores):
    return sum(valores) / len(valores)

def desviacion_estandar(valores):
    mu = media(valores)
    return math.sqrt(sum((x - mu) ** 2 for x in valores) / len(valores))

# Función para graficar distribuciones
def graficar_distribuciones(datos):
    for columna, valores in datos.items():
        if valores:
            # Cálculos necesarios
            mu = media(valores)
            sigma = desviacion_estandar(valores)

            # Valores para la distribución gaussiana
            x_gauss = [mu - 4 * sigma + i * (8 * sigma / 100) for i in range(101)]
            gaussiana = [1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in x_gauss]

            # Valores para la distribución de Bernoulli
            p = mu / max(valores)  # Probabilidad de éxito
            x_bernoulli = [0, 1]
            bernoulli = [(1 - p), p]

            # Valores para la distribución de Poisson
            lambda_poisson = mu
            poisson_x = list(range(0, min(int(max(valores)), 20) + 1))  # Limitar el rango de k
            poisson_pmf = [(lambda_poisson ** k * math.exp(-lambda_poisson)) / math.factorial(k) for k in poisson_x]

            # Graficar el histograma
            plt.figure(figsize=(12, 6))
            plt.hist(valores, bins=30, density=True, alpha=0.5, color='gray', label='Histograma de Datos')

            # Graficar las distribuciones
            plt.plot(x_gauss, gaussiana, label='Distribución Gaussiana', color='blue')
            plt.bar(x_bernoulli, bernoulli, width=0.1, label='Distribución de Bernoulli', color='green', alpha=0.6)
            plt.stem(poisson_x, poisson_pmf, label='Distribución de Poisson', basefmt=" ", linefmt='orange', markerfmt='ro')

            plt.title(f'Distribuciones de {columna}')
            plt.xlabel('Valores')
            plt.ylabel('Densidad de Probabilidad')
            plt.legend()
            plt.grid()
            plt.show()

# Cargar y procesar el archivo
nombre_archivo = 'data.csv'  # Cambia el nombre del archivo si es necesario
datos = cargar_datos_csv(nombre_archivo)

# Graficar distribuciones
graficar_distribuciones(datos)
