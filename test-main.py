"""
Kolorado test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

body = {
    "trainer_token": "b32fdc06b2ffb502ed653b181e832a5a",
    "email": "julia-s-amazing@yandex.ru",
    "password": "Pokemon_battle123"
}

response = requests.post(url=f'{URL}/trainers/reg', json=body, headers=HEADER, timeout=5)
print(f'status code: {response.status_code}. Message:{response.json()["message"]}')

response = requests.get(url=f'{URL}/trainers', params={'level':1})
print(f'Status code: {response.status_code}.')


def test_create_a_pokemon():
        URL = 'https://api.pokemonbattle.me:9104'
        HEADER = {'Content-Type': 'application/json'}

        endpoint = "/pokemons"
        data = {
        "name": "Carry",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    }
        
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print("Create Pokemon Response:")
print(response.json())

def rename_pokemon():
    endpoint = "/pokemons"
    data = {
        "old_name": "Carry",
        "new_name": "Love"
    }
    response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER,)
    print("Rename Pokemon Response:")
    print(response.json())

def catch_pokemon():
    endpoint = "/trainers/add_pokeball"
    data = {
        "trainer_name": "Lion",
        "pokemon_name": "Love"
    }
    response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER,)
    print("Catch Pokemon Response:")
    print(response.json())

# Выполнение запросов
if __name__ == "__main__":
    create_pokemon()
    rename_pokemon()
    catch_pokemon()

