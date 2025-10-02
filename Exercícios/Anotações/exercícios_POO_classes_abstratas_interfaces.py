# 01. Crie uma classe abstrata Pessoa que tenha os métodos: Falar, Andar e Comer e subclasses Funcionário e Aluno, que herde as características e métodos de Pessoa. Instancie um objeto para cada subclasse.

from abc import ABC, abstractmethod
class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

class Funcionario(Pessoa):
    def falar(self):
        return "O funcionário está falando."

    def andar(self):
        return "O funcionário está andando."

    def comer(self):
        return "O funcionário está comendo."
    
class Aluno(Pessoa):
    def falar(self):
        return "O aluno está falando."

    def andar(self):
        return "O aluno está andando."

    def comer(self):
        return "O aluno está comendo."

funcionario = Funcionario()
aluno = Aluno()
print(funcionario.falar())
print(funcionario.andar())
print(funcionario.comer())
print(aluno.falar())
print(aluno.andar())
print(aluno.comer())

# 02. Use o mesmo exemplo da questão anterior, mas converta a classe Pessoa em uma interface.

from abc import ABC, abstractmethod
class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

class Funcionario(Pessoa):
    def falar(self):
        return "O funcionário está falando."

    def andar(self):
        return "O funcionário está andando."

    def comer(self):
        return "O funcionário está comendo."

class Aluno(Pessoa):
    def falar(self):
        return "O aluno está falando."

    def andar(self):
        return "O aluno está andando."

    def comer(self):
        return "O aluno está comendo."

funcionario = Funcionario()
aluno = Aluno()
print(funcionario.falar())
print(funcionario.andar())
print(funcionario.comer())
print(aluno.falar())
print(aluno.andar()) 

# A diferença entre o resultado da questão 01 e 02 é que na questão 01 a classe Pessoa é uma classe abstrata, enquanto na questão 02 a classe Pessoa é uma interface. Em Python, tanto classes abstratas quanto interfaces são implementadas usando a biblioteca abc (Abstract Base Classes). A principal diferença conceitual é que uma classe abstrata pode ter métodos com implementação, enquanto uma interface não pode ter nenhum método com implementação. No entanto, no exemplo fornecido, ambas as implementações são idênticas, pois todos os métodos são abstratos em ambos os casos.