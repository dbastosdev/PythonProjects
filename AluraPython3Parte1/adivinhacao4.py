# Mais sobre a interpolação de strings:
# print("tentativa {} de {} tentativas".format(1, 2))
# Vai imprimir : tentativa 1 de 2
# print("tentativa {1} de {0} tentativas".format(1, 2))
# Vai imprimir : tentativa 2 de 1, pois são os índices do format

# É possível ainda manipular casas decimais e etc.
# print("valor R$ {:.2f} ".format(1234.501654))
# >> R$ 1234.50

# mais sobre o format: https://docs.python.org/3/library/string.html#formatexamples

print("********************************")
print("Bem vindo no jogo da Adivinhação")

numero_secreto = 42;

total_de_tentativas = 3
i = 1

# Maneira distinta de declaração do for no python.
# Precis de range e teve que adicionar o "+1" pois o range é exclusivo
# Um terceiro parâmetro que poderia ser declarado no "for", seguido de vírgula seria um "step" ou passo
# em que o for é executado.
for i in range(i, total_de_tentativas+1):
    print("********************************")
    print("")
    print(f"Tentativa {i} de {total_de_tentativas} tentativas")
    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    # Avalia range do número digitado pelo usuário
    # Perde uma rodada se utilizar um número fora do range.
    if(chute < 1 or chute > 100):
        print("O múmero digitado deve ser entre 1 e 100")
        continue # segue para próxima iteração

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        #sai do laço e termina o jogo
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
