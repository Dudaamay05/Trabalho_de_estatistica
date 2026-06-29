import streamlit as st
import grafico as g
import funcoes_uteis as fu
import calculos as c
from math import sqrt

st.title("Calculadora de Correlação e Regressão Linear:")
st.write("Insira valores para x e y abaixo para verificar sua correlação e regressão")
x = st.text_area("X:")
y = st.text_area("Y:")

if st.button("Calcular"):

    lista_x = fu.converte_lista(x)
    lista_y = fu.converte_lista(y)

    #A.Calcular o coeficiente de correlação Pearson
    st.markdown("### A.Calculo do Coeficiente de Correlação Pearson")

    st.latex(r"r_{xy}=\frac{S_{XY}}{\sqrt{S_{XX}S_{YY}}}")

    sxy = round(fu.calcula_SXY(lista_x, lista_y), 3)
    sxx = round(fu.calcula_SXX(lista_x), 3)
    syy = round(fu.calcula_SYY(lista_y), 3)

    st.latex(rf"r_{{xy}}=\frac{{{sxy}}}{{\sqrt{{{sxx}\cdot{syy}}}}}")

    rxy = round(c.calcula_correlacao_pearson(lista_x, lista_y), 4)

    st.latex(rf"r_{{xy}}={rxy}")

    st.divider()

    #B.Teste Para o coeficiente de correlação Pearson
    st.markdown("### B.Teste do Coeficiente de Correlação Pearson ao nível de 5%")


    st.markdown("##### -> Hipóteses:")
    st.write("H0: p = 0 (não há correlação linear entre x e y")
    st.write("H1: p ≠ 0 (há correlação linear entre x e y")

    st.markdown("##### -> Significância, graus de liberdade , t crítico:")
    n = len(lista_x)
    gl = n - 2
    t = c.t_student

    st.latex(rf"\alpha = 0.05 \quad gl={gl} \quad t= \pm {t}")

    st.markdown("##### -> Encontrar o tc:")

    st.latex(r"t_c=r\frac{\sqrt{n-2}}{\sqrt{1-r^2}}")
    st.latex(rf"t_c=\frac{{{rxy}\sqrt{{{n}-2}}}}{{\sqrt{{1-{rxy}^2}}}}")

    tc = round(c.calcula_teste_coeficiente_correlacao(n,rxy),3)
    st.latex(rf"t_c={tc}")

    hipotese = c.testa_hipotese_coeficiente_correlacao(tc)
    st.success(hipotese)

    st.divider()

    #C.Ajustar a equação de regressão linear simples
    st.markdown("### C.Equação da reta estimada:")

    st.latex(r"\hat{Y}=a+bX")
    st.markdown("##### Em que:")
    st.latex(r"a =\bar{y} - b.\bar{x}")
    st.latex(r"b=\frac{S_{xy}}{S_{xx}}")

    st.markdown("##### Calculando b e a:")

    b = round(fu.calcula_b(lista_x, lista_y),3)
    st.latex(rf"b=\frac{{{sxy}}}{{{sxx}}}")
    st.latex(rf"b={b}")

    x = fu.media(lista_x)
    y = fu.media(lista_y)
    a = round(y - b*x,3)
    st.latex(rf"a={y} - {b}*{x}")
    st.latex(rf"a={a}")

    st.markdown("##### Equação da reta:")
    equacao = c.calcula_equacao_regressao(lista_x, lista_y)
    st.latex(rf"{equacao}")

    st.divider()

    # D.Testar a significância da regressão ao nível de 5%
    st.markdown("### D.Teste para o Coeficiente de Regressão Linear:")

    st.markdown("##### ->Hipóteses:")
    st.write("H0: não existe regressão linear")
    st.write("H1: existe regressão linear")

    st.markdown("##### -> Significância, graus de liberdade , t-student:")
    st.latex(rf"\alpha = 0.05 \quad gl={gl} \quad t= \pm {t}")

    st.markdown("##### -> Calcular o valor da variável de teste:")

    st.latex(r"t_c=\frac{b}{S}\sqrt{S_{xx}}")
    st.markdown("##### Em que:")
    st.latex(r"S=\frac{\sqrt{S_{yy}-bS_{xy}}}{\sqrt{n-2}}")

    st.markdown("##### Substituindo:")

    st.latex(rf"S=\frac{{\sqrt{{{syy}-{b}\cdot{sxy}}}}}{{\sqrt{{{n}-2}}}}")
    S = round(sqrt((syy- b * sxy) / (n-2)),3)
    st.latex(rf"S={S}")

    st.latex(rf"t_c=\frac{{{b}}}{{{S}}}\sqrt{{{sxx}}}")
    tc_rl = round(c.calcula_teste_significancia_rl(lista_x, lista_y),3)
    st.latex(rf"t_c={tc_rl}")

    hipotese_rl = c.testa_coeficiente_de_regressão_linear(tc_rl)
    st.success(hipotese_rl)

    st.divider()

    # E.Interpretar os resultados no contexto  do Curso de de Sistemas de informação
    st.markdown("### E.conclusão:")

    g.grafico_de_dispersao(lista_x, lista_y, a, b)

    with st.container(border=True):
        st.write("Com base nos resultados obtidos, conclui-se que existe uma correlação linear positiva entre o número de horas de "
                 "programação e a nota final obtida pelos 10 estudantes na disciplina de Desenvolvimento de Software.O coeficiente "
                 "de Pearson indica que essa relação é forte e o teste de hipóteses mostra que ela é estatisticamente significativa"
                 "ao nível de 5% de significância.Além disso, é possível notar que as variáveis x e y sofrem acréscimos na mesma "
                 "direção,isto é, à medida que o número de horas de programação aumenta, a nota final também tende a aumentar.")







