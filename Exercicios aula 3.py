# Exercicio 1

class Pessoa:
                
        def __init__(self,nome,idade):
                        
                self.nome = nome
                self.idade = idade
                self.carro = ""

        def comprar_carro(self,a):
                        
                self.carro = a


class Carro:
                
        def __init__(self,marca,modelo,placa,ano):
                        
                self.marca = marca
                self.modelo = modelo
                self.placa = placa
                self.ano = ano

        
# Exercicio 2

class Pedido:
                
        def __init__(self):

                self.produto = []
                        

        def adicionar_produto(self,a):

                self.produto.append(a)

        def calcular_valor(self):

                soma = 0
                for i in self.produto:
                        preco = i.preco * i.quant
                        soma += preco
                return soma
                
                


class Produto:

        def __init__(self,nome,preco,quant):

                self.nome = nome
                self.preco = preco
                self.quant = quant



# Exercicio 3


class Carro2:
        
        def __init__(self, pneu1, pneu2, pneu3, pneu4):
                self.ligado = False
                self.pneu1 = pneu1
                self.pneu2 = pneu2
                self.pneu3 = pneu3
                self.pneu4 = pneu4

        def ligar(self):
                
                self.ligado = True

        def desligar(self):
                
                self.ligado = False

        
        def verificar_pneu(self):
                
                if self.ligado == True:
                    print("STALIN FALOU QUE A pressão do pneu 1: ", self.pneu1.pressao)
                    print("STALIN FALOU QUE A pressão do pneu 2: ", self.pneu2.pressao)
                    print("STALIN FALOU QUE A pressão do pneu 3: ", self.pneu3.pressao)
                    print("STALIN FALOU QUE A pressão do pneu 4: ", self.pneu4.pressao)
                else:
                    print("O CARRO TA DESLIGADA SUA CARALHA")

class Pneu:

        def __init__(self, pressao):
                
                self.pressao = pressao

        def furar(self):
                self.pressao = 0


p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)
meucarro = Carro2(p1, p2, p3, p4)
meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu()       # exibir a pressão de cada pneu.
meucarro.desligar()
meucarro.verificar_pneu()       # exibir mensagem que o carro está desligado

