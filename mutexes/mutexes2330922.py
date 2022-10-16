import threading
from pytube import YouTube 

mutex = threading.Lock()
def crito(id, url):
    global x;
    x = x + id
    print("HILO = "+ str(id)+ " => "+ str(x))
    x=1

def download_videos(id,url):
        SAVE_PATH = "C:/Pyvideos/youtubeMutexes" 
        try: 
            yt = YouTube(url)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
            print("Downloading video...", url)
        except: 
            print("Connection error in url: ",url ,"\n")
        
        print("videos donwloaded",url)


class Hilo(threading.Thread):
    
    def __init__(self, id, url):
        threading.Thread.__init__(self)
        self.id = id
        self.url = url

    def run(self):
        mutex.acquire()
        # crito(self.id, self.url)
        print("id: ", str(self.id),"\n url: ",self.url)
        download_videos(self.id,self.url)
        mutex.release()


urls = [
        'https://www.youtube.com/watch?v=ZnZqB5Z75zI&ab_channel=TopMovieClips',
        'https://www.youtube.com/watch?v=m6jfZa00vkY&ab_channel=IsmaelKrall',
        'https://www.youtube.com/watch?v=vn41-lpnjNM&ab_channel=WebZone',
        'https://www.youtube.com/watch?v=0I647GU3Jsc&ab_channel=ImagineDragonsVEVO',
        'https://www.youtube.com/watch?v=tjC3fjVcDjY&ab_channel=TomsMucenieks'
    ]

# hilos = [Hilo(1,urls[0]), Hilo(2,urls[0]), Hilo(3,urls[0])]
hilos=[]
for i in range(0,len(urls)):
    hilos.append(Hilo(i,urls[i]))

x = 1

for h in hilos:
    h.start()
