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
