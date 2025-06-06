import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Anuncios de ventas de coches")

hist_button = st.button('Crear histograma')

if hist_button:

    st.write('Creacion de histograma para el conjunto de datos de anuncio de ventas de coches')
    
    fig = px.histogram(car_data, x="odometer") # crear un histograma
    fig.show()

    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Crear grafico de dispercion')

if disp_button:

    st.write('Creacion de grafico de dispercion para el conjunto de datos de anuncio de ventas de coches')
    
    fig1 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    fig1.show()

    st.plotly_chart(fig1, use_container_width=True)

