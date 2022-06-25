# Classe veicular em um simulador de estradas usando Design Pattern Bridge and Factory

import abc

# Primeiramente, define-se a classe principal, que é a classe Veículo

class Veículo(abc.ABC):

    def __init__(self, tipo, motor):
        self.tipo = tipo # tipo de veículo
        self.motor = motor.requisitos_motor # tipo de motor
        self.eficiência = motor.requisitos_eficiência # eficiência do motor

    @abc.abstractmethod
    def descrição(self): # descrição básica do veículo e seu respectivo motor
        pass


# Agora, define-se as classes associadas, que são os tipos de veículo, conforme o método solicitado no enunciado

# Veículo: Moto

class Moto(Veículo):

    def __init__(self, tipo, motor):
        super().__init__(tipo, motor)

    def descrição(self):
        print("O veículo descrito é uma %s." % self.tipo)
        print("Seu motor é %s!" % self.motor)


# Veículo: Carro

class Carro(Veículo):

    def __init__(self, tipo, motor):
        super().__init__(tipo, motor)

    def descrição(self):
        print("O veículo descrito é um %s." % self.tipo)
        print("Seu motor é %s!" % self.motor)


# Veículo: Ônibus

class Ônibus(Veículo):

    def __init__(self, tipo, motor):
        super().__init__(tipo, motor)

    def descrição(self):
        print("O veículo descrito é um %s." % self.tipo)
        print("Seu motor é %s!" % self.motor)


# Veículo: Charrete

class Charrete(Veículo):

    def __init__(self, tipo, motor):
        super().__init__(tipo, motor)

    def descrição(self):
        print("O veículo descrito é uma %s." % self.tipo)
        print("Seu motor é %s!" % self.motor)


# Veículo: Caminhão

class Caminhão(Veículo):

    def __init__(self, tipo, motor):
        super().__init__(tipo, motor)

    def descrição(self):
        print("O veículo descrito é um %s." % self.tipo)
        print("Seu motor é %s!" % self.motor)


# Aqui, define-se uma nova classe para o Motor, com as instâncias indicadas e que serão atribuídas aos veículos

class Motor(abc.ABC):

    @abc.abstractmethod
    def eficiência(self):
        pass


# Motor: Combustão

class Combustão(Motor):

    def __init__(self):
        self.requisitos_motor = "motor de combustão" # definição do tipo de motor
        self.eficiência()

    def eficiência(self):
        self.requisitos_eficiência = "C" # definição da eficiência do motor


# Motor: Elétrico

class Elétrico(Motor):

    def __init__(self):
        self.requisitos_motor = "elétrico"
        self.eficiência()

    def eficiência(self):
        self.requisitos_eficiência = "A"


# Motor: Híbrido

class Híbrido(Motor):

    def __init__(self):
        self.requisitos_motor = "híbrido"
        self.eficiência()

    def eficiência(self):
        self.requisitos_eficiência = "B"


# Abaixo, alguns resultados para o terminal, conferindo a corretude da implementação

print("\nAlguns veículos serão exibidos a seguir:\n")
moto = Moto("motocicleta", Híbrido())
moto.descrição()
print("\n")
carro = Carro("carro", Combustão())
carro.descrição()
print("\n")
ônibus = Ônibus("ônibus", Elétrico())
ônibus.descrição()
print("\n")
charrete = Charrete("charrete", Híbrido())
charrete.descrição()
print("\n")
caminhão = Caminhão("caminhão", Elétrico())
caminhão.descrição()
print("\n")