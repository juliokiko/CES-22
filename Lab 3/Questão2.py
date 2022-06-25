# Construindo uma pizzaria usando o Padrão Decorator

# Primeiramente, definimos a classe de ingredientes da pizza, a classe principal a ser utilizada

class Ingredientes_Pizza:

    def getDescription(self):
        return self.__class__.__name__  # nome do ingrediente
    def getTotalCost(self):
        return self.__class__.cost      # custo do ingrediente


class Caixa_Pizza(Ingredientes_Pizza): # classe derivada referindo-se a uma embalagem, não um ingrediente de fato
    cost = 1.00


# Usando o Decorator, classifica-se os ingredientes mediante uma lógica em que obtém-se sua descrição e seu custo

class Decorator(Ingredientes_Pizza):
    def __init__(self, ingredientes_Pizza):
        self.component = ingredientes_Pizza
    def getTotalCost(self):
        return self.component.getTotalCost() + Ingredientes_Pizza.getTotalCost(self) # aqui armazena-se o custo do ingrediente
    def getDescription(self):
        return self.component.getDescription() + " " + Ingredientes_Pizza.getDescription(self) # aqui armazena-se a descrição do ingrediente
    

# Então, exibe-se os ingredientes conforme prevê o padrão criado

class Massa_Redonda(Decorator):
    cost = 4.50
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Molho_de_Tomate(Decorator):
    cost = 2.70
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Queijo_Muçarela(Decorator):
    cost = 5.00
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Tomate(Decorator):
    cost = 3.75
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Manjericão(Decorator):
    cost = 1.20
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Calabresa(Decorator):
    cost = 4.20
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Azeitona(Decorator):
    cost = 0.90
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Milho(Decorator):
    cost = 2.20
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Presunto(Decorator):
    cost = 5.90
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Frango(Decorator):
    cost = 6.80
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Catupiry(Decorator):
    cost = 7.00
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Chocolate(Decorator):
    cost = 4.00
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

class Leite_Condensado(Decorator):
    cost = 2.95
    def __init__(self, ingredientes_Pizza):
        Decorator.__init__(self, ingredientes_Pizza)

# Aqui definem-se as variáveis que contemplam os ingredientes e seu custo total (sabores de pizza)

pizza_de_margherita = Manjericão(Tomate(Queijo_Muçarela(Molho_de_Tomate(Massa_Redonda(Caixa_Pizza())))))

pizza_a_moda = Milho(Calabresa(Presunto(Queijo_Muçarela(Molho_de_Tomate(Massa_Redonda(Caixa_Pizza()))))))

pizza_de_frango_e_catupiry = Azeitona(Frango(Catupiry(Queijo_Muçarela(Molho_de_Tomate(Massa_Redonda(Caixa_Pizza()))))))

pizza_doce = Chocolate(Leite_Condensado(Queijo_Muçarela(Massa_Redonda(Caixa_Pizza()))))

# Po fim, imprimem-se os resultados do código usando Decorator, atestando a corretude da implementação

print("\nOs ingredientes de cada sabor e seu valor total são:\n")
print(pizza_de_margherita.getDescription() + ": $" + str(pizza_de_margherita.getTotalCost()))
print("\n")
print(pizza_a_moda.getDescription() + ": $" + str(pizza_a_moda.getTotalCost()))
print("\n")
print(pizza_de_frango_e_catupiry.getDescription() + ": $" + str(pizza_de_frango_e_catupiry.getTotalCost()))
print("\n")
print(pizza_doce.getDescription() + ": $" + str(pizza_doce.getTotalCost()))