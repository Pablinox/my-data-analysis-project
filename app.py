import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header('Graficos con informacion de vehiculos')

st.write('elige el tipo de grafico que deseas visualizar')

hist_button = st.button('histograma de los kilómetros recorridos')
if hist_button:
    st.write('Histograma de los kilómetros recorridos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

scatter_button = st.button(
    'Gráfico de dispersión precio vs kilómetros recorridos')
if scatter_button:
    st.write('Gráfico de dispersión de precio vs kilómetros recorridos')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)

scatter_button = st.button('Gráfico de dispersión precio vs Modelo')
if scatter_button:
    st.write('Gráfico de dispersión de precio vs Modelo')
    fig = px.scatter(car_data, x='model_year', y='price')
    st.plotly_chart(fig)
