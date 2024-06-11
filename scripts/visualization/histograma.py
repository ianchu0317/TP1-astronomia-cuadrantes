"""
Programa para realizar histograma (gráfico en barra)
con valores de latitudes promedios obtenidas por cada grupo.
Eje X de histograma van los grupos.
Eje Y de histograma van los valores de latitudes promedios.

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

# Posiciones de barras
bar_width = 0.25
br1 = np.arange(len(grupos))
br2 = [x - bar_width for x in br1]
br3 = [x + bar_width for x in br1]
# x_rect = np.linspace(0, 21, 100)
# y_rect = np.zeros(len(x_rect))
# y_rect = [latitud_ba + y for y in y_rect]

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
plt.bar(br1, latitudes, width=bar_width, color='blue', align='center', label='Latitud promedia')
plt.bar(br2, min_latitudes, width=bar_width, color='red', align='center', label='Latitud promedia + incerteza')
plt.bar(br3, max_latitudes, width=bar_width, color='violet', align='center', label='Latitud promedia - incerteza')
# plt.plot(x_rect, y_rect, color='black', label='Latitud de Buenos Aires')

# Configuraciones de ejes
plt.ylim((lat_min, lat_max))
# ax.yaxis.set_ticks(y_ticks, y_elements)
ax.yaxis.set_ticks(y_ticks)
ax.xaxis.set_ticks(br1, grupos)

# Título y nombre
ax.set_ylabel('Latitud promedio [º]')
ax.set_xlabel('Número de grupo')
ax.set_title('Histograma de latitudes por grupo', fontsize=14)

plt.grid(linestyle=':', linewidth=0.65)
plt.legend()

# Render
plt.savefig('histograma.png')
plt.show()

