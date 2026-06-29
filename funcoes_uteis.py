def converte_lista(text):
    list_aux = text.split(",")
    lista = []
    for valor in list_aux:
        lista.append(float(valor))
    return lista

def somatorio(valores):
    soma = 0
    for valor in valores:
        soma += valor
    return soma

def multiplica_valores(a,b):
    lista_mult = []
    for i in range (len(a)):
        lista_mult.append(a[i]*b[i])
    return lista_mult

def media(lista):
    media = somatorio(lista) / len(lista)
    return media

def calcula_SXX(lista_x):

    x2 = multiplica_valores(lista_x, lista_x)
    SXX = somatorio(x2) - ((somatorio(lista_x) ** 2) / len(lista_x))

    return SXX

def calcula_SYY(lista_y):

    y2 = multiplica_valores(lista_y, lista_y)
    SYY = somatorio(y2) - ((somatorio(lista_y) ** 2) / len(lista_y))

    return SYY

def calcula_SXY(lista_x,lista_y):

    yx = multiplica_valores(lista_y, lista_x)
    SXY = somatorio(yx) - ((somatorio(lista_x) * somatorio(lista_y)) / len(lista_x))

    return SXY

def calcula_b(lista_x,lista_y):

    b = calcula_SXY(lista_x,lista_y) / calcula_SXX(lista_x)

    return b
