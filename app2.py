import streamlit as st
import matplotlib.pyplot as plt

# Títulos y selección
st.title("Comparación de Rocas Carbonatadas y Evaporíticas")

# Lista de muestras
muestras = [
    "Caliza de Tacna", "Caliza de Puno", "Caliza de Puno con fósil", "Marga de Tacna",
    "Halita", "Yeso", "Coquina", "Baritina"
]

# Datos simulados (debes reemplazarlos con datos reales si tienes)
composicion = {
    "Carbonatos": [90, 85, 88, 60, 0, 0, 70, 0],
    "Evaporitas": [0, 0, 0, 0, 95, 90, 0, 80]
}

textura_dunham = {
    "Mudstone": [1, 0, 0, 1, 0, 0, 0, 0],
    "Wackestone": [0, 1, 0, 0, 0, 0, 0, 0],
    "Packstone": [0, 0, 1, 0, 0, 0, 0, 0],
    "Evaporítica": [0, 0, 0, 0, 1, 1, 0, 1],
    "Coquina": [0, 0, 0, 0, 0, 0, 1, 0]
}

ambientes = {
    "Amb. marino somero": [1, 1, 1, 1, 0, 0, 1, 0],
    "Amb. evaporítico": [0, 0, 0, 0, 1, 1, 0, 1]
}

# Selección de muestras
seleccion = st.multiselect("Selecciona las muestras que deseas comparar:", muestras, default=muestras)

# Filtrar índices seleccionados
indices = [muestras.index(m) for m in seleccion]

# Plot 1: Composición
st.subheader("1. Composición Mineralógica")
fig1, ax1 = plt.subplots()
bar_width = 0.35
x = range(len(seleccion))
ax1.barh(x, [composicion["Carbonatos"][i] for i in indices], bar_width, label='Carbonatos')
ax1.barh([i + bar_width for i in x], [composicion["Evaporitas"][i] for i in indices], bar_width, label='Evaporitas')
ax1.set_yticks([i + bar_width / 2 for i in x])
ax1.set_yticklabels(seleccion)
ax1.set_xlabel('%')
ax1.legend()
st.pyplot(fig1)

# Plot 2: Clasificación textural (Dunham, 1962)
st.subheader("2. Clasificación Textural (Dunham, 1962)")
fig2, ax2 = plt.subplots()
texturas = list(textura_dunham.keys())
for i, textura in enumerate(texturas):
    valores = [textura_dunham[textura][j] for j in indices]
    ax2.barh(range(len(seleccion)), valores, left=[x + i for x in [0]*len(seleccion)], label=textura)
ax2.set_yticks(range(len(seleccion)))
ax2.set_yticklabels(seleccion)
ax2.set_xlabel("Presencia (1 = Sí)")
ax2.legend()
st.pyplot(fig2)

# Plot 3: Ambientes sedimentarios
st.subheader("3. Ambiente Sedimentario")
fig3, ax3 = plt.subplots()
ambs = list(ambientes.keys())
bar_width = 0.35
x = range(len(seleccion))
ax3.bar(x, [ambientes["Amb. marino somero"][i] for i in indices], bar_width, label='Marino somero')
ax3.bar([i + bar_width for i in x], [ambientes["Amb. evaporítico"][i] for i in indices], bar_width, label='Evaporítico')
ax3.set_xticks([i + bar_width / 2 for i in x])
ax3.set_xticklabels(seleccion, rotation=30, ha='right')
ax3.set_ylabel("Presencia (1 = Sí)")
ax3.legend()
st.pyplot(fig3)

