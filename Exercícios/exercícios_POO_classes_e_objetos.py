# 01. Crie uma classe chamada 'pessoa' que tenha os atributos 'home' e 'idade'. Em seguida, crie dois objetos dessa classe e imprima os valores de ses atributos. 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

nome1 = input('Digite seu nome: ')
idade1 = input('Digite sua idade: ')
pessoa1 = Pessoa(nome1, idade1)

nome2 = input('Digite seu nome: ')
idade2 = input('Digite sua idade: ')
pessoa2 = Pessoa(nome2, idade2)

print(f'Nome: {pessoa1.nome}, Idade: {pessoa1.idade}')
print(f'Nome: {pessoa2.nome}, Idade: {pessoa2.idade}')

print("-" * 30)

# 02. Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.')

nome1 = input('Digite o nome da primeira pessoa: ')
idade1 = input('Digite a idade da primeira pessoa: ')
pessoa1 = Pessoa(nome1, idade1)

nome2 = input('Digite o nome da segunda pessoa: ')
idade2 = input('Digite a idade da segunda pessoa: ')
pessoa2 = Pessoa(nome2, idade2)

pessoa1.apresentar()
pessoa2.apresentar()

print("-" * 30)

#Obs.: Eu não quis fazer com 'João' e '25 anos' como manda o enunciado, porque fica mais fácil pra eu entender com as interações do usuário com o programa no terminal, só que isso dá mais trabalho, então a partir da próxima questão eu vou fazer do jeito mais simples, ok? :D

# 03. Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro('Toyota', 'Corolla', 2020)
carro2 = Carro('Honda', 'Civic', 2019)
carro3 = Carro('Ford', 'Focus', 2018)
print(f'Carro 1: {carro1.marca} {carro1.modelo} {carro1.ano}')
print(f'Carro 2: {carro2.marca} {carro2.modelo} {carro2.ano}')
print(f'Carro 3: {carro3.marca} {carro3.modelo} {carro3.ano}')  
print("-" * 30)

# 04. Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro('Toyota', 'Corolla', 2020)
print(f'Antes da alteração: {carro1.marca} {carro1.modelo} {carro1.ano}')
carro1.ano = 2009
print(f'Depois da alteração: {carro1.marca} {carro1.modelo} {carro1.ano}')  
print("-" * 30)

# 05. Crie uma classee ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques. 

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo insuficiente para saque de R${valor}. Saldo atual: R${self.saldo}')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')  
conta = ContaBancaria('João', 1000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)
print("-" * 30)

# 06. Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saldo insuficiente para saque de R${valor}. Saldo atual: R${self.saldo}')
            return False
        else:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')  
            return True
conta = ContaBancaria('João', 1000)
conta.depositar(500)
if conta.sacar(200):
    print("Saque realizado com sucesso.")
else:
    print("Saque não realizado.")
if conta.sacar(2000):
    print("Saque realizado com sucesso.")
else:
    print("Saque não realizado.")
print("-" * 30)

# 07. Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
class Turma:
    def __init__(self):
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f'Aluno {aluno.nome} adicionado à turma.')
aluno1 = Aluno('Ana', 8.5)
aluno2 = Aluno('Bruno', 7.0)
turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
print("-" * 30)

# 08. Na classe Aluno, Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __str__(self):
        return f'Aluno: {self.nome} - Nota: {self.nota}'
aluno1 = Aluno('Ana', 8.5)
aluno2 = Aluno('Bruno', 7.0)
print(aluno1)
print(aluno2)
print("-" * 30)

# 09. Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.

class Cachorro:
    especie = "Canis familiaris"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
cachorro1 = Cachorro('Rex', 5)
print(f'Nome: {cachorro1.nome}, Idade: {cachorro1.idade}, Espécie: {cachorro1.especie}')
print(f'Espécie acessada pela classe: {Cachorro.especie}')
print("-" * 30)

 




