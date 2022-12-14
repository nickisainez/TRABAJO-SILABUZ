# La tarea gira en torno a la PokeAPI: https://pokeapi.co/docs/v2
# Utilizar la API v2 y el paquete requests de Python.
import requests
import json
pokeapi_url = "https://pokeapi.co/api/v2/"
var         = "generation/"
poke        = "pokemon/"

#Funcion para listar Pokemon: Nombre, Habilidades y URL imagen
def printPokemon(response):
    for name_pokemon in response['pokemon_species']:
        nombre = name_pokemon['name']
        responseAux = requests.get(pokeapi_url+ poke + nombre)
        if responseAux.status_code == 200:
            response = requests.get(pokeapi_url+ poke + nombre).json()
            abilities = [i['ability']['name'] for i in response['abilities']]
            img = response['sprites']['front_default']
            if img == None:
                img = 'Imágen no disponible por el momento.'
            print("-------------------------------------------------------------------------------------------------")
            print(f'Nombre      : {nombre}')
            print(f'Habilidades : {abilities}')
            print(f'URL Imágen  : {img}')

    print("-------------------------------------------------------------------------------------------------\n")

def print_pokemon_tipo_habilidad(response):
    for name_pokemon in response['pokemon']:
        nombre = name_pokemon['pokemon']['name']
        responseAux4 = requests.get(pokeapi_url+ poke + nombre)
        if responseAux4.status_code == 200:
            response = requests.get(pokeapi_url+ poke + nombre).json()
            abilities = [i['ability']['name'] for i in response['abilities']]
            img = response['sprites']['front_default']
            if img == None:
                img = 'Imágen no disponible por el momento.'
            print("-------------------------------------------------------------------------------------------------")
            print(f'Nombre      : {nombre}')
            print(f'Habilidades : {abilities}')
            print(f'URL Imágen  : {img}')

    print("-------------------------------------------------------------------------------------------------\n")
    
#Listar Pokemon por Generaciones
def genPok():
    print("-----------------------------------------------------")
    print("| Número a ingresar respecto a la gen. de pokemones |")
    print("-----------------------------------------------------")
    print("|           Generación I   : 1                      |")
    print("|           Generación II  : 2                      |")
    print("|           Generación III : 3                      |")
    print("|           Generación IV  : 4                      |")
    print("|           Generación V   : 5                      |")
    print("|           Generación VI  : 6                      |")
    print("|           Generación VII : 7                      |")
    print("|           Generación VII : 8                      |")
    print("-----------------------------------------------------\n")
    numbers     =[i for i in range(1,9)]

    while True:
        try:
            genP = int(input("Ingrese el número de generación: "))
        except ValueError:
            print("Ingrese el número de generación correctamente")
            continue
        if genP not in numbers:
            print("Ingrese el número de generación correctamente")
            continue
        break

    responseGen = requests.get(pokeapi_url+var+str(genP)).json()
    printPokemon(responseGen)

# Listar pokemon por forma
def shapePok():
    print("-----------------------------------------------------")
    print("| Número a ingresar respecto a la forma del pokemon |")
    print("-----------------------------------------------------")
    print("|           Ball          : 1                       |")
    print("|           Squiggle      : 2                       |")
    print("|           Fish          : 3                       |")
    print("|           Arms          : 4                       |")
    print("|           Blob          : 5                       |")
    print("|           Upright       : 6                       |")
    print("|           Legs          : 7                       |")
    print("|           Quadruped     : 8                       |")
    print("|           Wings         : 9                       |")
    print("|           Tentacles     : 10                      |")
    print("|           Heads         : 11                      |")
    print("|           Humanoid      : 12                      |")
    print("|           Bug-wings     : 13                      |")
    print("|           Armor         : 14                      |")
    print("-----------------------------------------------------\n")

    pokeapi_url = "https://pokeapi.co/api/v2/"
    var         = "pokemon-shape/"
    poke        = "pokemon/"
    numbers     =[i for i in range(1,15)]

    while True:
        try:
            shaP = int(input("Ingrese el número de forma del pokemon: "))
        except ValueError:
            print("Ingrese el número de forma del pokemon correctamente")
            continue
        if shaP not in numbers:
            print("Ingrese el número de forma del pokemon correctamente")
            continue
        break

    responseSha = requests.get(pokeapi_url+var+str(shaP)).json()
    printPokemon(responseSha)
# Listar Pokemon por habilidades
def abilitPoke():
    print("-----------------------------------------------------")
    print("| Número a ingresar respecto a la habilidad del pok |")
    print("-----------------------------------------------------")
    print("|           Stench          : 1                     |")
    print("|           Drizzle         : 2                     |")
    print("|           Speed-boost     : 3                     |")
    print("|           Battle-armor    : 4                     |")
    print("|           Sturdy          : 5                     |")
    print("|           Damp            : 6                     |")
    print("|           Limber          : 7                     |")
    print("|           Sand-veil       : 8                     |")
    print("|           Static          : 9                     |")
    print("|           Volt-absorb     : 10                    |")
    print("|           Water-absorb    : 11                    |")
    print("|           Oblivious       : 12                    |")
    print("|           Cloud-nine      : 13                    |")
    print("|           Compound-eyes   : 14                    |")
    print("|           Insomnia        : 15                    |")
    print("|           Color-change    : 16                    |")
    print("|           Immunity        : 17                    |")
    print("|           Flash-fire      : 18                    |")
    print("|           Shield-dust     : 19                    |")
    print("|           Own-tempo       : 20                    |")
    print("-----------------------------------------------------\n")

    var         = "ability/"
    numbers     =[i for i in range(1,21)]

    while True:
        try:
            abilP = int(input("Ingrese el número de habilidad del pokemon: "))
        except ValueError:
            print("Ingrese el número de habilidad del pokemon correctamente")
            continue
        if abilP not in numbers:
            print("Ingrese el número de habilidad del pokemon correctamente")
            continue
        break
    responseHabil = requests.get(pokeapi_url+var+str(abilP)).json()
    print_pokemon_tipo_habilidad(responseHabil)
# Listar pokemon por habitad
def habPok():
    print("-----------------------------------------------------")
    print("| Número a ingresar respecto al hábitat del pokemon |")
    print("-----------------------------------------------------")
    print("|           Cave          : 1                       |")
    print("|           Forest        : 2                       |")
    print("|           Grassland     : 3                       |")
    print("|           Mountain      : 4                       |")
    print("|           Rare          : 5                       |")
    print("|           Rough-terrain : 6                       |")
    print("|           Sea           : 7                       |")
    print("|           Urban         : 8                       |")
    print("|           Waters-edge   : 9                       |")
    print("-----------------------------------------------------\n")

    var         = "pokemon-habitat/"
    numbers     =[i for i in range(1,10)]

    while True:
        try:
            habP = int(input("Ingrese el número de hábitat del pokemon: "))
        except ValueError:
            print("Ingrese el número de hábitat del pokemon correctamente")
            continue
        if habP not in numbers:
            print("Ingrese el número de hábitat del pokemon correctamente")
            continue
        break

    responseHab = requests.get(pokeapi_url+var+str(habP)).json()
    printPokemon(responseHab)

# Listar Pokemon por tipo
def typePok():
    print("-----------------------------------------------------")
    print("|  Número para ingresar respecto al tipo de pokemon |")
    print("-----------------------------------------------------")
    print("|                 Normal   : 1                      |")
    print("|                 Fighting : 2                      |")
    print("|                 Flying   : 3                      |")
    print("|                 Poison   : 4                      |")
    print("|                 Ground   : 5                      |")
    print("|                 Rock     : 6                      |")
    print("|                 Bug      : 7                      |")
    print("|                 Ghost    : 8                      |")
    print("|                 Steel    : 9                      |")
    print("|                 Fire     : 10                     |")
    print("|                 Water    : 11                     |")
    print("|                 Grass    : 12                     |")
    print("|                 Electric : 13                     |")
    print("|                 Psychic  : 14                     |")
    print("|                 Ice      : 15                     |")
    print("|                 Dragon   : 16                     |")
    print("|                 Dark     : 17                     |")
    print("|                 Fairy    : 18                     |")
    print("-----------------------------------------------------\n")

    var         = "type/"
    numbers     =[i for i in range(1,19)]

    while True:
        try:
            typeP = int(input("Ingrese el número del tipo de pokemon: "))
        except ValueError:
            print("Ingrese el número del tipo de pokemon correctamente")
            continue
        if typeP not in numbers:
            print("Ingrese el número del tipo de pokemon correctamente")
            continue
        break

    responseType = requests.get(pokeapi_url+var+str(typeP)).json()
    print_pokemon_tipo_habilidad(responseType)

# Menu de la APP
def main():
    print("\n")
    print("|****************************|")
    print("|**|      Bienvenido(a)   |**|")
    print("|**|         Menu         |**|")
    print("|****************************|")
    print("")
    print("Seleccione una de las siguientes opciones:")
    print("1.- Listar pokemones por generación")
    print("2.- Listar pokemones por forma")
    print("3.- Listar pokemones por habilidad")
    print("4.- Listar pokemones por habitat")
    print("5.- Listar pokemones por tipo\n")

    numbersOp = [i for i in range(1,6)]
    while True:
        try:
            opcion = int(input('Ingrese una opción: '))
        except ValueError:
            print("Ingrese la opción correctamente")
            continue
        if opcion not in numbersOp:
            print("Ingrese la opción correctamente")
            continue
        break

    if opcion == 1:
        genPok()
    if opcion == 2:
        shapePok()
    if opcion == 3:
        abilitPoke()
    if opcion == 4:
        habPok()
    elif opcion == 5:
        typePok()

    againU = input('¿Desea realizar otra consulta? (Tipee "Si" para ello o cualquier tecla para finalizar): ').lower()
    if againU == 'si':
        main()

if __name__ == '__main__':
    main()