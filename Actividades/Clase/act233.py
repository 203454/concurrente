import queue
import threading
import time
import random


BODEGA = queue.Queue(maxsize=20)

CONSUMIDORES = random.randint(1, 10)
PRODUCTORES = random.randint(1, 10)

mutex = threading.Lock()
condition = threading.Condition()
class Consumidor(threading.Thread):

    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def Consumir(self):
        time.sleep(3)
        while True:
            if(BODEGA.qsize() == 0):
                print("La bodega esta vacia...")
                time.sleep(5)
            else:
                # mutex.acquire()    
                time.sleep(2)
                print("el consumidor: ",self.id," ha adquirido un producto a la bodega: ",BODEGA.get(),"tamaño de la bodega: ", BODEGA.qsize())
                # mutex.release()
        
    def run(self):
        print("Consumidor: ",self.id, "tamaño: ", BODEGA.qsize())
        self.Consumir()
        
class Productor(threading.Thread):

    #declaracion del metodo constructor 
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    #Metodo producir que es donde llenamos la cola o queue
    def producir(self):

        productos = ["Maiz","Arroz","Frijol","Platano","Manzana"]

        while BODEGA.full() == False:
                time.sleep(2)
                mutex.acquire()
                objeto = random.choice(productos)
                BODEGA.put(objeto)
                print("el productor: ",self.id," esta añadiendo producto a la bodega: ", objeto," tamaño de la bodega: ", BODEGA.qsize())
                mutex.release()
            
    def run(self):
        # print("productor: ",self.id, "tamaño:",BODEGA.qsize())
        self.producir()
       

def main():
    
    consumidores = []
    productores = []

    for i in range(CONSUMIDORES):
        consumidores.append(Consumidor(i))

    for j in range(PRODUCTORES):
        productores.append(Productor(j))

    for c in consumidores:
        c.start()

    for p in productores:
        p.start()
 

if __name__ == '__main__':
    
    main()

