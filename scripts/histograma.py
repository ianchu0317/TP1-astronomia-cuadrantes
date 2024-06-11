import matplotlib.pyplot as plt
import numpy as np

# Cargar latitudes
with open('latitudes.txt', 'r') as file:
    latitudes = file.read()
latitudes = latitudes.split()

# Cargar grupos
with open('grupos_latitudes.txt', 'r') as file:
    grupos = file.read()
grupos = grupos.split()

# Limpiar dato
latitudes = [float(latitud.replace(',', '.')) for latitud in latitudes]

# Constantes
lat_max = -38.5
lat_min = -30

# Graficar
fig, ax = plt.subplots()
# Plot
plt.bar(grupos, latitudes)
# Axis configuraciones
plt.ylim((lat_min, lat_max))
# ax.yaxis.set_ticks(np.arange(lat_max, lat_min, 0.25))
plt.grid(linestyle=':')
# Título y nombre
ax.set_ylabel('Latitudes')
ax.set_xlabel('Grupos')
ax.set_title('Histograma de latitudes por grupo')
plt.show()
print(latitudes)
