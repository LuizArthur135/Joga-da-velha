import define_jogadores
import tabuleiro

jogadores = define_jogadores.inicia_jogadores()
while True:
    print(f'\033[33mVEZ DE {jogadores["jogador_1"]["name"]}\033[m')
    tabuleiro.mostra_tabuleiro()
    tabuleiro.atualiza_tabuleiro(jogadores["jogador_1"]["escolha"])
    if tabuleiro.tem_vencedor(jogadores["jogador_1"],jogadores["jogador_1"]["escolha"]):
        break
    print(f'\033[33mVEZ DE {jogadores["jogador_2"]["name"]}\033[m') 
    tabuleiro.mostra_tabuleiro()
    tabuleiro.atualiza_tabuleiro(jogadores["jogador_2"]["escolha"])
    if tabuleiro.tem_vencedor(jogadores["jogador_2"],jogadores["jogador_2"]["escolha"]):
        break
