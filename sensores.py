import time
from time import perf_counter
import threading

class Sensor:
    def __init__(self, nombre, duracion):
        self.duracion = duracion
        self.nombre = nombre
        self.duracion_obtenida = 0

    def leer(self):
        time.sleep(self.duracion)
        self.duracion_obtenida = perf_counter()

sensores = [Sensor("S1", 1), Sensor("S2", 2), Sensor("S3", 1.5)]

def conHilos():
    hilos = [
        threading.Thread(target=sensores[0].leer),
        threading.Thread(target=sensores[1].leer),
        threading.Thread(target=sensores[2].leer),
    ]

    # ======================
    print("Leyendo simulacion de sensores")

    t_inicio = perf_counter()
    hilos[0].start()
    hilos[1].start()
    hilos[2].start()

    hilos[0].join()
    hilos[1].join()
    hilos[2].join()
    t_total = perf_counter()


    for sensor in sensores:
        print("Lectura de sensor: ", sensor.nombre)
        print("Tiempo esperado: ", str(sensor.duracion))
        print("Tiempo transcurrido: ", str(sensor.duracion_obtenida - t_inicio))
        print("======================")

    print("Total:", t_total - t_inicio)

    # ======================


def secuencial():
    t_inicio = perf_counter()
    for sensor in sensores:
        sensor.leer()
    t_total = perf_counter()

    for sensor in sensores:
            print("Lectura de sensor: ", sensor.nombre)
            print("Tiempo esperado: ", str(sensor.duracion))
            print("Tiempo transcurrido: ", str(sensor.duracion_obtenida - t_inicio))
            print("======================")
    print("Total:", t_total - t_inicio)

if __name__ == "__main__":
     conHilos()