class Cliente:
    
   def __init__(self, nome):
       self.__nome = nome

   @property
   def nome(self): 
       print("chamando @property nome()")
       return self .__nome.title()


cliente = Cliente('nico')

cliente.nome