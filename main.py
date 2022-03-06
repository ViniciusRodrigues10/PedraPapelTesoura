def regraJogo(escolhaJogador1, escolhaJogador2):
    if escolhaJogador1 == escolhaJogador2:
        return "empate"

    elif escolhaJogador1 == "papel":
        if escolhaJogador2 == "pedra":
            return "jogador1"
        elif escolhaJogador2 == "tesoura":
            return "jogador2"

    elif escolhaJogador1 == "tesoura":
        if escolhaJogador2 == "papel":
            return "jogador1"
        elif escolhaJogador2 == "pedra":
            return "jogador2"

    elif escolhaJogador1 == "pedra":
        if escolhaJogador2 == "tesoura":
            return "jogador1"
        elif escolhaJogador2 == "papel":
            return "jogador2"

placarJogador1 = placarJogador2 = cont = 0
while cont < 5:
    escolhaJogador1 = str(input())
    escolhaJogador2 = str(input())
    if regraJogo(escolhaJogador1, escolhaJogador2) == "empate":
        continue
    elif regraJogo(escolhaJogador1, escolhaJogador2) == "jogador1":
        placarJogador1 += 1
    elif regraJogo(escolhaJogador1, escolhaJogador2) == "jogador2":
        placarJogador2 += 1
    cont += 1

if placarJogador1 < placarJogador2:
    print("MIGUEL")
elif placarJogador1 > placarJogador2:
    print("MARIA")
