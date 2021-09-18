print("********************************")
print("Bem vindo no jogo da Adivinhação")
print("********************************")

numero_secreto = 42;

chute = int(input("Digite seu número: "))

# if, else e elif são boolean
# operadores relacionais são normais de qualquer linguagem
if(chute == numero_secreto):
    print("Você acertou")
else:
    # if encadeado
    if(chute > numero_secreto):
        print("Seu chute foi maior que o do número secreto")
    # else encadeado
    else:
        #Aqui eu poderia utilizar elif (condição):, mas o else simplifica
        print("Seu chute foi menor que o do número secreto")
    print("Você errou")

print("fim do jogo")