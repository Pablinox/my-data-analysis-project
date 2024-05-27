import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    'C:/Users/pablo/Documents/my-data-analysis-project/vehicles_us.csv')

st.header('Cuadro de mandos de análisis de vehículos')

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
