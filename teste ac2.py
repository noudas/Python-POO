# ARQUIVO DE TESTE PARA A ATIVIDADE CONTÍNUA 02
# Este arquivo não deve ser modificado.


# Importa as classes do módulo ac02
from ac02 import Socio, Clube


# Testa a criação dos objetos da classe Sócio
try:
    # Criação do primeiro Sócio
    m1 = Socio('Paulo', '10/09/1990', '649.943.670-43', 1, 2020)
    assert m1.nome == 'Paulo'
    assert m1.nascimento == '10/09/1990'
    assert m1.cpf == '649.943.670-43'
    assert m1.mes == 1
    assert m1.ano == 2020

    # Criação do segundo Sócio
    m2 = Socio('Ana', '14/12/1995', '918.199.320-01', 2, 2020)
    assert m2.nome == 'Ana'
    assert m2.nascimento == '14/12/1995'
    assert m2.cpf == '918.199.320-01'
    assert m2.mes == 2
    assert m2.ano == 2020

    # Criação dos outros Sócios do clube
    m3 = Socio('Maria', '14/01/2002', '770.046.380-81', 3, 2020)
    m4 = Socio('Vinicius', '14/05/1989', '682.194.070-34', 4, 2020)
    m5 = Socio('Guilherme', '14/02/1987', '001.655.780-84', 3, 2020)
    m6 = Socio('Ruan', '14/10/2000', '157.550.560-64', 1, 2019)
    m7 = Socio('Caroline', '14/09/2001', '548.428.380-94', 1, 2018)
    m8 = Socio('Fernanda', '14/09/2005', '023.126.550-63', 3, 2020)
    m9 = Socio('Zé', '14/07/1990', '012.308.030-41', 3, 2020)
except AssertionError:
    print('ERRO...: valor dos atributos dos objetos da classe Socio')
except Exception:
    print('ERRO...: criação dos objetos da classe Socio')
else:
    print('CORRETO: criação dos objetos da classe Socio')


# Testa a criação do objeto Clube
try:
    clube = Clube()
    # Verifica se a lista de sócios foi inicializada como vazia
    assert clube.socios == []
except AssertionError:
    print('ERRO...: lista de socios do clube deve iniciar vazia')
except Exception:
    print('ERRO...: criação do objeto da classe Clube')
else:
    print('CORRETO: criação do objeto da classe Clube')


# Testa a associação dos sócios ao clube
try:
    clube.associar(m1)
    assert len(clube.socios) == 1              # clube possui 1 sócio
    # verifica se armazenou objeto do tipo correto na lista
    assert type(clube.socios[0]) == Socio
    assert clube.socios[0].nome == 'Paulo'

    clube.associar(m2)
    assert len(clube.socios) == 2              # clube possui 2 sócios
    # verifica se armazenou objeto do tipo correto na lista
    assert type(clube.socios[1]) == Socio
    assert clube.socios[1].nome == 'Ana'

    clube.associar(m3)
    clube.associar(m4)
    clube.associar(m5)
    clube.associar(m6)
    clube.associar(m7)
    clube.associar(m8)
    clube.associar(m9)
    assert len(clube.socios) == 9              # clube possui 9 sócios
except AssertionError:
    print('ERRO...: método associar')
except Exception:
    print('ERRO...: método associar implementado com erro')
else:
    print('CORRETO: método associar')


# Testa o método numero_de_socios
try:
    # clube possui 9 sócios
    assert clube.numero_de_socios() == 9

    # insere um novo sócio
    m10 = Socio('Pedro', '091.974.110-00', '14/12/1999', 7, 2018)
    clube.associar(m10)

    # clube possui 10 sócios
    assert clube.numero_de_socios() == 10
except AssertionError:
    print('ERRO...: método numero_de_socios não retornou resultado correto')
except Exception:
    print('ERRO...: método numero_de_socios implementado com erro')
else:
    print('CORRETO: método numero_de_socios')


# Testa o método mes_associacao
try:
    assert clube.mes_associacao(3, 2020) == 4
    assert clube.mes_associacao(1, 2019) == 1
    assert clube.mes_associacao(10, 2020) == 0
except AssertionError:
    print('ERRO...: método mes_associacao não retornou resultado correto')
except Exception:
    print('ERRO...: método mes_associacao implementado com erro')
else:
    print('CORRETO: método mes_associacao')


# Testa validação do mês no método mes_associacao
try:
    clube.mes_associacao(0, 2020)
    clube.mes_associacao(13, 2020)
except ValueError:
    print('CORRETO: gerou exceção ValueError para mês inválido no \
método mes_associacao')
except Exception:
    print('ERRO...: não gerou exceção ValueError para mês inválido no \
método mes_associacao')
else:
    print('ERRO...: não gerou exceção ValueError para mês inválido no \
método mes_associacao')


# Testa validação do ano no método mes_associacao
try:
    clube.mes_associacao(3, 20)
    clube.mes_associacao(3, 9)
    clube.mes_associacao(3, 20201)
except TypeError:
    print('CORRETO: gerou exceção TypeError para ano inválido no \
método mes_associacao')
except Exception:
    print('ERRO...: não gerou exceção TypeError para ano inválido no \
método mes_associacao')
else:
    print('ERRO...: não gerou exceção TypeError para ano inválido no \
método mes_associacao')


# Testa o método expulsar
try:
    assert clube.expulsar(3, 2020) == ('Fernanda', 'Guilherme', 'Maria', 'Zé')
    assert clube.numero_de_socios() == 6

    assert clube.expulsar(1, 2018) == ('Caroline',)
    assert clube.numero_de_socios() == 5

    assert clube.expulsar(10, 2020) == ()
    assert clube.numero_de_socios() == 5
except AssertionError:
    print('ERRO...: método expulsar não retornou tupla correta ou não \
removeu socios corretamente')
except Exception:
    print('ERRO...: método expulsar implementado com erro')
else:
    print('CORRETO: método expulsar')


# Testa validação do mês no método expulsar
try:
    assert clube.expulsar(0, 2020) == []
    assert clube.expulsar(13, 2020) == []
except ValueError:
    print('CORRETO: gerou exceção ValueError para mês inválido no \
método expulsar')
except Exception:
    print('ERRO...: não gerou exceção ValueError para mês inválido no \
método expulsar')
else:
    print('ERRO...: não gerou exceção ValueError para mês inválido no \
método expulsar')


# Testa validação do ano no método expulsar
try:
    assert clube.expulsar(3, 20) == []
    assert clube.expulsar(3, 9) == []
    assert clube.expulsar(3, 20201) == []
except TypeError:
    print('CORRETO: gerou exceção TypeError para ano inválido no \
método expulsar')
except Exception:
    print('ERRO...: não gerou exceção TypeError para ano inválido no \
método expulsar')
else:
    print('ERRO...: não gerou exceção TypeError para ano inválido no \
método expulsar')
