import requests

def obter_regioes():
    url = "https://pokeapi.co/api/v2/region/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        regioes = [regiao['name'] for regiao in data['results']]
        return regioes
    else:
        print("Erro ao obter regiões:", response.status_code)
        return []

def obter_pokemons_por_regiao(regiao):
    url = f"https://pokeapi.co/api/v2/region/{regiao}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemons = []
        for area in data['locations']:
            response_area = requests.get(area['url'])
            if response_area.status_code == 200:
                data_area = response_area.json()
                for pokemon in data_area['pokemon_encounters']:
                    pokemons.append({'name': pokemon['pokemon']['name'], 'types': pokemon['pokemon']['types']})
        return pokemons
    else:
        print("Erro ao obter Pokémon por região:", response.status_code)
        return []

def obter_detalhes_pokemon(nome_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}/"
    response = requests.get(url)
    if response.status_code == 200:
        detalhes = response.json()
        print(f"Detalhes de {nome_pokemon}:")
        print("Nome:", detalhes['name'])
        print("Tipos:", [tipo['type']['name'] for tipo in detalhes['types']])
        print("Altura:", detalhes['height'])
        print("Peso:", detalhes['weight'])
        print("Habilidades:", [habilidade['ability']['name'] for habilidade in detalhes['abilities']])
        print("Stats:")
        for stat in detalhes['stats']:
            print("-", stat['stat']['name'], ":", stat['base_stat'])
    else:
        print("Erro ao obter detalhes do Pokémon:", response.status_code)

def main():
    print("Lista de regiões disponíveis:")
    regioes = obter_regioes()
    for idx, regiao in enumerate(regioes, start=1):
        print(f"{idx}. {regiao}")

    escolha_regiao = input("\nEscolha uma região (digite o número correspondente): ")
    try:
        escolha_regiao = int(escolha_regiao)
        regiao_escolhida = regioes[escolha_regiao - 1]
        print(f"\nPokémons da região {regiao_escolhida}:")
        pokemons_regiao = obter_pokemons_por_regiao(regiao_escolhida)
        for pokemon in pokemons_regiao:
            print(f"Nome: {pokemon['name']}, Tipos: {', '.join([tipo['type']['name'] for tipo in pokemon['types']])}")

        escolha_pokemon = input("\nDigite o nome de um Pokémon para ver seus detalhes: ")
        obter_detalhes_pokemon(escolha_pokemon.lower())
    except (ValueError, IndexError):
        print("Escolha inválida.")

if __name__ == "__main__":
    main()






