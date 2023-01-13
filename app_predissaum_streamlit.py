import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.set_page_config(
    page_title='Predissaum',
    page_icon='📊',
    layout='wide',#centered
    initial_sidebar_state='expanded', #collapsed
    menu_items={
        'Get help':'https://www.google.com/',
        'Report a bug':'https://www.google.com/',
        'About':'DA & ML'
    }
)

dados = pd.read_csv('logsDiarios.csv')
#dados

max = len(dados['value'])

#d = dados.where(dados['index'] < 5) ---> gera NaN
d1 = dados.loc[(dados['index'] < 5)]
d1

with st.sidebar:
    st.subheader('menu de opções para alternar entre as possibilidades das combinações de redes')
    col1, col2 = st.columns(2)

    with col1:
        camada1 = st.selectbox(
            'Primeira Camada',
            options=['LSTM','GRU'])

    with col2:
        camada2 = st.selectbox(
            'Segunda Camada',
            options=['LSTM','GRU'])
    
    qtd_neuro = st.selectbox(
            'Quantidade de Neuronios',
            options=['camada1 = 56 | camada2 = 32','camada1 = 81 | camada2 = 27'])
    
    st.subheader('seletor linha (2 pontos)')
    inter_min, inter_max = st.slider('escolha a qtd de unidades', 1,max,(1,max))
    st.write('intervalo escolhido: ', inter_min, inter_max)


st.subheader('combinassaum do grafico da base vs o predito')
linhaA = alt.Chart(dados).mark_line(
    #point=alt.OverlayMarkDef(color='green',size=50,filled=False,fill='red'),
    color='lightgreen'
).encode(
    x = alt.X('index'),
    y = alt.Y('value'),
    tooltip=['index','value']
).properties(
    width=600,
    height=300,
    title = 'valores mensais'
)
st.altair_chart(linhaA,use_container_width=True)


st.subheader('download da imagem')

st.subheader('grafico comparando a taxa de acerto')
