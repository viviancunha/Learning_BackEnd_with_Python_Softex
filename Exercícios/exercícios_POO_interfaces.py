# Crie uma interface chamada Pagamento com um método abstrato processar(valor). Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. Mostre como chamar processar() para cada uma.

from abc import ABC, abstractmethod
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass
class CartaoCredito(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento de R${valor} com cartão de crédito."
class Boleto(Pagamento):
    def processar(self, valor):
        return f"Processando pagamento de R${valor} com boleto bancário."

cartao = CartaoCredito()
boleto = Boleto()
print(cartao.processar(150.75))
print(boleto.processar(150.75))

def mover(self):
        return "O carro está se movendo."

# Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). Crie uma classe Computador que implemente ambas. Mostre seu uso.

from abc import ABC, abstractmethod
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass
class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass
class Computador(Ligavel, Desligavel):
    def ligar(self):
        return "Computador ligado."
    def desligar(self):
        return "Computador desligado."
    
computador = Computador()
print(computador.ligar())
print(computador.desligar())

# Crie uma interface Imprimivel com o método imprimir(). Crie outra interface Exportavel com o método exportar(). Implemente uma classe Relatorio que herde de ambas e implemente os métodos.

from abc import ABC, abstractmethod
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass
class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass
class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        return "Imprimindo relatório."
    def exportar(self):
        return "Exportando relatório."

relatorio = Relatorio()
print(relatorio.imprimir())
print(relatorio.exportar())

# Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. O que acontece quando você tenta instanciá-la? Corrija o código.

from abc import ABC, abstractmethod
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    @abstractmethod
    def buscar(self, id):
        pass
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return f"Objeto {objeto} salvo na memória."

# TypeError: Can't instantiate abstract class RepositorioMemoria with abstract methods buscar. Isso acontece porque a classe RepositorioMemoria não implementou o método abstrato buscar() da interface Repositorio. Para corrigir, precisamos implementar o método buscar() na classe RepositorioMemoria.

from abc import ABC, abstractmethod
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    @abstractmethod
    def buscar(self, id):
        pass
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        return f"Objeto {objeto} salvo na memória."
    def buscar(self, id):
        return f"Buscando objeto com id {id} na memória."

repositorio = RepositorioMemoria()
print(repositorio.salvar("Dados"))
print(repositorio.buscar(1))

# ------------------------------FIM!------------------------------