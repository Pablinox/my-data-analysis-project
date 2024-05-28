import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header('Graficos con infromacion importante de vehiculos')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Histograma de los kilómetros recorridos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Gráfico de dispersión de precio vs kilómetros recorridos')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Gráfico de dispersión de precio vs Modelo')
    fig = px.scatter(car_data, x='model_year', y='price')
    st.plotly_chart(fig)
