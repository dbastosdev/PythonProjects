
# Define uma função que pode ser importada em outro código. Nesse caso,
# será importada em "jogo.py" como um módulo
# ATENÇÃO!!! Deve ser identado.

# Dessa maneira que se configura uma função em python
# Não temos chaves na linguagem. Logo, para funcionar tudo que está na função forca deve estar identado.
def jogar_forca():
    print("**********************************")
    print("****Bem vindo no jogo de forca****")
    print("**********************************")

# Variáveis são dinâmicamente tipadas em tempo de execução. Não precisam ser declaradas

    # define uma palavra secreta
    palavra_secreta = "banana"

    # define uma estrutura para guardar os dados digitados pelo usuário e monitorar o tamanho da palvra
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

   # valor começa com letra maiúscula
   # Repare que os valores vazios ou zeros são considerado False, do contrário são considerados True.
    enforcou = False
    acertou = False

    # looping do jogo
    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip() # método retira espaços

        # Checa se letra digitada é igual a palavra chave
        string_index = 0

        # iteração em toda a palvra_secreta (string)
        for letra in palavra_secreta:

            # através do método upper, sempre vai transformar a entrada em letra maiúscula. Padroniza a comparação.
            if(chute.upper() == letra.upper()):
                letras_acertadas[string_index] = letra

            # a cada iteração do for, incrementa o index e não somente ao acertar
            string_index = string_index + 1

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