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

def buscar_n_autores():
    print("Buscar Libro\n")
    numero = input("Ingrese Numero de autores: ")
    for libro0 in listaLibros:
        print(libro0.autor[0])
        # if numero == libro0.titulo:
        #     libro0.entregarDatos()

def modificarLibros():
    print("Modificar Libro\n")
    isbn = int(input("Ingrese el numero de ISBN a buscar: "))
    autores =[]
    for libro0 in listaLibros:
        if isbn == libro0.isbn:
          id        = int(input("Ingrese el id único: "))
          titulo    = input("Ingrese el título: ")
          genero    = input("Ingrese el género: ")
          isbn      = int(input("Ingrese el ISBN: "))
          editorial = input("Ingrese la editorial: ")
          n_autor = int(input('Cantidad de autores: '))
          for i in range(n_autor):
            autor = input(f'Ingrese Autor {i+1}: ')
            autores.append(autor)
          libro0.editarLibros(id, titulo, genero, isbn, editorial, autores)
          libro0.entregarDatos()
          
def deleteFile():
    whatDel = input('Ingrese el titulo del libro que desea eliminar: ')
    df = pd.read_csv('books.csv',index_col=['id'])
    A = df.drop(index=df[df['titulo']==whatDel].index)
    print("")

def guardar_csv():
    list_save_book = []
    file = open("books.csv", "w")
    file.close()
    atributos = [['ID', 'Titulo', 'Genero', 'ISBN', 'Editorial', 'Autores']]
    with open('books.csv','a',newline='') as file:
        write = csv.writer(file, delimiter=',')
        write.writerows(atributos)
    for libro in listaLibros:
        save_book = []
        save_book.append(libro.id)
        save_book.append(libro.titulo)
        save_book.append(libro.genero)
        save_book.append(libro.isbn)
        save_book.append(libro.editorial)
        save_book.append(libro.autor)
        list_save_book.append(save_book)
    with open('books.csv','a',newline='') as file:
            write = csv.writer(file, delimiter=',')
            write.writerows(list_save_book)
    print('Guardado Correctamente')
def main():
    while True:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|****************************|")
        print("")  
        print("Seleccione una de las siguientes opciones:");
        print("1.- Registrar Libro")
        print("2.- Listar libros ingresados")
        print("3.- Buscar libro por ISBN")
        print("4.- Buscar libro por título")
        print("5.- Buscar libro por autor")
        print("6.- Buscar libro por editorial")
        print("7.- Buscar libro por género")
        print("8.- Modificar libros ingresados")
        print("9.- Eliminar libro")
        print("10.- Ordenar Libros por Titulo")
        print("11.- Buscar por número de autores")
        print("12.- Guardar Cambios en el CSV")
        
        while True:
            try:
                opcion = int(input("Opcion: "))
                break
            except ValueError:
                print("Ingrese una opción válida: ")
                continue
             
        if opcion == 1:
            registrarLibros()
        elif opcion == 2:
            listadoLibros()
        elif opcion == 3:
            buscarLibros4()
        elif opcion == 4:
            buscarLibros5()
        elif opcion == 5:
            buscarLibros1()
        elif opcion == 6:
            buscarLibros2()
        elif opcion == 7:
            buscarLibros3()
        elif opcion == 8:
            modificarLibros()
        elif opcion == 9:
            deleteFile()
        elif opcion == 10:
            ordenarLibros()
        elif opcion == 11:
            buscar_n_autores()
        elif opcion == 12:
            guardar_csv()
                
if __name__ == '__main__':
    readFile()
    main()    