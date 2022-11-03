# Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autores.
# Considerar que un libro puede tener varios autores.
# Se solicita escribir un programa en Python que permita registrar libros.

#Método y función para buscar libro por ISBN

listaLib = []

class Libro:
    def __init__(self,id,titulo,genero,ISBN,editorial,*autores):
        self.id        = id
        self.titulo    = titulo
        self.genero    = genero
        self.ISBN      = ISBN
        self.editorial = editorial
        self.autores   = autores
    def giveData(self):
        print(f'ID      TÍTULO   GÉNERO   ISBN   EDITORIAL   AUTOR(ES)')
        return f'{self.id} - {self.titulo} - {self.genero} - {self.ISBN} - {self.editorial} - {self.autores}'
  
    libro_0=[]

def buscarLibro():
    print("Buscar Libro por el ISBN o Título\n")
    ISBN = int("Ingrese el numero de cedula a buscar: ")
    for libro_0 in listaLib:
        if ISBN == libro_0.isbn:
            libro_0.giveData()