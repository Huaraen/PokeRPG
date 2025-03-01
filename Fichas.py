import csv

def criar_ficha_pokemon():
    return {
        'Status': [0, 0, 0, 0, 0, 0],  # HP, ATK, DEF, SP ATK, SP DEF, SPD
        'Nome': '',
        'Tipo': '',
        'Peso': 0.0,
        'Altura': 0.0,
        'Sexo': '',
        'Natureza': '',
        'Habilidade': '',
        'Movimento01': '',
        'Movimento02': '',
        'Movimento03': '',
        'Movimento04': ''
    }

def salvar_ficha_pokemon(ficha, csv_file):
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=ficha.keys())
        writer.writerow(ficha)

def carregar_fichas_pokemon(csv_file):
    fichas = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            fichas.append(row)
    return fichas

def editar_ficha_pokemon(ficha):
    print("Digite os novos valores (deixe em branco para manter o valor atual):")
    for chave, valor in ficha.items():
        novo_valor = input(f"{chave}: ({valor}) ")
        if novo_valor:
            if chave == 'Status':
                ficha[chave] = list(map(int, novo_valor.split(',')))
            elif chave == 'Peso' or chave == 'Altura':
                ficha[chave] = float(novo_valor)
            else:
                ficha[chave] = novo_valor

def main():
    csv_file = 'pokemons.csv'

    while True:
        print("\n1. Criar nova ficha de Pokémon")
        print("2. Visualizar fichas de Pokémon")
        print("3. Sair")
        escolha = input("Escolha uma opção (1/2/3): ")

        if escolha == '1':
            nova_ficha = criar_ficha_pokemon()
            editar_ficha_pokemon(nova_ficha)
            salvar_ficha_pokemon(nova_ficha, csv_file)
            print("Ficha de Pokémon criada e salva com sucesso!")
        elif escolha == '2':
            fichas = carregar_fichas_pokemon(csv_file)
            for idx, ficha in enumerate(fichas, start=1):
                print(f"\nFicha de Pokémon #{idx}:")
                for chave, valor in ficha.items():
                    print(f"{chave}: {valor}")
            if not fichas:
                print("Nenhuma ficha de Pokémon encontrada.")
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
