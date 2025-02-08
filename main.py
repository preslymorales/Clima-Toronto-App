import requests
import csv
from datetime import datetime

# Configuración de la API
API_KEY = "1cd0b2dac179557e6acd923869e1f565"
LATITUD = 43.7001
LONGITUD = -79.4163
URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUD}&lon={LONGITUD}&appid={API_KEY}&units=metric"

# Obtener datos climáticos
response = requests.get(URL)
data = response.json()

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
archivo_csv = "/home/iccd332/Clima-Toronto-App/clima-toronto-hoy.csv"
encabezado = ["Fecha y Hora", "Ciudad", "Temperatura (°C)", "Humedad (%)", "Presión (hPa)", "Viento (m/s)", "Descripción"]
columnas_ancho = [20, 10, 20, 15, 15, 15, 25]  # Anchura de cada columna
nuevo_registro = [fecha_hora, ciudad, f"{temperatura:.1f}", f"{humedad}", f"{presion}", f"{viento_velocidad:.1f}", descripcion]

# Función para generar una línea alineada
def formatear_fila(fila, ancho):
    return "| " + " | ".join([f"{str(dato):<{ancho[i]}}" for i, dato in enumerate(fila)]) + " |"

# Escribir los datos
with open(archivo_csv, mode="a", newline="", encoding="utf-8") as file:
    # Si el archivo está vacío, escribir el encabezado formateado
    if file.tell() == 0:
        file.write(formatear_fila(encabezado, columnas_ancho) + "\n")
        file.write("|" + "|".join(["-" * (ancho + 2) for ancho in columnas_ancho]) + "|\n")  # Línea separadora
    file.write(formatear_fila(nuevo_registro, columnas_ancho) + "\n")

print("Datos climáticos guardados correctamente.")
