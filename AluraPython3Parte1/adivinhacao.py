print("********************************")
print("Bem vindo no jogo da Adivinhação")
print("********************************")

numero_secreto = 42;

#Input sempre captura uma string
# Devido a isso, deve-se utilizar a função "int" para converter de string para int
chute = int(input("Digite seu número: "))

# A função não precisa de chaves. Utiliza-se ":" após a função "if"
# São quatro espaços para identação. A identação é muito importante
# para que o código fique correto. Pois não há muita verbosidade na sintaxe
if(chute == numero_secreto):
    print("Você acertou")
else:
    print("Você errou")