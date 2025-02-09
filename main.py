import requests
import csv
import os
from datetime import datetime

# Conexión a la API
API_KEY = "1cd0b2dac179557e6acd923869e1f565"
LATITUD = 43.7001
LONGITUD = -79.4163
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUD}&lon={LONGITUD}&appid={API_KEY}&units=metric"

# Obtener datos climáticos
try:
    response = requests.get(URL)
    response.raise_for_status()  #si la solicitud no es exitosa
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error al conectarse a la API: {e}")
    exit()

# Extraer datos del clima
if response.status_code == 200:
    temperatura = data["main"]["temp"]
    humedad = data["main"]["humidity"]
    presion = data["main"]["pressure"]
    viento_velocidad = data["wind"]["speed"]
    descripcion = data["weather"][0]["description"]
    ciudad = data.get("name", "Desconocido") 
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
else:
    print("Error al obtener datos climáticos")
    exit()

# Guardar datos en un archivo CSV
archivo_csv = "/home/iccd332/TorontoWeather/clima-toronto-hoy.csv"
encabezado = ["Fecha y Hora", "Ciudad", "Temperatura (°C)", "Humedad (%)", "Presión (hPa)", "Viento (m/s)", "Descripción"]
columnas_ancho = [20, 10, 20, 15, 15, 15, 25]  # Anchura de cada columna
nuevo_registro = [fecha_hora, ciudad, f"{temperatura:.1f}", f"{humedad}", f"{presion}", f"{viento_velocidad:.1f}", descripcion]

# Función para generar una línea alineada
def formatear_fila(fila, ancho):
    return "| " + " | ".join([f"{str(dato):<{ancho[i]}}" for i, dato in enumerate(fila)]) + " |"

# Función para contar el número de líneas en el archivo
def contar_lineas(archivo):
    if os.path.exists(archivo):
        with open(archivo, mode="r", encoding="utf-8") as file:
            return sum(1 for line in file)
    return 0

# Verificar si ya hay 50 datos en el archivo
if contar_lineas(archivo_csv) < 52:
# Escribir los datos
    with open(archivo_csv, mode="a", newline="", encoding="utf-8") as file:
        # Si el archivo está vacío, escribir el encabezado formateado
        if file.tell() == 0:
            file.write(formatear_fila(encabezado, columnas_ancho) + "\n")
            file.write("|" + "|".join(["-" * (ancho + 2) for ancho in columnas_ancho]) + "|\n")
# Línea separadora
        file.write(formatear_fila(nuevo_registro, columnas_ancho) + "\n")
    print("Datos climáticos guardados correctamente.")
else:
    print("No se puede agregar mas datos ya hay 50 registros.")
