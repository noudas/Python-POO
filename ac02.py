# ATIVIDADE CONTÍNUA 02

# NOMES DOS ALUNOS
# ALUNO 1: Jonathan Kahan


class Clube:
    def __init__(self):

        self.socios = []

    def associar(self, socio):
        self.socios.append(socio)

    def numero_de_socios(self):
        return len(self.socios)

    def mes_associacao(self, mes, ano):
        count = 0
        if mes < 1 or mes > 12:
            raise ValueError("O mês deve estar entre 1 e 12")
        if len(str(ano)) < 4:
            raise TypeError("O ano deve conter apenas 4 digitos")
        for socio in self.socios:
            if mes == socio.mes and ano == socio.ano:
                count += 1
        return count

    def expulsar(self, mes, ano):
        tupla = []
        if mes < 1 or mes > 12:
            raise ValueError("O mês deve estar entre 1 e 12")
        if len(str(ano)) < 4:
            raise TypeError("O ano deve conter apenas 4 digitos")
        i = 0
        while i < len(self.socios):
            if self.socios[i].mes == mes and self.socios[i].ano == ano:
                tupla.append(self.socios[i].nome)
                del self.socios[i]
            else:
                i += 1
            tupla.sort()
        tupla = tuple(tupla)
        return tupla


class Socio:

    def __init__(self, nome, nascimento, cpf, mes, ano):

        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.mes = mes
        self.ano = ano
