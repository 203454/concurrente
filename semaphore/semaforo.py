from asyncio import threads
from threading import Thread, Semaphore
from pytube import YouTube 

semaforo = Semaphore(1) #Crea la variable semáforo

# wait (s) Decrementa el valor de s si este es mayor que
# cero. Si s es igual a 0, el proceso se bloqueará en el semáforo

# signal(s) desbloquea algún proceso bloqueado en s, y en 
# el caso de que no haya ningún procesos incrementa el valor de s

def critico(id):
    urls = [
        'https://www.youtube.com/watch?v=ZnZqB5Z75zI&ab_channel=TopMovieClips',
        'https://www.youtube.com/watch?v=m6jfZa00vkY&ab_channel=IsmaelKrall',
        'https://www.youtube.com/watch?v=vn41-lpnjNM&ab_channel=WebZone',
        'https://www.youtube.com/watch?v=0I647GU3Jsc&ab_channel=ImagineDragonsVEVO',
        'https://www.youtube.com/watch?v=tjC3fjVcDjY&ab_channel=TomsMucenieks'
    ]
    global x;
    
    x = x + id
    # print("Hilo= " + str(id) + " =>"+str(x))

    download_videos(urls[id-1])

    x=1

def download_videos(urls):
        SAVE_PATH = "C:/Pyvideos/youtube" 
        try: 
            yt = YouTube(urls)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
            print("Downloading video...", urls)
        except: 
            print("Connection error in url: ",urls)
        
        print("videos donwloaded",urls)

class Hilo(Thread):
    
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire() #Inicializa semáforo, lo adquiere
        critico(self.id)
        semaforo.release() #Libera un semáforo e incrementa la variable semáforo


class Videos(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire() 
        critico(self.id)
        semaforo.release() 

threads_semaphore = [Videos(1),Videos(2),Videos(3),Videos(4),Videos(5)]

x=1

for t in threads_semaphore:
    t.start()