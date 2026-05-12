import streamlit as st
import pandas as pd

## CARGA DE DATOS=====================================================================


ruta = 'data/ZNI.CSV' 
df = pd.read_csv(ruta)

##analisis de datos ==

filas = df.shape[0]
columnas = df.shape[1]

##visualizacion de datos===============================================================
##st.dataframe(df)
col1, col2 = st.columns(2)
with col1: 
    with st.container(border=True):
         st.subheader("Numero de filas")
         st.text(filas)
with col2:
        with st.container(border=True):
             st.subheader("Numero de columnas")
             st.text(columnas)
##Otra forma de mostrar los datos
col3, col4 = st.columns(2)
with col3:
    st.metric("Numero de filas", filas, border= True)
with col4:
    st.metric("Numero de columnas", columnas, border= True)

