#superclasse
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_barulho(self):
        print('O animal fez barulho!!!!')
        
class Cachorro(Animal):# super classe
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.raca = raca
    
    def abana_rabo(self):
        print('Abanando o rabo')
        
class Gato(Animal):
    def ronronar(self):
        print('O', self.nome,'esta ronronando')
        
cachorro1 = Cachorro('Pitt', 4,'chalchal')
cachorro1.fazer_barulho()
cachorro1.abana_rabo()