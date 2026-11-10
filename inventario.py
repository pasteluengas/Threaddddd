import threading

class Tienda:
    def __init__(self):
        self.inventario = 1
        self.ventas = 0
        self.barrera = threading.Barrier(2)

    def vender(self):
        vender = (self.inventario > 0)

        self.barrera.wait()
        
        if vender:
            print("Venta aprobada")
            self.inventario -= 1
        else:
            print("Venta no aprobada")
            return


tienda1 = Tienda()
hilo1 = threading.Thread(target=tienda1.vender)
hilo2 = threading.Thread(target=tienda1.vender)

print("======= TIENDA SIN LOCK ========")

hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print("Cantidad final: ", tienda1.inventario)

class TiendaConLock(Tienda):
    def __init__(self):
        Tienda.__init__(self)
        self.lock = threading.Lock()

    def vender(self):
        with self.lock:
            if self.inventario > 0:
                print("Venta aprobada")
                self.inventario -= 1
            else:
                print("Venta no aprobada")
        
tienda2 = TiendaConLock()
hilo1 = threading.Thread(target=tienda2.vender)
hilo2 = threading.Thread(target=tienda2.vender)

print("======= TIENDA CON LOCK ========")

hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
print("Cantidad final: ", tienda2.inventario)

assert tienda2.inventario == 0, f"Error: El inventario quedó en {tienda2.inventario}."
print("¡Prueba superada con éxito.\n")