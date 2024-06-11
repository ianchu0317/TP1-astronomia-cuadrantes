"""
Programa para hallar latitudes de cada medición utilizando ecuaciones correspondientes.
También devuelve el valor promedio de latitud.

Son 20 mediciones (en decimal) de las estrellas Acrux y Becrux de la Cruz del Sur,
cuyas declinaciones son: -64º 5' 57'' (Acrux) y -59º 41' 19'' (Becrux).

Principal razón de la creación del programa es por el uso incompatible del sistema
sexagesimal en planillas de excel. Por lo tanto, es preferible automatizar la tarea de cálculo.

****USO****
- Ubicar todas las mediciones (en orden) en altura1.txt y altura2.txt de cada estrella medida. 
- Modificar valores de las declinaciones de las estrellas medidas (en sexagesimal): 
    'decl1' para la estrella medida para 'altura1.txt' y decl2 para la estrella medida para 'altura2.txt'.
- Modificar la función 'hallar_latitud()' con la ecuación correspondiente de la estrella a medir.
"""

# Conversión de sexagesimal (grados, minutos y segundos) a decimal
def dms_to_decimal(value):
    # value: 'deg min sec' ex. '97 45 23'
    deg, min_, sec = value.split()
    dec = int(deg) + int(min_)/60 + int(sec)/3600
    print(dec)
    return dec


# Conversión de decimal a sexagesimal
def decimal_to_dms(value):
    degree = int(value)
    minute = int((value - degree)*60)
    second = ((value - degree)*60 - minute)*60
    sexagesimal = f'{degree} {minute} {second}'
    return sexagesimal


# Hallar promedio total
def average(val1, val2):
    # Suma de todos los valores obtenidos
    val_sum = 0
    for val in val1:
        val_sum += val
    for val in val2:
        val_sum += val
    # División de suma total por cantidad total
    return val_sum/(len(val1) + len(val2))


# Hallar latitud para cada altura
def hallar_latitud(decl, alt):
    return 90 + decl - alt


# Declinaciones de estrellas
decl1 = '-64 5 57'  # Declinación Acrux
decl2 = '-59 41 19'  # Declinación Mimosa, Becrux
decl1_dec = dms_to_decimal(decl1)  # Declinación Acrux decimal
decl2_dec = dms_to_decimal(decl2)  # Declinación Becrux decimal

# Alturas Acrux
with open('altura1.txt', 'r') as file:
    alturas1 = file.read()
alturas1 = alturas1.split()
# Alturas Becrux
with open('altura2.txt', 'r') as file:
    alturas2 = file.read()
alturas2 = alturas2.split()

# Latitudes halladas
lat_1 = []  # Latitudes halladas por primera estrella
lat_2 = []  # Latitudes halladas por segunda estrella

# Hallar latitudes
# Acrux
for altura in alturas1:
    altura = int(altura)
    lat = hallar_latitud(decl1_dec, altura)
    lat_1.append(lat)
# Becrux
for altura in alturas2:
    altura = int(altura)
    lat = hallar_latitud(decl2_dec, altura)
    lat_2.append(lat)

# Imprimir latitudes halladas
print('**** LATITUDES ACRUX ****')
for lat in lat_1:
    print(decimal_to_dms(lat))
print('**** LATITUDES BECRUX ****')
for lat in lat_2:
    print(decimal_to_dms(lat))
print('**** LATITUD PROMEDIO ****')
print(decimal_to_dms(average(lat_1, lat_2)))
