
jogadores = {
    "jogador_1":{
        "name": "",
        "escolha": ""
    },
    "jogador_2":{
        "name": "",
        "escolha": ""
    }
}


def inicia_jogadores():
    jogadores["jogador_1"]["name"] = str(input('Qual e seu nome? '))
    jogadores["jogador_2"]["name"] = str(input('Nome da pessoa que vai jogar com vc: '))
    jogadores["jogador_1"]["escolha"] = str(input(f'Qual você quer {jogadores["jogador_1"]["name"]}? [O/X] ')).upper()
    valida_escolha(jogadores["jogador_1"]["escolha"])
    if jogadores["jogador_1"]["escolha"] == "X":
        jogadores["jogador_2"]["escolha"] = "O"
    else:
        jogadores["jogador_2"]["escolha"] = "X"
    return jogadores

def valida_escolha(escolha):
    if escolha != "O" and escolha != "X":
        while jogadores["jogador_1"]["escolha"] != "O" and jogadores["jogador_1"]["escolha"] != "X":
            jogadores["jogador_1"]["escolha"] = str(input("ERRO: tente novamente, Qual você quer? [O/X] ")).upper()