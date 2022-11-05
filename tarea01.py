# Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autores.
# Considerar que un libro puede tener varios autores.
# Se solicita escribir un programa en Python que permita registrar libros.

import pandas as pd
import csv

listaLibros = []

class Libro:
    def __init__(self, id, titulo, genero, isbn, editorial, autor):
        self.id        = id
        self.titulo    = titulo
        self.genero    = genero
        self.isbn      = isbn
        self.editorial = editorial
        self.autor     = autor
    def entregarDatos(self):
        print("{} - {} - {} - {} - {} - {}".format(self.id, self.titulo, self.genero, self.isbn, self.editorial, self.autor))
    
    def editarLibros(self, id, titulo, genero, isbn, editorial, autor):
        self.id        = id
        self.titulo    = titulo
        self.genero    = genero
        self.isbn      = isbn
        self.editorial = editorial
        self.autor     = autor
        print("Modificación Exitosa!")
    
    def __repr__(self):
        return "{0}:{1}".format(self.id, self.titulo)

def readFile():
    path0 = input("Ingrese la dirección relativa del archivo, ejm. (***.csv): ")
    df = pd.read_csv(path0,header=0)
    print("LEYENDO TU ARCHIVO CSV")
    print(df)
    for i in range(len(df)):
        info_book =[]
        for j in df:
            info = df.loc[i][j]
            info_book.append(info)
        book = Libro(info_book[0],info_book[1],info_book[2],info_book[3],info_book[4],info_book[5])
        listaLibros.append(book)
        
def registrarLibros():
    autores = []
    print("Registro de Libro\n")
    while True:
        try:
            id = int(input("Ingrese el id único: "))
            break
        except ValueError:
            print('Ingrese un entero por favor')
            continue
    titulo    = input("Ingrese el título: ")
    genero    = input("Ingrese el género: ")
    while True:
        try:
            isbn = int(input("Ingrese el ISBN (13 dígitos): "))
            break
        except ValueError:
            print('Ingrese correctamente el ISBN por favor')
            continue
    editorial = input("Ingrese la editorial: ")
    n_autor = int(input('Cantidad de autores: '))
    for i in range(n_autor):
        autor = input(f'Ingrese Autor {i+1}: ')
        autores.append(autor)

    libro0 = Libro(id, titulo, genero, isbn, editorial, autores)
    listaLibros.append(libro0)
  
def listadoLibros():
    print("Listado de Libros\n")
    print("ID | TÍTULO | GÉNERO | ISBN | EDITORIAL | AUTOR(ES)")
    for libro0 in listaLibros:
        libro0.entregarDatos()
def buscarLibros1():
    print("Buscar Libro\n")
    autor = input("Ingrese el autor a buscar: ")
    for libro0 in listaLibros:
        if autor in libro0.autor:
            libro0.entregarDatos()

def buscarLibros2():
    print("Buscar Libro\n")
    editorial = input("Ingrese la editorial a buscar: ")
    for libro0 in listaLibros:
        if editorial == libro0.editorial:
            libro0.entregarDatos()

def buscarLibros3():
    print("Buscar Libro\n")
    genero = input("Ingrese el genero a buscar: ")
    for libro0 in listaLibros:
        if genero == libro0.genero:
            libro0.entregarDatos()        

def buscarLibros4():
    print("Buscar Libro\n")
    isbn = int(input("Ingrese el ISBN a buscar: "))
    for libro0 in listaLibros:
        if isbn == libro0.isbn:
            libro0.entregarDatos()

def buscarLibros5():
    print("Buscar Libro\n")
    titulo = input("Ingrese el título a buscar: ")
    for libro0 in listaLibros:
        if titulo in libro0.titulo:
            libro0.entregarDatos()

def ordenarLibros():
    print('Ordenar Libros por Titulo')
    ordenar = sorted(listaLibros, key=lambda x: x.titulo)
    print(ordenar)