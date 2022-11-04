# Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autores.
# Considerar que un libro puede tener varios autores.
# Se solicita escribir un programa en Python que permita registrar libros.
import pandas as pd
import csv
from random import randint
class Libro:
    def __init__(self,id, titulo, genero, ISBN, editorial, autor_es):
        self.id=id
        self.titulo=titulo
        self.genero=genero
        self.ISBN=ISBN
        self.editorial=editorial
        self.autor_es=autor_es

    #ingresa datos a modificar
    def input_UpDate():
        list_data=[]
        print(Libro.List_books())
        code_item=input('Ingrese codigo del libro a editar: ')
        df1=pd.read_csv('librosbd.csv')
        check=code_item in df1.values
        while not(check):
            code_item=input('Ingrese código valido: ')
            check=code_item in df1.values
        field_edit=input('Ingrese campo a editar (titulo, genero, ISBN, editorial o autores): ')
        while field_edit not in ('titulo', 'genero', 'ISBN', 'editorial','autores'):
            field_edit=input('Ingrese campo válido: ')
        atributos = ['titulo','genero','ISBN','editorial']
        new_line=''
        for atributo in atributos :
            if field_edit==atributo:
                new_line = input(f'Ingrese {atributo}:')
                break
        if field_edit=='autores':
            len_authors=int(input('Ingrese cantidad de autores: '))
            new_line=[ input(f"Ingrese autor {str(i+1)} : ") for i in range(len_authors)]
        list_data.append(code_item)
        list_data.append(field_edit)
        list_data.append(str(new_line))    
        return list_data

    #actualizar datos
    def BookUpDate(code_item,field_edit,new_line):
        print('      ACTUALIZAR DATOS       ')
        try:
            df=pd.read_csv('librosbd.csv', index_col=0)
            df.loc[code_item, field_edit]=new_line
            df.to_csv('librosbd.csv')
            print(df)
        except Exception as ex :
            print(ex, 'Ocurrio un problema')
            Libro.menu()
                
    def question():
        rpt=input('Presione M si desea regresar al menu principal ').upper()
        if rpt=='M':
            return Libro.menu()
