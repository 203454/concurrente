from os import link
import requests
import threading
from pytube import YouTube 
import threading
import concurrent.futures
import psycopg2

def write_db(data):
    connection = connect_db()
    cursor = connection.cursor()
    for dataout in data:
        # print("data to insert",dataout)
        query = f""" INSERT INTO public.names (name) VALUES ('{dataout}') """ 
        cursor.execute(query)
        connection.commit()

    print("insert completed successfully")

def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="203454",
            database="concurrente",
            port=5432
        )
        print("Conexión exitosa.")
        return connection
        
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    
def service_dyt(urls): 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_videos,urls)

def download_videos(urls):       
    SAVE_PATH = "C:/Pyvideos/youtube" 
    try: 
        yt = YouTube(urls)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(SAVE_PATH)
        print("Downloading video...", urls)
    except: 
        print("Connection error in url: ",urls)  

def get_servicesToWrite(url_site):
    data = []
    response = requests.get(url_site)
    if response.status_code == 200:
        results = response.json().get('results')
        for x in range(0,len(results)):                
            data.append(results[x].get('name').get('first'))
    else: 
        print("error: ", response.status_code)

    write_db(data)
    

def get_servicesIterable(url):
    # print(f'Dato={dato}')
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
    # else:
    #     print("error: ", response.status_code)
  

if __name__ == '__main__':

    
    urls = [
        'https://www.youtube.com/watch?v=ZnZqB5Z75zI&ab_channel=TopMovieClips',
        'https://www.youtube.com/watch?v=m6jfZa00vkY&ab_channel=IsmaelKrall',
        'https://www.youtube.com/watch?v=vn41-lpnjNM&ab_channel=WebZone',
        'https://www.youtube.com/watch?v=0I647GU3Jsc&ab_channel=ImagineDragonsVEVO',
        'https://www.youtube.com/watch?v=tjC3fjVcDjY&ab_channel=TomsMucenieks'

    ]

    url_site = "https://randomuser.me/api/?results=2000&inc=name"

    url = "https://randomuser.me/api/"
    
    print("Starting to connect to download videos...")
    th1 = threading.Thread(target=service_dyt,args=[urls])
    print("Starting to connect to insert data...")
    th2 = threading.Thread(target=get_servicesToWrite,args=[url_site])
    th1.start()
    th2.start()
    
    print("Starting to connect to iter data")
    for x in range(0,50):
        th3 = threading.Thread(target=get_servicesIterable,args=[url])
        th3.start()

