# Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

pessoa1 = Pessoa("Ana")
livro1 = Livro("Python para Iniciantes", "Carlos Silva")
print(f"{pessoa1.nome} está lendo o livro '{livro1.titulo}' de {livro1.autor}.")

# Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

class Onibus:
    def __init__(self, linha):
        self.linha = linha
    def embarcar(self, aluno):
        return f"{aluno.nome} embarcou no ônibus da linha {self.linha}."
class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def pegar_onibus(self, onibus):
        return onibus.embarcar(self)

aluno1 = Aluno("João")
onibus1 = Onibus("205 - Centro")
print(aluno1.pegar_onibus(onibus1))

# Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    def listar_funcionarios(self):
        return [f"{func.nome} - {func.cargo}" for func in self.funcionarios]

func1 = Funcionario("Mariana", "Analista")
func2 = Funcionario("Pedro", "Desenvolvedor")
departamento = Departamento("TI")
departamento.adicionar_funcionario(func1)
departamento.adicionar_funcionario(func2)
print(departamento.listar_funcionarios())

# Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
    def listar_jogadores(self):
        return [f"{jog.nome} - {jog.posicao}" for jog in self.jogadores]

jog1 = Jogador("Lucas", "Atacante")
jog2 = Jogador("Rafael", "Goleiro")
time = Time("Campeões FC")

time.adicionar_jogador(jog1)
time.adicionar_jogador(jog2)
print(time.listar_jogadores())

# Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto.

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)
    def especificacoes(self):
        return f"Carro: {self.modelo}, Motor: {self.motor.potencia} HP"
    
carro1 = Carro("Fusca", 50)
print(carro1.especificacoes())
del carro1

# Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.

class Comodo:
    def __init__(self, nome):
        self.nome = nome
class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.comodos = []
    def adicionar_comodo(self, comodo):
        self.comodos.append(comodo)
    def listar_comodos(self):
        return [comodo.nome for comodo in self.comodos]

casa1 = Casa("Rua das Flores, 123")
sala = Comodo("Sala")
cozinha = Comodo("Cozinha")
quarto = Comodo("Quarto")

casa1.adicionar_comodo(sala)
casa1.adicionar_comodo(cozinha)
casa1.adicionar_comodo(quarto)
print(casa1.listar_comodos())

# ------------------------------FIM!------------------------------