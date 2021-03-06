
# Define uma função que pode ser importada em outro código. Nesse caso,
# será importada em "jogo.py" como um módulo
# ATENÇÃO!!! Deve ser identado.

# Dessa maneira que se configura uma função em python
# Não temos chaves na linguagem. Logo, para funcionar tudo que está na função forca deve estar identado.
# Assim como if's, else, elif e etc.
import random


def jogar_forca():
    print("**********************************")
    print("****Bem vindo no jogo de forca****")
    print("**********************************")

# Variáveis são dinâmicamente tipadas em tempo de execução. Não precisam ser declaradas

    # define uma palavra secreta
    # através do método upper, sempre vai transformar a entrada em letra maiúscula. Padroniza a comparação.
    # Palavra secreta vinda de um arquivo:
    # lista em que ficarão armazenadas as palavras do arquivo
    palavras = []
    # Leitura do arquivo
    arquivo = open("palavras.txt", "r")
    # Iteração no arquivo e inclusão de itens na lista de palavras
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)
    arquivo.close()

    # Atribui a palavra secreta, uma palavra aleatória que esteja dentro da lista
    index = random.randrange(0, len(palavras))
    palavra_secreta = palavras[index]

    # Define uma estrutura para guardar os dados digitados pelo usuário e monitorar o tamanho da palvra
    # Preenche automáticamente com underline a quantidade de letras da palavra secreta
    # Outra forma: letras_acertadas = ["_" for i in palavra_secreta] -> List Comprehensions
    letras_acertadas = []
    for i in palavra_secreta: #Atenção! Não intera em inteiros. Erro lógico que eu estava cometendo
        letras_acertadas.append("_")

   # valor começa com letra maiúscula
   # Repare que os valores vazios ou zeros são considerado False, do contrário são considerados True.
    enforcou = False
    acertou = False
    erros = 0
    # looping do jogo
    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        # método "strip()" remove caracteres especiais de palavras.
        chute = chute.strip().upper()

        # Se a letra chutada não está dentro da palavra chave, incrementa erros:
        if (chute in palavra_secreta):

            # Checa se letra digitada é igual a palavra chave
            string_index = 0

            # iteração em toda a palvra_secreta (string)
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[string_index] = letra

                # a cada iteração do for, incrementa o index e não somente ao acertar
                string_index += 1
        else:
            erros += 1

        # Verifica se já se enforcou e em caso positivo, muda o status da flag enforcou, encerrando o programa
        # Se erros = tamanho da palavra, o usuário errou a quantidade máxima de tentativas
        enforcou = erros == len(palavra_secreta)

        #verifica se todas as letras da palavra chave foram acertadas e também encerra o jogo.
        if(not "_" in letras_acertadas):
            acertou = True

        # Ao sair do laço for, exibe as letras acertadas ou não. Como o for está no looping while, sempre acaba saindo.
        print(letras_acertadas)
        print("Jogando...")



    print("Final do jogo")

# if para informar ao programa que se esse arquivo não for importado como uma função em outro arquivo,
# esse mesmo será o ponto de entrada.
if(__name__ == "__main__"):
    jogar_forca()

# APRENDIZADO GERAL DO CÓDIGO:

# list é um tipo buit in do python. Aceita diversos tipos diferentes em uma única lista.
# Existem diversos métodos e funções built in na documentação.
# Muitos erros de python ocorrem por falha na identação. Deve-se sempre identar adequadamente com 4 espaços
# tuplas trabalham com parenteses e é uma estrutura de dados imutável. Podem ter valores internos de vários tipos
# É possível converter uma lista em tupla e vice versa
# Existe ainda o set que não permite elementos duplicados. Set não possui índice