from cmath import pi
import math
from abc import ABC, abstractmethod

class Breakfast_Rancho:
  def __init__(self, alimentos):
    self.alimentos = alimentos

  def __repr__(self):
    return f'Breakfast_Rancho({self.alimentos!r})'

  @classmethod
  def segunda(cls):
    return cls(['salsicha','mingau_rosa','leite_com_café'])

  @classmethod
  def terça(cls):
    return cls(['queijo','mingau_branco','pão'])

  @classmethod
  def sábado(cls):
    return cls(['mingau_marrom','café_puro'])

  @classmethod
  def domingo(cls):
    return cls(['água'])

class Playing_with_math:
  def __init__(self, número, raio, lado_do_quadrado):
    self.número = número
    self.raio = raio
    self.lado_do_quadrado = lado_do_quadrado

  def __repr__(self):
    return f'Playing_with_math({self.número!r})'

  def fatorial(self):
    return self.equação(self.número)
  
  @staticmethod
  def equação(n):
    return math.factorial(n)

  def area(self):
    return self.area_quadrado(self.lado_do_quadrado)
  
  @staticmethod
  def area_quadrado(l):
    return l*l

  def perímetro(self):
    return self.perímetro_círculo(self.raio)
  
  @staticmethod
  def perímetro_círculo(r):
    return 2*pi*r


class Juice_Rancho(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Roxo(Juice_Rancho):

	def noofsides(self):
		print("Estou entre uva e tamarindo!")

class Amarelo(Juice_Rancho):

  def noofsides(self):
    print("Posso ser literalmente qualquer fruta!")

class Marrom(Juice_Rancho):

	def noofsides(self):
		print("Você jamais saberá de onde eu vim!")

class Verde(Juice_Rancho):

	def noofsides(self):
		print("É limão ou abacaxi?")

print('')

print(Breakfast_Rancho.domingo())
print(Breakfast_Rancho.segunda())
print(Breakfast_Rancho.terça())

print('')

p = Playing_with_math(8, 5, 7)
print('A área do quadrado é ',p.area(),'!', sep='')
print('O fatorial calculado é ',p.fatorial(),'!', sep='')
print('O peírmetro do círculo é ',p.perímetro(),'!', sep='')

print('')

R = Roxo()
R.noofsides()
V = Verde()
V.noofsides()
A = Amarelo()
A.noofsides()

print('')

