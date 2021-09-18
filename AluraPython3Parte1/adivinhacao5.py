from random import random

# Dessa maneira que se configura uma função em python
def jogar_advinhacao5():
    print("********************************")
    print("Bem vindo no jogo da Adivinhação")

    # O random não é uma função built in. Logo, é necessário fazer o import que ela seja usada
    # Poderia ser utiliado a função int no lugar de round e teria o mesmo efeito resultando em números inteiros
    # Vale a pena olhar a biblioteca da linguagem, pois pode haver alguma função que facilita a solução
    numero_secreto = round(random()*100);

    print("Qual o nível de dificuldade você deseja? ")
    print("(1) fácil (2) médio (3) difícil")
    print("")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 10
    elif(nivel ==3):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 1

    i = 1
    pontos = 1000

    for i in range(i, total_de_tentativas+1):
        print("********************************")
        print("")
        print("Tentativa {} de {} tentativas".format(i,total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("O múmero digitado deve ser entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e ganhou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
                pontos = pontos - abs(total_de_tentativas - chute)
                print("Seus pontos: ", pontos)
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
                pontos = pontos - abs(total_de_tentativas - chute)
                print("Seus pontos: ", pontos)

    print("Fim do jogo")

# Ocorre que após a definição do jogo como uma função, não é possível chamá-lo diretamente via linha
# de comando. Para resolver isso, é necessário fazer o procedimento abaixo:

if(__name__ == "__main__"):
    jogar_advinhacao5()

# Agora com essa modificação, o jogo funciona como um script isolado ou mesmo como parte de um import.
# O python controla essa variável especial name. Por isso é necessário fazer esse controle. Caso contrário,
# o arquivo jogo.py chamará direto esse arquivo.

