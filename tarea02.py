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