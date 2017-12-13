import sqlite3
import os

db = sqlite3.connect('biblioteca.db')
cursor = db.cursor()

def creacion():
    return cursor.execute('''CREATE TABLE libro(ID INTEGER PRIMARY KEY,
    autor TEXT, titulo TEXT, publicacion TEXT)''')

def insertar():
    autor = input('Nombre del autor: ')
    libro = input('Nombre del libro: ')
    publicacion = input('Fecha de Publicación DD/MM/AA: ')
    cursor.execute('''INSERT INTO libro(autor,titulo,publicacion)
    VALUES(?,?,?)''',(autor,libro,publicacion))
    db.commit()

def eliminar():
    try:
        borrar = input('Borrar Autor por su ID:')
        cursor.execute('''DELETE FROM libro WHERE ID = ?''',(borrar))
        db.commit()
    except Exception as e:
        print(e)

def listar():
    os.system('clear')
    cursor.execute('''SELECT ID,autor,titulo FROM  libro''')
    resultado = cursor.fetchall()
    print('Autor    Titulo')
    for fila in resultado:
        print('{0}. {1}      {2}'.format(fila[0],fila[1],fila[2]))

def consulta():
    try:
        consul= input('Traer todos los resultados')
        cursor.execute('''SELECT * FROM libro WHERE autor like ?''',(consul))
        resultado = cursor.fetchall()
        for fila in resultado:
            print('{0}'.format(fila[0]))
    except Exception as e:
        print(e)

def menu():
    os.system('clear')
    numero = True
    while numero != False:
        numero = input('Menu \n1. Agregar\n2. Eliminar\n3. Listar'
                       '\n4. Consulta\n5 Salir \n-->')
        if numero == '1':
            insertar()

        elif numero == '2':
            eliminar()

        elif numero == '3':
            listar()

        elif numero == '4':
            consulta()

        elif numero == '5':
            numero = False

        else:
            print("Erro, Opción no valida")