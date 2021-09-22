import forca
import adivinhacao5

print("**********************************")
print("******Aos jogos do Douglas********")
print("**********************************")

print("")

print("Escolha um dos jogos para iniciar")
print("(1) Jogo forca (2) Jogo Adivinhação")

print("") #pula linha

escolha = int(input("Selecione o jogo: "))

print("")

if(escolha == 1):
    forca.jogar_forca()
elif(escolha == 2):
    adivinhacao5.jogar_advinhacao5()
else:
    print("Selecione uma opção válida")

# Atenção de como são chamados os módulos criados anteriormente para os jogos
# Eles entram como Classes/funções dentro do código
# É muito importante identar o código adequadamente para que funcionem dentro da função
# Nesse momento os dois jogos apenas são acessíveis via esse arquivo de jogos.


# Python é interpretado e não compilado. Logo, a cada linha o interpretador Python transforma o código
# em uma instrução para máquina. No caso de C, Java ... é criado um programa completo lido pela máquina
# através do compilador.

'''
O senso comum é que o Python é uma linguagem interpretada. Interpretado significa que não há um processo de compilação 
que traduz o código fonte em algum código nativo, que o seu computador entende. A documentação do Python confirma isso, no entanto 
também menciona a presença de um compilador:

"Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler."

Traduzido livremente: "Python é uma linguagem interpretada, em oposição às compiladas, embora a distinção possa ficar desfocada devido à presença do compilador de bytecode."

Temos um compilador, porém de bytecode. Bytecode é um código intermediário, normalmente independente do sistema operacional. 
Então, Python é uma linguagem compilada também? Em 2003, Fredrik Lundh, em seu artigo Compiling Python Code, título que perverte o senso comum, começa:

"Python source code is automatically compiled into Python byte code by the CPython interpreter. Compiled code is usually 
stored in PYC (or PYO) files, and is regenerated when the source is updated, or when otherwise necessary."

Novamente traduzindo livremente: "O código fonte é automaticamente compilado para bytecode do Python pelo 
interpretador CPython. O código compilado é comumente armazenado nos arquivos no PYC (ou PY0), sendo regerado quando o arquivo fonte é atualizado ou quando é necessário."

E aí? Python é uma linguagem interpretada ou compilada? As duas coisas? Há discussões acaloradas entre desenvolvedores, cada um com sua opinião. 
Então, uma resposta interessante está no StackOverFlow, aliás, a resposta mais bem avaliada:

"First off, interpreted/compiled is not a property of the language but a property of the implementation (...) 
Python is compiled. Not compiled to machine code ahead of time (i.e. "compiled" by the restricted and wrong, but also common definition), "only" compiled to bytecode"

Traduzindo: "O fato de uma linguagem ser interpretada ou compilada não é uma questão da linguagem, mas da sua implementação. (...) 
Python é compilada. Não compilada para o código de máquina antes da execução, apenas para o bytecode.

Isso significa que alguém pode implementar o Python totalmente compilado, totalmente interpretado ou ambos, a linguagem continua a mesma. 
Ser compilada/interpretada é mais propriedade da implementação do Python do que da linguagem.

E você, o que pensa dessa definição?
'''