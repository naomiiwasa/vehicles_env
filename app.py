import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de anuncios de coches en USA')

# Checkbox para histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión odómetro vs precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
