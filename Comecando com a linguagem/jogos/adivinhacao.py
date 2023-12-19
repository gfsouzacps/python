print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = input("Digite o seu numero: ")

    # Chute nesse caso recebe uma str. Devido a isso, ao fazer o if temos false independente do número.
    # Para isso fizemos int(chute) que faz a conversão
    conv_chute = int(chute)
    acertou = numero_secreto == conv_chute
    maior = conv_chute > numero_secreto
    menor = conv_chute < numero_secreto

    if acertou:
        print("Voce acertou!")
        break
    else:
        if maior:
            print("Você errou, o chute foi maior que o numero secreto!")
        elif menor:
            print("Voce errou, o chute foi menor que o numero secreto!")

    print("Fim do jogo")
    print("*****************************")
