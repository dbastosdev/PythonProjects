print("********************************")
print("Bem vindo no jogo da Adivinhação")

numero_secreto = 42;

total_de_tentativas = 3
i = 1

while (i <= total_de_tentativas):
    print("********************************")
    print("")
    # forma 1
    # print("Tentativa", i, "de", total_de_tentativas)
    # forma 2
    # print("tentativa {} de {} tentativas".format(i, total_de_tentativas))
    # forma 3 abaixo: interpolação de strings
    print(f"Tentativa {i} de {total_de_tentativas} tentativas")
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

    i += 1

print("Fim do jogo")
