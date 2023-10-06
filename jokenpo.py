vetor= ("pedra","papel","tesoura")
jogador1=int(input("jogador  1 escolha : "))
jogador2=int(input("jogador 2 escolha : "))

if jogador1 == 0:
    if jogador2 == 0:
        print("Empante")
    elif jogador2 == 1:
        print(f" O jogador 2 venceu")
    elif jogador2 == 2:
        print(f" O jogador 1 venceu")
if jogador1 == 1:
    if jogador2 == 1:
        print("Empate")
    elif jogador2 == 0:
        print(f" O jogador 1 venceu")
    elif jogador2 == 2:
        print(f" O jogador 2 venceu")
if jogador1 == 2:
        if jogador2 == 2:
            print(f"Empate")
        elif jogador2 == 0 :
            print(f" O jogador 2 venceu")
        elif jogador2 == 1:
            print(f" O jogador 1 venceu")
print("jogo acabou")