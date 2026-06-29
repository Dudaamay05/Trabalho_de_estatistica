import matplotlib.pyplot as plt
import streamlit as st

def grafico_de_dispersao(lista_x,lista_y,a,b):

    fig_grafico, dados_grafico = plt.subplots()

    dados_grafico.scatter(lista_x,lista_y)

    dados_grafico.set_title("Horas de programação vs Nota final de 10 estudantes")
    dados_grafico.set_xlabel("Horas de Programação")
    dados_grafico.set_ylabel("Nota Final")

    dados_grafico.grid(True)

    y_reta = []
    for x in lista_x:
        y_reta.append(a + b * x)

    dados_grafico.plot(lista_x,y_reta)

    st.pyplot(fig_grafico)