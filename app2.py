import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de las rocas
rocas = [
    {"Roca": "Caliza de Tacna", "Mineral Principal": "Calcita", "Composición": "Carbonato", "Porosidad": "Media", "Textura": "Granular", "Solubilidad en Ácido Clorhídrico": "Alta", "Presencia de Fósiles": "No", "Color": "Blanco"},
    {"Roca": "Caliza de Puno", "Mineral Principal": "Calcita", "Composición": "Carbonato", "Porosidad": "Media", "Textura": "Granular", "Solubilidad en Ácido Clorhídrico": "Alta", "Presencia de Fósiles": "No", "Color": "Blanco"},
    {"Roca": "Caliza de Puno (con fósil)", "Mineral Principal": "Calcita", "Composición": "Carbonato", "Porosidad": "Alta", "Textura": "Fósilífera", "Solubilidad en Ácido Clorhídrico": "Alta", "Presencia de Fósiles": "Sí", "Color": "Blanco"},
    {"Roca": "Marga de Tacna", "Mineral Principal": "Calcita", "Composición": "Carbonato", "Porosidad": "Media", "Textura": "Granular", "Solubilidad en Ácido Clorhídrico": "Alta", "Presencia de Fósiles": "No", "Color": "Gris"},
    {"Roca": "Halita", "Mineral Principal": "Halita", "Composición": "Sal", "Porosidad": "Alta", "Textura": "Masiva", "Solubilidad en Ácido Clorhídrico": "Alta", "Presencia de Fósiles": "No", "Color": "Translúcido"},
    {"Roca": "Yeso", "Mineral Principal": "Yeso", "Composición": "Sulfato", "Porosidad": "Baja", "Textura": "Masiva", "Solubilidad en Ácido Clorhídrico": "Baja", "Presencia de Fósiles": "No", "Color": "Blanco"},
    {"Roca": "Coquina", "Mineral Principal": "Calcita", "Composición": "Carbonato", "Porosidad": "Alta", "Textura": "Fósilífera", "Solubilidad en Ácido Clorhídrico": "Alta", "Presencia de Fósiles": "Sí", "Color": "Blanco"},
    {"Roca": "Baritina", "Mineral Principal": "Baritina", "Composición": "Sulfato", "Porosidad": "Baja", "Textura": "Masiva", "Solubilidad en Ácido Clorhídrico": "Baja", "Presencia de Fósiles": "No", "Color": "Blanco"}
]

# Convertir los datos a listas para facilitar la visualización en gráficos
minerales = [roca["Mineral Principal"] for roca in rocas]
composiciones = [roca["Composición"] for roca in rocas]
porosidades = [roca["Porosidad"] for roca in rocas]
fosiles = [roca["Presencia de Fósiles"] for roca in rocas]

# Configuración de la interfaz en Streamlit
st.title("Clasificación de Rocas Carbonatadas y Evaporíticas")
st.write("Este es un sistema de clasificación de rocas carbonatadas y evaporíticas basado en características típicas.")

# Mostrar tabla con las características de las rocas
st.subheader("Características de las Rocas:")
st.write("Roca - Mineral Principal - Composición - Porosidad - Textura - Solubilidad en Ácido Clorhídrico - Presencia de Fósiles - Color")
for roca in rocas:
    st.write(f"{roca['Roca']} - {roca['Mineral Principal']} - {roca['Composición']} - {roca['Porosidad']} - {roca['Textura']} - {roca['Solubilidad en Ácido Clorhídrico']} - {roca['Presencia de Fósiles']} - {roca['Color']}")

# Gráfico comparativo de "Mineral Principal"
st.subheader("Distribución de Rocas por Mineral Principal")
fig, ax = plt.subplots()
sns.countplot(x=minerales, ax=ax)
ax.set_title("Distribución de Rocas por Mineral Principal")
ax.set_xlabel("Mineral Principal")
ax.set_ylabel("Cantidad de Rocas")
st.pyplot(fig)

# Gráfico comparativo de "Composición"
st.subheader("Distribución de Rocas por Composición")
fig, ax = plt.subplots()
sns.countplot(x=composiciones, ax=ax)
ax.set_title("Distribución de Rocas por Composición")
ax.set_xlabel("Composición")
ax.set_ylabel("Cantidad de Rocas")
st.pyplot(fig)

# Gráfico comparativo de "Porosidad"
st.subheader("Distribución de Rocas por Porosidad")
fig, ax = plt.subplots()
sns.countplot(x=porosidades, ax=ax)
ax.set_title("Distribución de Rocas por Porosidad")
ax.set_xlabel("Porosidad")
ax.set_ylabel("Cantidad de Rocas")
st.pyplot(fig)

# Gráfico comparativo de "Presencia de Fósiles"
st.subheader("Distribución de Rocas por Presencia de Fósiles")
fig, ax = plt.subplots()
sns.countplot(x=fosiles, ax=ax)
ax.set_title("Distribución de Rocas por Presencia de Fósiles")
ax.set_xlabel("Presencia de Fósiles")
ax.set_ylabel("Cantidad de Rocas")
st.pyplot(fig)

# Resumen general
st.subheader("Resumen General")
st.write("Este análisis permite observar la distribución de las 8 muestras de rocas según diversas características como el mineral principal, composición, porosidad y la presencia de fósiles. Los gráficos comparativos facilitan la visualización de las propiedades de las rocas estudiadas.")
