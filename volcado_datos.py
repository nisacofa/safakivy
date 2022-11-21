import mysql.connector as bbdd
from web_scrapping import *
def insertar_datos():
    lista_zapatos = web_scra()
    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="zapatos",
                            user="root",
                            password="1111",
                            autocommit=True)
    cursor = conexion.cursor()
    cursor.execute("delete from zapato where id is not null")
    cursor.execute("alter table zapato auto_increment=1")
    script_insert="insert into zapato(marca, modelo, precio, genero)" \
                  "values (%s, %s, %s, %s)"
    for zap in lista_zapatos:
        cursor.execute(script_insert, (zap["marca"],
                       zap["modelo"],
                       zap["precio"],
                       zap["genero"]))
    print("Datos insertados correctamente")

def consultar_datos():
    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="zapatos",
                            user="root",
                            password="1111",
                            autocommit=True)

    lista_zapatos = []

    cursor = conexion.cursor()

    consulta = "select * from zapato"

    cursor.execute(consulta)

    for dato in cursor.fetchall():
        zapato = tuple([dato[0],dato[3],dato[1],dato[4],dato[5]])
        lista_zapatos.append(zapato)

    return lista_zapatos
