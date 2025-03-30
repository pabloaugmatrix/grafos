def resultado(instancia , dimensao):
    print("Instancia:", instancia)
    print("Linhas:", dimensao[0])
    print("Colunas:", dimensao[1])
    with open('resultado.txt', 'w') as arquivo:
        arquivo.write(f'Instancia: {instancia}\n')
        arquivo.write(f'Linhas: {dimensao[0]}\n')
        arquivo.write(f'Colunas: {dimensao[1]}\n')
