class Aluno:
    def __init__(self,nome,curso,n1,n2,n3,):
        self.nome = nome
        self.curso = curso
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

        
        
    def apresentar(self):
        print('Ola , me chamo: ', self.nome)
        
    def notas(self):
        print('notas do aluno sao: ', self.n1, self.n2, self.n3)
        
    def verificar_media(self):
        media= (self.n1 + self.n2 + self.n3) /3
        if media > 7:
            print('APROVADO COM SUCESSO')
        else:
            print('ALUNO REPROVADO')
        
      
aluno1 = Aluno('Mary', 'adminitracao', 8, 6, 8)
aluno1.apresentar()
aluno1.notas()
aluno1.verificar_media()