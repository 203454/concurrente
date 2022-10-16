# Crear una aplicación con las siguientes características.

# Existen uno o más productores y uno o más consumidores,
# todos almacenan y extraen productos de una misma bodega. 
# 
# El productor produce productos cada vez que puede, y el consumidor 
# los consume cada vez que lo necesita.

# Problema:
# coordinar a los productores y consumidores, para que los 
# productores no produzcan más ítems de los que se pueden 
# almacenar en el momento, y los consumidores no adquieran más
#  ítems de los que hay disponibles.

# PARA ESTO APLICARA METODOS DE SINCRONIZACIÓN Y COMUNICACIÓN 
# JUNTO A SEMAFOROS
import threading
import random 
import queue
import time 

BODEGA = queue.Queue(maxsize=random.randint(20, 50))
PRODUCTORES = random.randint(5, 10)
CONSUMIDORES = random.randint(5, 10)
condition = threading.Condition()

class Productor(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    
    def run(self):
        while True:
            if condition.acquire():
                if BODEGA.full():
                    condition.wait()
                else:
                    item = random.randint(1, 100)
                    BODEGA.put(item)
                    print("El productor "+  str(self.id)  +" produjo => " + str(item))
                    condition.notify()
                    condition.release()
                    time.sleep(4)
    
class Consumidor(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        while True:
            if condition.acquire():
                if BODEGA.empty():
                    condition.wait()
                else:
                    item = BODEGA.get()
                    print("El consumidor "+  str(self.id)  +" consumio => " + str(item))
                    condition.notify()
                    condition.release()
                    time.sleep(4)

                


if __name__ == '__main__':
    productores = []
    consumidores = []
    for i in range(PRODUCTORES):
        productores.append(Productor(i))
    for i in range(CONSUMIDORES):
        consumidores.append(Consumidor(i))
    
    for i in productores:
        i.start()
    for i in consumidores:
        i.start()