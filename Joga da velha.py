seu_nome = str(input('Qual e seu nome? '))
outro_nome = str(input('Nome da pessoa que vai jogar com vc: '))
tabuleiro = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]
sim = str(input(f'Qual você quer {seu_nome}? [O/X] ')).upper()
if sim != 'O' and sim != 'X':
    sim = str(input('ERRO: tente novamente, Qual você quer? [O/X] ')).upper()
    while sim != 'O' and sim != 'X':
        sim = str(input('ERRO: tente novamente, Qual você quer? [O/X] ')).upper()
while True:
    print(f'\033[33mVEZ DE {seu_nome.upper()}\033[m')
    for linha in tabuleiro:
        print(f'{linha}')
    column = int(input('Em qual coluna você quer? '))-1
    row = int(input('Em qual linha você quer? '))-1
    tabuleiro[column][row] = sim
    for linha in tabuleiro:
        print(f'{linha}')
    if tabuleiro[0][0]  == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][2] == 'X' or tabuleiro[1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][2] == 'X' or tabuleiro[2][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[2][2] == 'X' or tabuleiro[0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][2] == 'O' or tabuleiro[1][0] == 'O' and tabuleiro[1][1] and tabuleiro[1][2] == 'O' or tabuleiro[2][0] and tabuleiro[2][1] and tabuleiro[2][2] == 'O' or tabuleiro[0][0] and tabuleiro[1][0] and tabuleiro[2][0] == 'X' or tabuleiro[0][1] and tabuleiro[1][1] and tabuleiro[1][2] == 'X' or tabuleiro[0][2] and tabuleiro[1][2] and tabuleiro[2][2] == 'X':
        print('PARABÉNS VOCÊ GANHOU')
        break
    print(f'\033[33mVEZ DE {outro_nome.upper()}\033[m')  
    for linha in tabuleiro:
        print(f'{linha}')
    column = int(input('Em qual coluna você quer? '))-1
    row = int(input('Em qual linha você quer? '))-1
    if tabuleiro[0][0] and tabuleiro[0][1] and tabuleiro[0][2] == 'X' or tabuleiro[1][0] and tabuleiro[1][1] and tabuleiro[1][2] == 'X' or tabuleiro[2][0] and tabuleiro[2][1] and tabuleiro[2][2] == 'X' or tabuleiro[0][0] and tabuleiro[0][1] and tabuleiro[0][2] == 'O' or tabuleiro[1][0] and tabuleiro[1][1] and tabuleiro[1][2] == 'O' or tabuleiro[2][0] and tabuleiro[2][1] and tabuleiro[2][2] == 'O' or tabuleiro[0][0] and tabuleiro[1][0] and tabuleiro[2][0] == 'X' or tabuleiro[0][1] and tabuleiro[1][1] and tabuleiro[1][2] == 'X' or tabuleiro[0][2] and tabuleiro[1][2] and tabuleiro[2][2] == 'X':
        print('PARABÉNS VOCÊ GANHOU')
        break
    if sim == 'O':
        tabuleiro[column][row] = 'X'
    elif sim == 'X':
        tabuleiro[column][row] = 'O'