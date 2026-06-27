# How to connect to an API using python 

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:             # 200 is http response code meaning ok (eg 404 means error)
        pokemon_data = response.json()          # converts the data in python dic
        return pokemon_data
    else:
        print(f"Failed to retreive data {response.status_code}")





pokemon_name = "charizard"
pokemon_info = get_pokemon(pokemon_name)  

if pokemon_info:
    print(f"Name = {pokemon_info["name"]}")
    print(f"ID = {pokemon_info["id"]}")
    print(f"Height = {pokemon_info["height"]}")
    print(f"Weight = {pokemon_info["weight"]}")