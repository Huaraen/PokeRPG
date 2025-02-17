import json

with open('PokeRPG/dex.json', 'r') as file:
    data = json.load(file)
    pokemons = data["pokemons"]


import requests
from bs4 import BeautifulSoup

# URL da página da Lista de Pokémon na Wiki PokeXGames
url = 'https://wiki.pokexgames.com/index.php/Pok%C3%A9mon'

# Falsificando o User-Agent para simular um navegador real
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encontrando os elementos que contêm os nomes dos Pokémon
    pokemon_names = soup.find_all(class_='mw-headline')
    
    # Loop para exibir os nomes dos Pokémon
    for name in pokemon_names:
        print(name.text)
else:
    print(f"Erro ao fazer a requisição. Código de status: {response.status_code}")



