import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Función para la clasificación de Dunham (1962)
def clasificar_textura_dunham(grano_fino, grano_grueso, porcentaje_limoso):
    if porcentaje_limoso >= 50:
        return "Limoso"
    if grano_fino > grano_grueso:
        return "Lime Mudstone"
    if grano_fino == grano_grueso:
        return "Limestone"
    return "Lime Wackestone"

# Función para la clasificación de rocas calcareas según Folk (1974)
def clasificar_roca_folk(cemento, matriz, grano):
    if cemento > 60:
        return "Caliza Cementada"
    if matriz > 50:
        return "Lime Mudstone"
    if grano > 30:
        return "Grano Limoso"
    return "Lime Wackestone"

# Datos de ejemplo (muestras)
muestras = {
    'Muestra': ['Caliza Tacna', 'Caliza Puno', 'Caliza Puno con fósil', 'Marga Tacna', 'Halita', 'Yeso', 'Coquina', 'Baritina'],
    'Grano_fino': [20, 15, 25, 5, 0, 0, 50, 10], # % de grano fino
    'Grano_grueso': [70, 75, 60, 90, 100, 100, 30, 80], # % de grano grueso
    'Porcentaje_limoso': [10, 10, 10, 5, 0, 0, 20, 10], # % de limo
    'Cemento': [40, 60, 55, 70, 0, 0, 10, 50],  # Cemento
    'Matriz': [50, 40, 35, 20, 0, 0, 60, 30],  # Matriz
    'Grano': [10, 5, 10, 10, 0, 0, 30, 20]  # Grano
}

# Convertir a DataFrame
df_muestras = pd.DataFrame(muestras)

# Clasificación textural según Dunham (1962)
df_muestras['Clasificación Textural'] = df_muestras.apply(
    lambda row: clasificar_textura_dunham(row['Grano_fino'], row['Grano_grueso'], row['Porcentaje_limoso']), axis=1)

# Clasificación según Folk (1974)
df_muestras['Clasificación Folk'] = df_muestras.apply(
    lambda row: clasificar_roca_folk(row['Cemento'], row['Matriz'], row['Grano']), axis=1)

# Mostrar tabla con las clasificaciones
st.write("Clasificación de Rocas Carbonatadas y Evaporíticas")
st.dataframe(df_muestras)

# Gráficos Comparativos sobre los tipos de ambiente de las rocas
st.subheader("Gráfico Comparativo: Clasificación Textural según Dunham (1962)")
fig, ax = plt.subplots()
df_muestras['Clasificación Textural'].value_counts().plot(kind='bar', ax=ax, color='skyblue')
ax.set_title('Distribución de Clasificación Textural de Rocas')
ax.set_ylabel('Cantidad')
ax.set_xlabel('Clasificación Textural')
st.pyplot(fig)

st.subheader("Gráfico Comparativo: Clasificación según Folk (1974)")
fig, ax = plt.subplots()
df_muestras['Clasificación Folk'].value_counts().plot(kind='bar', ax=ax, color='lightcoral')
ax.set_title('Distribución de Clasificación de Rocas según Folk (1974)')
ax.set_ylabel('Cantidad')
ax.set_xlabel('Clasificación Folk')
st.pyplot(fig)

# Información adicional sobre ambientes
ambientes = {
    'Ambiente': ['Submarino', 'Costeros', 'Lagos', 'Desértico'],
    'Muestra': ['Caliza Tacna', 'Caliza Puno', 'Halita', 'Yeso']
}

df_ambientes = pd.DataFrame(ambientes)
st.write("Ambientes de las Rocas")
st.dataframe(df_ambientes)

# Graficar ambientes
st.subheader("Gráfico Comparativo: Tipos de Ambiente de las Rocas")
fig, ax = plt.subplots()
df_ambientes['Ambiente'].value_counts().plot(kind='bar', ax=ax, color='lightgreen')
ax.set_title('Distribución de Ambientes de las Rocas')
ax.set_ylabel('Cantidad')
ax.set_xlabel('Ambiente')
st.pyplot(fig)
