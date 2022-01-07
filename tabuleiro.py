import os

tabuleiro = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]


def mostra_tabuleiro():
    print(f"{tabuleiro[0]}\n{tabuleiro[1]}\n{tabuleiro[2]}")

def atualiza_tabuleiro(caracter):
    coluna = int(input('Em qual coluna você quer? '))-1
    linha = int(input('Em qual linha você quer? '))-1
    if tabuleiro[linha][coluna] == "-":
        tabuleiro[linha][coluna] = caracter
    else:
        print("Esse campo ja escolhido")
        atualiza_tabuleiro(caracter)
    os.system("cls||clear")

def tem_vencedor(jogador, caracter):
    if tabuleiro[0][0] == caracter and tabuleiro[1][0] == caracter and tabuleiro[2][0] == caracter or tabuleiro[0][1] == caracter and tabuleiro[1][1] == caracter and tabuleiro[2][1] == caracter or tabuleiro[0][2] == caracter and tabuleiro[1][2] == caracter and tabuleiro[2][2] == caracter or tabuleiro[0][0] == caracter and tabuleiro[0][1] == caracter and tabuleiro[0][2] == caracter or tabuleiro[1][0] == caracter and tabuleiro[1][1] == caracter and tabuleiro[1][2] == caracter or tabuleiro[2][0] == caracter and tabuleiro[2][1] == caracter and tabuleiro[2][2] == caracter or tabuleiro[0][2] == caracter and tabuleiro[1][1] == caracter and tabuleiro[2][0] == caracter or tabuleiro[0][0] == caracter and tabuleiro[1][1] == caracter and tabuleiro[2][2] == caracter:
        print(f'\033[33m{jogador["name"].upper()} GANHOU!\033[m')
        mostra_tabuleiro()
        return True
    else:
        return False

