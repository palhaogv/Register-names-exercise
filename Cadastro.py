import pandas as pd
import os.path


try:
    os.path.isfile('Primeira_Planilha.xlsx') == True
    df = pd.read_excel('Primeira_Planilha.xlsx', usecols=['Jogador', 'Gols', 'Cartões', 'Faltas'])
    print(df)

    lista_jogador = []
    

    while True:
        jogador = str(input('Qual o nome do jogador? '))
        gols = int(input('Quantos gols? '))
        cartoes = int(input('Quantos cartões? '))
        faltas = int(input('Quantas faltas? '))
        lista_jogador.append(jogador)
        lista_jogador.append(gols)
        lista_jogador.append(cartoes)
        lista_jogador.append(faltas)
        df.loc[len(df)] = lista_jogador[:]
        lista_jogador.clear()
        continuacao = str(input('Deseja cadastrar mais jogadores [S/N]? ')).upper().strip()
        if continuacao == 'N':
            break
    print(df)
    df.to_excel('Primeira_Planilha.xlsx', sheet_name='Premierleague')

except:
    lista_jogador = []
    lista_partida = []

    while True:
        jogador = str(input('Qual o nome do jogador? '))
        gols = int(input('Quantos gols? '))
        cartoes = int(input('Quantos cartões? '))
        faltas = int(input('Quantas faltas? '))
        lista_jogador.append(jogador)
        lista_jogador.append(gols)
        lista_jogador.append(cartoes)
        lista_jogador.append(faltas)
        lista_partida.append(lista_jogador[:])
        lista_jogador.clear()
        continuacao = str(input('Deseja cadastrar mais jogadores [S/N]? ')).upper().strip()
        if continuacao == 'N':
            break
    df = pd.DataFrame(lista_partida)
    df.columns = ['Jogador', 'Gols', 'Cartões', 'Faltas']
    print(df)
    df.to_excel('Primeira_Planilha.xlsx', sheet_name='Premierleague')  # verificar se esse comando é no começo ou no final


