# Visualización del Índice Kp

Este proyecto realiza una consulta a la API de la NOAA para obtener los últimos valores del índice Kp, que mide la actividad geomagnética de la Tierra. Los datos obtenidos se visualizan en un gráfico dinámico utilizando la biblioteca `matplotlib` en Python.

## Descripción

El índice Kp es una medida de la actividad geomagnética global en la Tierra. Este script descarga los últimos 20 valores del índice Kp desde una API pública y genera un gráfico de dispersión con colores que indican el nivel de actividad geomagnética. Los datos son proporcionados por la NOAA, la cual ofrece monitoreo en tiempo real de tormentas geomagnéticas y otros eventos espaciales.

![image](https://github.com/user-attachments/assets/5e81e904-2c8f-4b1b-b5db-e64bfa9ffee6)

## Características

- Consulta de los últimos 20 valores del índice Kp desde la API de NOAA.
- Visualización gráfica con colores basados en la intensidad del índice Kp:
  - Verde: Kp bajo (0-4)
  - Amarillo: Moderado (5)
  - Naranja: Activo (6-7)
  - Rojo: Tormenta geomagnética severa (8-9)
- Formato claro de fechas y valores en el gráfico.

## Requisitos

Asegúrate de tener instalado Python 3.x y las siguientes librerías antes de ejecutar el script:

- `requests`
- `matplotlib`

Instala las dependencias con el comando adecuado en tu entorno de desarrollo.

## Uso

Para ejecutar este proyecto, sigue estos pasos:

1. Clona el repositorio desde el enlace del proyecto en GitHub.
2. Accede al directorio del proyecto.
3. Ejecuta el script para obtener y visualizar los datos del índice Kp.

Al ejecutar el script, verás una gráfica con los últimos 20 valores del índice Kp, con fechas y colores correspondientes a la intensidad geomagnética.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el código, añadir nuevas características o corregir errores, por favor sigue los pasos habituales para abrir un *issue* o enviar una *pull request*.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Referencias

- [NOAA Space Weather Prediction Center](https://www.swpc.noaa.gov/)
