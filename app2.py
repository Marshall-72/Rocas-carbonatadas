import streamlit as st
import matplotlib.pyplot as plt

# Datos
muestras = [
    "Caliza de Tacna",
    "Caliza de Puno",
    "Caliza con fósil",
    "Marga de Tacna",
    "Halita",
    "Yeso",
    "Coquina",
    "Baritina"
]

clasificacion_dunham = {
    "Caliza de Tacna": "Mudstone",
    "Caliza de Puno": "Wackestone",
    "Caliza con fósil": "Packstone",
    "Marga de Tacna": "Mudstone",
    "Halita": "N/A",
    "Yeso": "N/A",
    "Coquina": "Grainstone",
    "Baritina": "N/A"
}

clasificacion_folk = {
    "Caliza de Tacna": "Micrita",
    "Caliza de Puno": "Biomicrita",
    "Caliza con fósil": "Biopelsparita",
    "Marga de Tacna": "Micrita",
    "Halita": "N/A",
    "Yeso": "N/A",
    "Coquina": "Biosparita",
    "Baritina": "N/A"
}

ambiente_formacion = {
    "Caliza de Tacna": "Marino somero",
    "Caliza de Puno": "Marino somero",
    "Caliza con fósil": "Marino somero",
    "Marga de Tacna": "Marino somero",
    "Halita": "Ambiente evaporítico",
    "Yeso": "Ambiente evaporítico",
    "Coquina": "Playa/alto-energía",
    "Baritina": "Ambiente hidrotermal"
}

# Mapear categorías a números
def mapear_clasificacion(diccionario):
    categorias = list(sorted(set(diccionario.values())))
    if "N/A" in categorias:
        categorias.remove("N/A")
        categorias.append("N/A")
    mapa = {cat: i for i, cat in enumerate(categorias)}
    return mapa, categorias

# Función para graficar
def graficar_categorizacion(titulo, datos, muestras_filtradas):
    mapa, categorias = mapear_clasificacion(datos)
    x = []
    y = []
    colores = []

    for i, muestra in enumerate(muestras_filtradas):
        categoria = datos.get(muestra, "N/A")
        if categoria != "N/A":
            x.append(i)
            y.append(mapa[categoria])
            colores.append(i)

    fig, ax = plt.subplots(figsize=(max(6, len(muestras_filtradas)*0.9), 4))
    scatter = ax.scatter(x, y, c=colores, cmap='tab10', s=120)

    ax.set_xticks(range(len(muestras_filtradas)))
    ax.set_xticklabels(muestras_filtradas, rotation=30, ha='right')
    ax.set_yticks(list(mapa.values()))
    ax.set_yticklabels(categorias)
    ax.set_title(titulo)
    ax.set_xlabel("Muestras")
    ax.set_ylabel("Clasificación")
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    # Agregar fuente más abajo
    fig.text(0.5, -0.15, "Fuente: Cutipa C., Jaramillo A., Quenaya F., Amaro M.", ha='center', fontsize=9, style='italic')

    st.pyplot(fig)

# Interfaz
st.title("Comparación de Rocas Carbonatadas y Evaporíticas")

muestras_seleccionadas = st.multiselect("Selecciona las muestras a comparar:", muestras, default=muestras)

if muestras_seleccionadas:
    st.subheader("Clasificación según Dunham (1962)")
    graficar_categorizacion("Clasificación Dunham", clasificacion_dunham, muestras_seleccionadas)

    st.subheader("Clasificación según Folk (1974)")
    graficar_categorizacion("Clasificación Folk", clasificacion_folk, muestras_seleccionadas)

    st.subheader("Ambiente de Formación")
    graficar_categorizacion("Ambiente de Formación", ambiente_formacion, muestras_seleccionadas)
else:
    st.warning("Por favor selecciona al menos una muestra para comparar.")

