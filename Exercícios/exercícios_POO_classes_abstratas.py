# Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. Mostre o uso criando objetos e chamando o método falar().

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass
class Cachorro(Animal):
    def falar(self):
        return "Au Au!"
class Gato(Animal):
    def falar(self):
        return "Miau!"

cachorro = Cachorro()
gato = Gato()
print(cachorro.falar())  
print(gato.falar())

# Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.

animal = Animal()  
print(animal.falar())

# TypeError: Can't instantiate abstract class Animal with abstract methods falar. Esse erro acontece porque a classe Animal é abstrata e possui um método abstrato falar() que não foi implementado. Classes abstratas não podem ser instanciadas diretamente.

# Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro(). Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos. Teste criando um objeto e calculando sua área e perímetro.

from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
    def perimetro(self):
        return 2 * (self.largura + self.altura)

retangulo = Retangulo(5, 10)
print(retangulo.area())
print(retangulo.perimetro())

# Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). Depois, crie uma subclasse Carro que implemente apenas o método mover(). O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.

from abc import ABC, abstractmethod
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def parar(self):
        pass
class Carro(Transporte):
    def mover(self):
        return "O carro está se movendo."

carro = Carro()
print(carro.mover())

# TypeError: Can't instantiate abstract class Carro with abstract methods parar. Isso acontece porque a classe Carro não implementou o método abstrato parar() da classe Transporte. Para corrigir, precisamos implementar o método parar() na classe Carro.

from abc import ABC, abstractmethod
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def parar(self):
        pass
class Carro(Transporte):
    def mover(self):
        return "O carro está se movendo."
    def parar(self):
        return "O carro parou."

carro = Carro()
print(carro.mover())
print(carro.parar())

# ------------------------------FIM!------------------------------



