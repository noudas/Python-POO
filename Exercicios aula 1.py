# Exercicio 1

class Livro:
    
    def __init__(self):
            
            # Atributos
            
        self.titulo = None
        self.autor = None
        self.quantidade_paginas = None




# Exercicio 2
        
class Triangulo:
    
    def __init__(self, lado_a, lado_b, lado_c):
            
            # Atributos
            
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

            # Metodos

    def calcular_perimetro(self):
        p = self.lado_a + self.lado_b + self.lado_c
        print("O perímetro do triângulo é: %.1f" %p)


# Exercicio 3


class Televisao:
    
    def __init__(self):
            
            # Atributos
            
        self.canal = None
        self.volume = 0

            # Metodos

    def aumentar_volume(self):
        if self.volume < 101:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > -1: 
            self.volume -= 1

    def alterar_canal(self,a):
        self.canal = a




# Exercicio 4


class Funcionario:
    
    def __init__(self):
            
            # Atributos
            
        self.nome = None
        self.salario = 0

            # Metodos

    def aumentar_salario(self,a):
        self.salario = (a/100)*self.salario + self.salario
        print("Seu salario e: %.2f" %self.salario)



# Exercicio 5


class Carro:
    
    def __init__(self):

            
            # Atributos

            
        self.quantidade_combustivel = 0


            # Metodos

    def adicionar_combustivel(self,a):
        self.quantidade_combustivel += a
            
            
    def andar(self,km):
        self.quantidade_combustivel = -(km * 0.2) + self.quantidade_combustivel

    def obter_combustivel(self):
        return self.quantidade_combustivel
