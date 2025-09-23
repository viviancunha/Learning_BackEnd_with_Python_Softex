# 01. Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email) 

cliente1 = Cliente('Vívian','vivian@alunasoftex.com')
print(cliente1.nome)
print(cliente1.email)

# 02. Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        return f'Nome: {self.nome}, Email: {self.email}' 

class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def exibir_informacoes(self):
        return super().exibir_informacoes()
    
cliente2 = Cliente('Fernanda','fernanda@alunasoftex.com')
print(cliente2.exibir_informacoes())

# 03. Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.

class Usuario:
    def saudacao(self):
        return 'Olá, usuário'
    
class Cliente(Usuario):
    def saudacao(self):
        return 'Olá, cliente' 
    
cliente3 = Cliente()
print(cliente3.saudacao())

# 04. Na classe Cliente, adicione o atributo saldo. Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

cliente4 = Cliente('Natalia', 'natalia@franca.com', '100.000.00')
print(cliente4.nome)
print(cliente4.email)
print(cliente4.saldo)

# 05. Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email  

class Funcionario(Usuario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email)
        self.salario = salario 

class Gerente(Funcionario):
    def __init__(self, nome, email, salario, unidade):
        super().__init__(nome, email, salario)
        self.unidade = unidade

gerente1 = Gerente('Renato', 'renato@henrique.com', '15.000.00', 'Unidade Compartilhada Jurídica e de Compliance')
print(gerente1.nome)
print(gerente1.email)
print(gerente1.salario)
print(gerente1.unidade)

# 06. Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?

class Autenticacao:
    def login(self):
        return 'Login realizado com sucesso!'
    
class Permissao:
    def verificar_permissao(self):
        return 'Permissão verificada com sucesso!'

class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome

admin1 = Administrador('Aryella')
print(admin1.nome)
print(admin1.login())
print(admin1.verificar_permissao()) # Como usar os métodos herdados? Pode ser chamado diretamente pela instância da classe Administrador, ou seja, admin1.

# 07. Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.

class Autenticacao:
    def login(self):
        return 'Login realizado com sucesso!'
    
    def status(self):
        return 'Status da Autenticação'    
    
class Permissao:
    def verificar_permissao(self):
        return 'Permissão verificada com sucesso!'
    
    def status(self):
        return 'Status da Permissão'

class Administrador(Autenticacao, Permissao):
    def __init__(self, nome):
        self.nome = nome

admin2 = Administrador('Eduarda')
print(admin2.status()) # A versão de status() chamada será a da classe Autenticacao, pois ela é a primeira na ordem de herança.
print(Administrador.__mro__) # Mostra a ordem de resolução de métodos (Method Resolution Order - MRO). Resultado no terminak: (<class '__main__.Administrador'>, <class '__main__.Autenticacao'>, <class '__main__.Permissao'>, <class 'object'>)



