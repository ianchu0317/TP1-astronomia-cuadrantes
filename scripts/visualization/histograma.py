"""
Programa para realizar histograma (gráfico en barra)
con valores de latitudes promedios obtenidas por cada grupo.
Eje X de histograma van los intervalos (clase).
Eje Y de histograma van la cantidad de grupo que obtuvo el intervalo (frecuencia).

Los sus latitudes se cargan del archivo 'latitudes.txt'.
"""

import matplotlib.pyplot as plt
import numpy as np


# Función para cargar datos desde archivo
def load_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
    data = data.split()
    return data


# Limpiar datos
def data_frequency(my_list):
    # Números límites
    current_number = max(my_list)
    max_item = min(my_list)

    # Nuevas variables
    step = 0.25  # intervalo
    freq_list = []

    # Loop interval 0.25 between -31, -38.25
    while current_number + step > max_item:
        freq_count = 0
        for element in my_list:
            if current_number >= element > current_number - step:
                freq_count += 1
                # print(freq_count)

        # print(current_number, freq_count)
        freq_list.append(freq_count)
        # new_dict.update({f'{(current_number, current_number - step)}': freq_count})
        current_number -= step

    return freq_list


# Cargar datos
latitudes = load_data('latitudes.txt')
grupos_total = len(latitudes)  # cantidad total de grupos

# Limpieza, conversión y organización de dato
latitudes = np.array([float(data.replace(',', '.')) for data in latitudes])

# Datos para graficar
eje_x_label = np.arange(-31, -38.5, -0.25)  # clase
x_label = []
counter = 0
for x in eje_x_label:
    if counter % 2 == 0:
        x_label.append(x)
    else:
        x_label.append('')
    counter += 1
eje_x = np.arange(0, len(eje_x_label), 1)  # clase
eje_y = data_frequency(latitudes)  # frecuencia

print(eje_y)
print(eje_x)

# Graficar
fig, ax = plt.subplots(figsize=(14, 7), layout='constrained')
plt.bar(eje_x + 0.5, eje_y, width=1, edgecolor='black')

# Configuraciones de ejes
plt.ylim((min(eje_y), max(eje_y)+1))
ax.xaxis.set_ticks(eje_x, eje_x_label)

# Configuración de título
ax.set_ylabel('Cantidad de grupos', fontsize=10)
ax.set_xlabel('Latitud [º] (intervalo de 0.25º)', fontsize=10)

ax.set_title('Histograma con la distribución estadística de los valores de la latitud obtenidos por todos los grupos', fontsize=16)

ax.grid(True, linestyle='--', linewidth=0.4)
plt.savefig('histograma.png')
plt.show()
