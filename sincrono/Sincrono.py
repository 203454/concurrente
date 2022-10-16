from urllib import response
import requests
import time
import psycopg2
import psycopg2.extras

def service():

    print("Hola Service")
    data = get_service()
    conn = connect_db()
    write_db(data, conn)

def get_service(url):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200 :
        data = response.json()
        return data
        # for dataout in data:
            # title = dataout["title"]
            # print(title)

    else:
        pass

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
    
    
def write_db(data,connection):
    cursor = connection.cursor()
    data = get_service()
    for dataout in data:
        query = f""" INSERT INTO public.titulos (title) VALUES ('{dataout["title"]}') """ 
    cursor.execute(query)
    connection.commit()

    for dataout in data:
            title = dataout["title"]
            print(title)




def create_table(connection):
    pass
  
if __name__ == "__main__":
    init_time = time.time()
    service()
    end_time = time.time() - init_time
    print(end_time)