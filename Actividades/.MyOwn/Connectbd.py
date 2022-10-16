
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

def read_txt(file):
    data = []
    with open(file) as f:
        for linea in f:
            data.append(linea)
            # print(linea)
        return data

if __name__ == '__main__':
    file = "D:/Usuarios/eduar/Desktop/nombres.txt"
    data = read_txt(file) 

    write_db(data)
