#Integrantes:
#Hernandez Ruiz Haydee Michelle
#Montoya Garza Luis Angel
#Rueda Martinez Alison Michelle
#Silva Sanchez Yamilka Arely

import serial
import time

try:
    ser = serial.Serial('COM13', 9600, timeout=1)  # Cambia 'COM' si es necesario
    time.sleep(2)  # Espera a que el puerto se abra completamente

    while True:
        if ser.in_waiting > 0:  # Verifica si hay datos disponibles
            line = ser.readline().decode('utf-8').rstrip()  # Lee la línea de datos
            try:
                sensor_value = int(line)  # Convierte la línea a entero
                print(f"Valor del sensor: {sensor_value}")
                
                if sensor_value > 500:  # Umbral para encender el LED
                    ser.write(b'1\n')  # Envía '1' para encender el LED
                else:
                    ser.write(b'0\n')  # Envía '0' para apagar el LED
            except ValueError:
                print(f"Dato recibido no es un entero: {line}")
        
        time.sleep(0.1)  # Espera 0.1 segundos

except serial.SerialException as e:
    print(f"Error de puerto serie: {e}")
except KeyboardInterrupt:
    print("Programa terminado por el usuario.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
