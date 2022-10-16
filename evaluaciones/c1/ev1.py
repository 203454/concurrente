from tabnanny import check
import threading
import time

mutex = threading.Lock()
def comer(id):

    global palillo;
    global personas;

    if(id % 2 == 0 ):
        print("Ahora estas comiendo",id, " y hay en espera: ",palillo-2, " palillos")
        print("comiendo...")        
        personas = personas - 1
        print("Aun no han comido", personas, " personas")
    else:
        print("Tu no estas comiendo, estas esperando",id)

def intercambiar(id):
    global personas;
    if(id % 2 != 0 ):
        print("Ahora estas comiendo",id, " y hay en espera: ",palillo-2, " palillos")
        print("comiendo...")        
        personas = personas - 1
        print("Aun no han comido", personas, " personas")
    else:
        print("Tu has comido",id)    



class Hilo(threading.Thread):

     def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

     def run(self):
        mutex.acquire() #Inicializa semáforo , lo adquiere
        # crito(self.id,self.palillo)
        
            
        # print("HILO_ID: ",self.id)
        
        comer(self.id)
        intercambiar(self.id)
        time.sleep(3)
        print("..............................................................")
        # intercambio(self.id)
        mutex.release() #Libera un semáforo e incrementa la varibale






if __name__ == '__main__':

    hilos=[Hilo(2), Hilo(4), Hilo(6),Hilo(8), Hilo(1), Hilo(3),Hilo(6), Hilo(7)]
    # for i in range(0,8):
    #     hilos.append(Hilo(i+1))
    palillo = 8
    personas = len(hilos)
    for h in hilos:
        h.start()


    # print(len(hilos))