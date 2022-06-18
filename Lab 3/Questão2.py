# Modelo de padaria usando Construtor

class Bolo: 
  
    def __init__(self): 
        self.evento() 
  
    def evento(self): 
        raise NotImplementedError 
  
    def __repr__(self): 
        return 'Evento : {evento}'.format(self) 


class Chocolate(Bolo):  
  
    def evento(self): 
        self.evento = "festa de aniversário"
  
    def __str__(self): 
        return "chocolate"


class Mandioca(Bolo): 
   
    def evento(self): 
        self.evento = "festa informal"
  
    def __str__(self): 
        return "mandioca"


class Cenoura(Bolo): 
    
    def evento(self): 
        self.evento = "casamento"
  
    def __str__(self): 
        return "cenoura"


class Baunilha(Bolo): 
    
    def evento(self): 
        self.evento = "festa surpresa"
  
    def __str__(self): 
        return "baunilha"


class Floreta_Negra(Bolo): 
    
    def evento(self): 
        self.evento = "festa da firma"
  
    def __str__(self): 
        return "floresta negra"

class Bolo_Sonho_de_Valsa: 
  
    def __repr__(self): 
        return 'Evento para o bolo sonho de valsa : {0.evento}'.format(self) 

  
class Bolo_Sonho_de_Valsa(Bolo_Sonho_de_Valsa): 
  
    def evento(self): 
        self.evento = "Fim de semestre"
  

def construtor_de_bolos(x): 
  
    bolo = x() 
    bolo.evento() 
  
    return bolo  


if __name__ == "__main__": 
  
    chocolate = Chocolate()  
    mandioca = Mandioca()  
    cenoura = Cenoura()  
    baunilha = Baunilha()
    floresta_negra = Floreta_Negra() 
  
    bolo_sonho_de_valsa = construtor_de_bolos(Bolo_Sonho_de_Valsa)
    print("\nExemplo 'Construtor' para a Padaria CES-22 :\n")
    print(bolo_sonho_de_valsa) 
    print("\n")