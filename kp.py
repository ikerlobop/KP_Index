import requests
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.dates as mdates
from datetime import datetime

# URL de la API de NOAA para el índice Kp
url = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"

# Función para obtener los últimos 20 valores del índice Kp
def obtener_ultimos_20_kp():
    response = requests.get(url)
    response.raise_for_status()
    kp_data = response.json()
    return kp_data[:20] 

def parse_time(time_string):
    try:
        return datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%S')

# Obtener los datos
kp_data = obtener_ultimos_20_kp()

# Extraer fechas y valores del índice Kp
fechas = [parse_time(kp['time_tag']) for kp in kp_data]
kp_indices = [kp['kp_index'] for kp in kp_data]

# Crear el mapa de colores basado en los valores de Kp
cmap = colors.ListedColormap(['green', 'yellow', 'orange', 'red'])
bounds = [0, 4, 5, 7, 9]  # Definir los límites para los colores
norm = colors.BoundaryNorm(bounds, cmap.N)

# Graficar los valores
fig, ax = plt.subplots()
sc = ax.scatter(fechas, kp_indices, c=kp_indices, cmap=cmap, norm=norm, s=100)

# Formato de la fecha en el eje x
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
plt.xticks(rotation=45, ha='right')

# Etiquetas y título
plt.xlabel('Fecha y Hora')
plt.ylabel('Índice Kp')
plt.title('Índice Kp de las últimas 20 observaciones')

# Añadir la barra de colores
cbar = plt.colorbar(sc, ticks=[1, 3, 5, 7, 9])
cbar.ax.set_yticklabels(['Bajo', 'Moderado', 'Activo', 'Tormenta', 'Tormenta severa'])

plt.tight_layout()
plt.show()
