from math import sqrt
import funcoes_uteis as fu

t_student = 2.306

def calcula_correlacao_pearson(lista_x, lista_y):

    RXY = fu.calcula_SXY(lista_x,lista_y) / sqrt((fu.calcula_SXX(lista_x)*fu.calcula_SYY(lista_y)))

    return RXY

def  calcula_teste_coeficiente_correlacao(n,rxy):

    tc = rxy * sqrt((n-2)/(1-rxy**2))

    return tc

def testa_hipotese_coeficiente_correlacao(tc):

    H0 = "não há correlação linear entre x e y"
    H1 = "há correlação linear entre x e y"

    if -t_student < tc < t_student:
        return H0
    else:
        return H1

def calcula_equacao_regressao(lista_x,lista_y):

    x_media = fu.media(lista_x)
    y_media = fu.media(lista_y)

    b = round(fu.calcula_b(lista_x,lista_y),3);

    a = round(y_media - (b * x_media),3)

    equacao_reta = "Y = " + str(a) + " + " + str(b) + "xi"

    return equacao_reta

def calcula_teste_significancia_rl(lista_x,lista_y):

    n = len(lista_x)

    SXX = fu.calcula_SXX(lista_x)
    SYY = fu.calcula_SYY(lista_y)
    SXY = fu.calcula_SXY(lista_x,lista_y)

    b = round(fu.calcula_b(lista_x, lista_y), 3)

    S = sqrt((SYY - b * SXY) / (n - 2))

    tc =(b/S) * sqrt(SXX)

    return tc

def testa_coeficiente_de_regressão_linear(tc):

    H0 = "não existe regressão linear"
    H1 = "existe regressão linear"

    if -t_student < tc < t_student:
        return H0
    else:
        return H1