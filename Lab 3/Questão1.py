# Modelo de padaria usando Fábrica Abstrata

import random 
  
class Padaria: 
   
    def __init__(self, sabores_de_bolo = None): 
        
      self.sabores_de_bolo = sabores_de_bolo 
  
    def exibir_compra(self):

      bolo = self.sabores_de_bolo()

      print(f'Obrigado, você escolheu o bolo de {bolo} para seu/sua {bolo.evento()}!\n') 

# Cada sabor de bolo tem um evento específico relacionado (por exemplo, bolo de chocolate é somente para aniversário)  
  
class chocolate: 
    
    def evento(self): 
        return "festa de aniversário"
  
    def __str__(self): 
        return "chocolate"
  
class mandioca: 

    def evento(self): 
        return "festa informal"
  
    def __str__(self): 
        return "mandioca"
  
class cenoura:     
  
    def evento(self): 
        return "casamento"
  
    def __str__(self): 
        return 'cenoura'

class baunilha:     
  
    def evento(self): 
        return "festa surpresa"
  
    def __str__(self): 
        return 'baunilha'

class floresta_negra:     
  
    def evento(self): 
        return "festa da firma"
  
    def __str__(self): 
        return 'floresta negra'
  
def escolha_randomica_de_bolo(): 
  
    return random.choice([cenoura, mandioca, chocolate, baunilha, floresta_negra])() 
  
  
if __name__ == "__main__": 
  
    bolo = Padaria(escolha_randomica_de_bolo)

    print('\nÚltimas notas fiscais da Padaria CES-22!\n') 
  
    for i in range(5): 
        bolo.exibir_compra() 