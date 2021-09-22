# Organizando o código em funções. É uma boa prática separar o código em funções
# cada uma com sua respectiva responsabilidade.
# Funções podem receber parâmetros

import random

def jogar_forca2():

    imprime_mensagem_abertura()

    # Como as variáveis só existem dentro do seu escopo, é necessário declarar a função com um retorno
    # e guardar esse mesmo retorno nas variáveis utilizadas ao longo do código.
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = []
    for i in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            string_index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[string_index] = letra
                string_index += 1
        else:
            erros += 1
            print("  _______     ")
            print(" |/      |    ")

            if (erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if (erros == 2):
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")

            if (erros == 3):
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if (erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if (erros == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if (erros == 6):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if (erros == 7):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

            print(" |            ")
            print("_|___         ")
            print()

        if(erros == 7):
            enforcou = True
            print("Puxa, você foi enforcado!")
            print("A palavra era {}".format(palavra_secreta))
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")
            break

        if(not "_" in letras_acertadas):
            acertou = True
            ganhou()
            break

        print(letras_acertadas)
        print("Jogando...")

    print("Final do jogo")


def ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_abertura():
    print("**********************************")
    print("****Bem vindo no jogo de forca****")
    print("**********************************")

def carrega_palavra_secreta():
    palavras = []
    arquivo = open("palavras.txt", "r")
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)
    arquivo.close()

    index = random.randrange(0, len(palavras))
    palavra_secreta = palavras[index]

    return palavra_secreta


# Essa é a última função que deve ser declarada
if(__name__ == "__main__"):
    jogar_forca2()
