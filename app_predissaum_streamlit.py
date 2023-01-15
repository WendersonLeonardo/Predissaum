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

dadosA = pd.read_csv('logsDiarios.csv')
dadosB = pd.read_csv('dados pred.csv')
df = pd.read_csv('erros predissaum.csv')

maxA = len(dadosA['index'])
maxB = len(dadosB['index'])
altura = 400

#d = dados.where(dados['index'] < 5) ---> gera NaN



st.header('Base')
def converter(df):
    return df.to_csv().encode('utf-8')

inter_minA, inter_maxA = st.slider('Selecione, caso deseje, um intervalo para a base abaixo', 1,maxA,(1,maxA))

linhaA = alt.Chart(dadosA.loc[(dadosA['index'] >= inter_minA)&(dadosA['index'] <= inter_maxA)]).mark_line(
    color='lightgreen'
).encode(
    x = alt.X('index'),
    y = alt.Y('value'),
    tooltip=['index','value']
).properties(
    width=600,
    height=altura,
    title = 'valores mensais'
)
st.altair_chart(linhaA,use_container_width=True)

st.download_button(
    label='baixar base.csv',
    data=converter(dadosA),
    file_name='base predissaum.csv',
    mime='text/csv  '
)

st.header('Root Mean Squared Error')
st.write('Erro Quadrático Médio')
barras = alt.Chart(df).mark_bar(width=10
).encode(x ='combinassaum', y ='error',
    color='combinassaum').properties(
    height=altura-20,
    width=700,
    title = 'taxa de erro'
)

rotuloB = barras.mark_text(
    dy = -11,
    size = 15
).encode(
    text='error')

st.altair_chart(barras+rotuloB)



#st.header()

st.subheader('Menu de opções para alternar entre as possibilidades das combinações de redes')

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

inter_minB, inter_maxB = st.slider('escolha o intervalo', 1,maxB,(1,maxB))

var = camada1 + ' vs ' + camada2 + ' - ' + qtd_neuro
st.subheader('Dado Original vs Predito: ' + var)


linhaB = alt.Chart(dadosB.loc[(dadosB['index'] >= inter_minB)&(dadosB['index'] <= inter_maxB)]).mark_line(
    color='lightgreen'
).encode(
    x = alt.X('index'),
    y = alt.Y('original'),
    tooltip=['index','original']
).properties(
    #width=700,
    height=altura+50
)

linhaC = alt.Chart(dadosB.loc[(dadosB['index'] >= inter_minB)&(dadosB['index'] <= inter_maxB)]).mark_line(
    color='lightblue'
).encode(
    x = alt.X('index'),
    y = alt.Y(var)
)

erro = df.loc[(df['combinassaum'] == var)]['error'][0]
st.info('RMSE: ' + str(erro))

st.altair_chart(linhaB+linhaC,use_container_width=True)
