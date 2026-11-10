import time
from time import perf_counter
import threading

class Sensor:
    def __init__(self, nombre, duracion):
        self.duracion = duracion
        self.nombre = nombre

    def leer(self):
        time.sleep(self.duracion)

sensores = [Sensor("S1", 1), Sensor("S2", 2), Sensor("S3", 1.5)]
hilos = [
    threading.Thread(target=sensores[0].leer),
    threading.Thread(target=sensores[1].leer),
    threading.Thread(target=sensores[2].leer),
]

# ======================
print("Leyendo simulacion de sensores")

for hilo_index, hilo_sensor in enumerate(hilos):
    t_inicio = perf_counter()
    hilo_sensor.start()
    hilo_sensor.join()
    t_fin = perf_counter()


    print("Lectura de sensor: ", sensores[hilo_index].nombre)
    print("Tiempo esperado: ", str(sensores[hilo_index].duracion))
    print("Tiempo transcurrido: ", str(t_fin - t_inicio))
    print("======================")

# ======================



