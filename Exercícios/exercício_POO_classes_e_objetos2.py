# 01. Na classe, ContaBancaria, converta saldo para uma atributo privado. Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo).

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor inválido.')
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
            print(f'Saldo atualizado para R${valor}.')
        else:
            print('Saldo não pode ser negativo.')   

# Testes:

conta = ContaBancaria('Cliente', 1000)
print(conta.get_saldo())  
conta.depositar(500)
print(conta.get_saldo())  
conta.sacar(200)
print(conta.get_saldo())  
conta.set_saldo(1500)     
print(conta.get_saldo())

# 02. Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores.

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade
    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, cpf):
        self.__cpf = cpf
    def get_identidade(self):
        return self.__identidade
    def set_identidade(self, identidade):
        self.__identidade = identidade

# Testes:

pessoa = Pessoa('Vívian', '28/02/1999', '111.222.333-44', '1.222.333')
print(pessoa.get_cpf())
print(pessoa.get_identidade())
pessoa.set_cpf('555.666.777-88')
pessoa.set_identidade('4.555.666')
print(pessoa.get_cpf())
print(pessoa.get_identidade())
