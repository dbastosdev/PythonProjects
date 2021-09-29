#Python programação orientada a objetos: 

Não teve um projeto para implementar como nos outros cursos. Apenas conceitos. 

## 1- O problema do paradigma procedural

    // O linux é escrito no paradigma procedural o.o

    // Um dos problemas do paradigma procedural é a enorma quantidade de repetição de código de forma desnecessário.
    // Além disso, é difícil agrupar propriedades de um mesmo item e suas ações. Imagine uma conta: com seu código, 
    // seu titular, seu saldo e limite. Além disso, com suas ações de depositar, de saque dentre outras. 
    // Uma das melhores de solucionar esse problema é a orientação a objetos. 

    // A essência da OO é juntar elementos em comum criando entidades chamadas classes e suas instâncias os objetos. 
    // Eles agrupam elementos em comum como atributos (caracterísitcas) e métodos (ações). Além de permitir outras
    // caracterísitcas típicas do universo OO, como herança, interfaces e etc. 

    // dicionários: Apesar de agruparem dados, são inferiores a classes

nome = {"chave1": valor, "chave2": valor, "chave3": valor}
-> valores são mutáveis.
-> somente tuplas são imutáveis.

## 2- Classe, objetos e 3- métodos

### Criação de classe: 
    
    // DEFINIÇÃO DE ATRIBUTOS
    // self: referencia que guarda o endereço do objeto em memória. Criado automáticamente pelo python. 
    // outros parâmetros são referencias do contrutor
    // __init__ é uma função construtora do python para criação da classe
    // É possível inicializar algum valor como padrão. Exemplo limite inicial de mil reais
    // def __init__(self, numero, titular, saldo, limite =1000.00), se limite não for declarado será igual a 1000.00. 

    // DEFINIÇÃO DE MÉTODOS
    // Da mesma forma que nos atributos, os métodos são criados a partir da palavra reservada self
    // essa palavra, assim como this no Java permite acessar os atributos da classe. 
    // Nos métodos são passados parâmetros, além do self, para que sejam feitas operações. 

class Conta:
    
// Define os atributos
    def __init__(self, numero, titular, saldo, limite):     
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

// Define os métodos
   def extrato(self):
        print("saldo {} do titular {}".format(self.saldo, self.titular))

   def deposita(self, valor):
        self.saldo += valor
   
   def saca(self, valor):
        self.saldo -= valor


### Criação de um objeto: 

    // Cria a instância de uma classe conta

conta = Conta(123, "bastos", 55.5, 1000.00)
conta2 = Conta(321, "lima", 60.5, 900.00)

### Importando classe criada no console e acessando atributos e métodos do objeto: 

    // Importa do arquivo conta.py a classe Conta
>>> from conta import Conta

    //Cria o objeto conta
>>> conta = Conta(123, "bastos", 55.5, 1000.00)

    // Acessa atributos
>>> conta.saldo       // imprime na tela 55.5

    // Acessa métodos
>>> conta.extrato()   // imprime o texto configurado no print do método extrato. 

### Outros conceitos fundamentais

    // Se um objeto ficar sem referência, esse objeto será removido da memória por um processo chamado garbage collector
    // Assim como no Java, podemos ter várias referências a um objeto.
ex.: 
conta = Conta()  // Cria um objeto em memória tendo como referencia o nome conta
conta2 = conta   // Não foi criado um novo objeto. Agora tanto conta, quanto conta2 apontam para o mesmo objeto do tipo Conta

conta2 = None    // Remove a referência de conta do conta2
conta = None     // O objeto da memória ficou sem referência e será limpo pelo garbage collector

## 4- Encapsulamento

    // É quando se acessa e modifica os atributos de uma classe / objeto apenas através de métodos.
    // adicionando o "__" na frente dos atributos, os mesmos ficam privados e apenas ficam acesíveis via métodos
    // Criação de atributos privados

    // Apesar desse ser um encapsulamento "falso" pois o python apenas avisa que os atributos devem ser acessados via método e não bloqueia como no Java
    // Se fizermos conta = Conta() e em seguida conta.tipoDeConta = Gold o python cria esse atributo de forma automática
    // Maneira de declarar uma operação que manipula dados de dois objetos de mesmo tipo.

    // uma classe deve ter apenas uma responsabilidade (ou deve ter apenas uma razão para existir). 
    // Em outras palavras, ela não deve assumir responsabilidades que não são delas.
    // Princípio SOLID
    // S - Single responsibility principle
    // O - Open/closed principle
    // L - Liskov substitution principle
    // I - Interface segregation principle
    // D - Dependency inversion principle
    
class Conta:
    def __init__(self, numero, titular, saldo, limite):     
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def transfere(self, valor, destino):
        self.saca(valor)                     // Conta de onde o R$ sai objeto que chama o método
        destino.deposita(valor)              // Conta para onde o R$ vai outro objeto


## 5- Usando propriedades
    
    // Para retornar ou editar os valores dos atributos de uma classe, utilizamos os getters and setters

class Conta:
    def __init__(self, numero, titular, saldo, limite):     
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

// Em ambos os casos abaixo o encapsulamento será respeitado. De forma a não acessar diretamente os atributos
// Só devem ser criados setter e getters diante de dados que realmente precisam disso. 

    def get_limite(self):              // retorna o valor do limite quando chamado. "get" sempre retorna algo
        return self.__limite

    def set_titular(self, nome):       // edita o valor do titular quando chamado. "set" nunca retorna nada
        self.__titular = nome          // aqui é possível encadear métodos buit in do python para aplicar propriedades

// Os propeties são para facilitar a escrita de código em python. Assim elimina-se a necessidade de escrever get e set

class Cliente:
    def __init__(self, nome):     
        self.__nome = nome
    
    @propety                           // chama a propriedade através de um método 'nome' sem '()' como se fosse uma propriedade
    def nome(self):            
        return self.nome.title()       // emcadeamento de método built in

    @nome.setter                       // edita a propriedade nome
    def nome(self, nome):            
       self.__nome = nome

### Formas de uso: 

    // Importa do arquivo conta.py a classe Conta
>>> from cliente import Cliente

    //Cria o objeto conta
>>> cliente = Cliente("bastos")

    // Acessa atributos
>>> cliente.nome       // imprime na tela bastos

    // Edita nome
>>> cliente.nome = "lima"   // o atributo self.nome agora é igual a lima 


## 6- Métodos privados e estáticos
    
    // Podemos passar um método dentro de outro método. 

    // No trecho de código abaixo, se o método __pode_sacar for true, o saque no método saca é realizado. 
    // caso contrário, imprime na tela a mensagem de ultrapassagem do limite. 
    // trecho de código na classe conta. 

def __pode_sacar(self, valor_a_sacar):                              // Aqui é definido com "__" que o método é privado.
    valor_disponivel_a_sacar = self.__saldo + self.__limite
    return valor_a_sacar <= valor_disponivel_a_sacar 

def saca(self, valor):
    if(self.__pode_sacar(valor)):
        self.__saldo -= valor
    else:
        print("O valor {} passou o limite".format(valor))


    // Como definir um atributo de classe, que é comum mas não faz parte de nenhum objeto em específico
    // Assim como os métodos statics do Java

class Conta:

    def __init__(self, numero, titular, saldo, limite):             
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod                     // Definie um código que é da classe e não do objeto instaciado.
    def codigos_bancos():
         return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

// Usando: 

// Importa a classe
>>> from conta import Conta

// guarda os códigos em uma variável qualquer
>>> codigos = Conta.codigos_bancos()

// chama a variável
>>> codigos
{'BB': '001', 'Caixa': '104', 'Bradesco':'237'}



