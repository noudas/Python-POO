#Exercicio 1

class Carro:
    
    def __init__(self, marca, modelo, placa):

        # Atributos

        self.marca = marca
        self.modelo = modelo
        self.placa = placa



        # Metodos

    def exibir_dados(self):
        a = self.marca
        b = self.modelo
        c = self.placa
        print(a,b,c)


        
#Exercicio 2

class Funcionario:
    
    def __init__(self, nome, sobrenome, salario_mensal):

        # Atributos
        
        if salario_mensal <=0:
            salario_mensal = 0
            self.salario_mensal = salario_mensal
        else:
            self.salario_mensal = salario_mensal

        
        self.nome = nome
        self.sobrenome = sobrenome


    # Metodos
    
    def aumentar_salario(self):
        self.salario_mensal += self.salario_mensal * 0.1


    def salario_anual(self):
        salario = self.salario_mensal * 12
        print("Ö salario do funcionario anual e? %.2f"%salario)


#Exercicio 3

class ContaBancaria:
    
    def __init__(self, numero, titular, senha):

        # Atributos
        
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

        # Metodos

    def depositar(self, valor, senha):
        valor = valor
        senha = senha
        if senha != self.senha:
            print("senha incorreta")
        else:
            self.saldo += valor

        

    def sacar(self, valor, senha):
        valor = valor
        senha = senha
        if senha != self.senha:
            print("senha incorreta")
        else:
            self.saldo -= valor



#Exercicio 4

class Aluno:
    
    def __init__(self, ra, nome, turma):

        # Atributos
        
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.nota = 0
        self.count = 0


        # Metodos

    def inserir_nota(self, nota):
        nota = nota
        self.nota += nota
        self.count += 1


    def calcular_media(self):
        media = self.nota/self.count
        print(media)

a = []

alun1 = Aluno(1,"a","2c")
alun1.inserir_nota(10)
alun1.inserir_nota(9)
alun1.inserir_nota(8)
alun1.inserir_nota(7)
alun1.inserir_nota(6)
alun1.inserir_nota(5)



alun2 = Aluno(2,"b","2c")
alun2.inserir_nota(8)
alun2.inserir_nota(7)
alun2.inserir_nota(6)

alun3 = Aluno(3,"c","2c")
alun3.inserir_nota(8)
alun3.inserir_nota(7)

a.append(alun1)
a.append(alun2)
a.append(alun3)

for i in range(len(a)):
    a[i].calcular_media
