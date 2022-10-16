from asyncore import write
import requests
import time
import concurrent.futures
import threading
import psycopg2

def service(url):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(get_service, url)
    
def get_service(url):
    response = requests.get(url)
    if response.status_code == 200 :
        data = response.json()
        # for dataout in data:
        #     print(dataout["title"])
        return data
    else:
        pass

def write_db(connection):
    cursor = connection.cursor()
    data = get_service()
    for dataout in data:
        query = f""" INSERT INTO public.titulos (title) VALUES ('{dataout["title"]}') """ 
    cursor.execute(query)
    connection.commit()

def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="203454",
            database="poke",
            port=5432
        )
        print("Conexión exitosa.")
        return connection
        

    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    



if __name__ == "__main__":
    init_time = time.time()
    url_site = ["https://jsonplaceholder.typicode.com/posts"]
    data = service(url_site)
    connection = connect_db()
    end_time = time.time() - init_time
    print(end_time)