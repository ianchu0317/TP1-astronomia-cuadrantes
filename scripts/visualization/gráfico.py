"""
Programa para realizar visualización en gráfico
con valores de latitudes promedios obtenidas por cada grupo.
Eje X de gráfico van los grupos.
Eje Y de gráfico van los valores de latitudes promedios.

Los valores de grupos y sus latitudes se cargan de los archivos
'grupos_latitudes.txt' y 'latitudes.txt' respectivamente.
"""

import matplotlib.pyplot as plt
import numpy as np


# Función para cargar datos desde archivo
def cargar_datos(filename):
    with open(filename, 'r') as file:
        data = file.read()
    data = data.split()
    return data


# Función para limpiar datos
def limpiar_datos(datas):
    clean_data = []
    for data in datas:
        if data == '-':
            clean_data.append(float(0))
        else:
            clean_data.append(float(data.replace(',', '.')))
    return np.array(clean_data)


# Cargar datos
latitudes = cargar_datos('latitudes.txt')
grupos = cargar_datos('grupos_latitudes.txt')
incertezas = cargar_datos('incertezas.txt')

# Limpieza y conversión de dato
latitudes = limpiar_datos(latitudes)
incertezas = limpiar_datos(incertezas)

# valores de incertezas máximas y mínimas
max_latitudes = latitudes - incertezas
min_latitudes = latitudes + incertezas

# Constantes de gráfico
lat_max = -43
lat_min = -29
latitud_ba = -34.61315

# Posiciones en Eje x
x_axis = np.arange(len(grupos))
dot_size = 30  # pt

# Eje Y
y_ticks = np.arange(lat_max, lat_min, 0.25)
y_elements = []
counter = 0
for element in y_ticks:
    if counter % 2 == 0:
        y_elements.append(element)
    else:
        y_elements.append('')
    counter += 1

fig, ax = plt.subplots(figsize=(12, 9), layout='constrained')

# Plots
# Puntos
pt1 = plt.scatter(x_axis, max_latitudes, s=dot_size, c='#D217CC', marker='*', label='Latitud promedio - incerteza')
pt2 = plt.scatter(x_axis, min_latitudes, s=dot_size, c='#E1364C', marker='*', label='Latitud promedio + incerteza')
pt3 = plt.scatter(x_axis, latitudes, s=dot_size, c='#4444F6', marker='o', label='Latitud promedio')
# Línea
ln1, = plt.plot(x_axis, max_latitudes, color='violet', linewidth=0.5, label='test')
ln2, = plt.plot(x_axis, min_latitudes, color='red', linewidth=0.5, label='test')
ln3, = plt.plot(x_axis, latitudes, color='blue', linewidth=0.5, label='test')
ln4, = plt.plot(x_axis, [latitud_ba + y for y in np.zeros(len(x_axis))], color='#734848',
                linewidth=1, linestyle='--', label='test')

# Configuraciones de ejes
plt.ylim((lat_min, lat_max))
ax.yaxis.set_ticks(y_ticks, y_elements)
ax.yaxis.set_ticks(y_ticks)
ax.xaxis.set_ticks(x_axis, grupos)

# Título y nombre
ax.set_ylabel('Latitud promedio [º]', fontsize=10)
ax.set_xlabel('Número de grupo', fontsize=10)
ax.set_title('Gráfico de latitudes promedios con incertezas', fontsize=16)

nombres_lineas = ['Variación latitud promedio - incerteza',
                  'Variación latitud promedio + incerteza',
                  'Variación latitud promedio',
                  'Latitud promedio de Buenos Aires']

# Leyendas (carteles)
legend1 = ax.legend(handles=[pt1, pt2, pt3], title='Puntos')
ax.add_artist(legend1)
ax.legend([ln1, ln2, ln3, ln4], nombres_lineas, loc='upper center', title='Líneas de variación')
plt.grid(linestyle=':', linewidth=0.5)

# Render
plt.savefig('gráfico_análisis.png')
plt.show()

