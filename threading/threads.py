import threading

def hola_mundo():
    print("Hola mundo")

if __name__ == '__main__':

    thread = threading.Thread(target=hola_mundo)
    thread.start()
    
        # thread.daemon = True
        # thread.start()
        # print("Hola mundo")