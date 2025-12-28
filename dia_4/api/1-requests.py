import requests
from tabulate import tabulate
import mysql.connector


URL = 'https://randomuser.me/api/?nat=es&results=100'

response = requests.get(URL)

if response.status_code == 200:
    print('Conexion API exitosa')
    data = response.json()
    rows = []
    for dic_user in data['results']:
        nombre = dic_user['name']['first'] + ' ' + dic_user['name']['last']
        pais =  dic_user['location']['country']
        email = dic_user['email']
        telefono = dic_user['phone']
        foto = dic_user['picture']['large']
        rows.append([nombre, pais, email, telefono, foto])
    
    headers = ['Nombre','País','Email','Telefono', 'Foto']
    print(tabulate(rows,headers,tablefmt='grid'))
    
    #CARGAMOS DATA EN DB
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'db_g6'    
    )
    if connection.is_connected():
        cursor = connection.cursor()
        
        cursor.execute("DROP TABLE IF EXISTS usuario")
        
        cursor.execute(
            """
            CREATE TABLE IF NOT exists usuario(
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nombre VARCHAR(225) not null,
            pais VARCHAR(225) not null,
            email varchar(225),
            telefono varchar(100),
            foto TEXT
            );
            """
        )
    #INSERTAMOS LOS USUARIOS A LA BD
        for usuario in rows:
            cursor.execute(
                """
                insert into usuario (nombre, pais, email, telefono, foto)
                values(%s,%s,%s,%s,%s)
                """,
                usuario
            )
        connection.commit()
        connection.close()
        print('Registros importados a la BD')
    else:
        print('Error al interntar conectarse a la BD')
else:
    print(f'error{response.status_code}')