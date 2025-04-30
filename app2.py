import streamlit as st
import matplotlib.pyplot as plt

# Datos de las muestras
muestras = {
    "Caliza de Tacna": {
        "textura_dunham": "Mudstone",
        "clasificacion_folk": "Micrita",
        "ambiente": "Marino somero"
    },
    "Caliza de Puno": {
        "textura_dunham": "Wackestone",
        "clasificacion_folk": "Biomicrita",
        "ambiente": "Plataforma carbonatada"
    },
    "Caliza de Puno con fósil": {
        "textura_dunham": "Packstone",
        "clasificacion_folk": "Biomicrita",
        "ambiente": "Plataforma interna"
    },
    "Marga de Tacna": {
        "textura_dunham": "Mudstone",
        "clasificacion_folk": "Micrita",
        "ambiente": "Laguna"
    },
    "Halita": {
        "textura_dunham": "Cristalina",
        "clasificacion_folk": "No aplica",
        "ambiente": "Evaporítico"
    },
    "Yeso": {
        "textura_dunham": "Cristalina",
        "clasificacion_folk": "No aplica",
        "ambiente": "Evaporítico"
    },
    "Coquina": {
        "textura_dunham": "Grainstone",
        "clasificacion_folk": "Biosparita",
        "ambiente": "Alta energía costera"
    },
    "Baritina": {
        "textura_dunham": "Cristalina",
        "clasificacion_folk": "No aplica",
        "ambiente": "Hidrotermal o evaporítico"
    }
}

st.title("Comparador de Rocas Carbonatadas y Evaporíticas")

seleccionadas = st.multiselect("Selecciona las muestras a comparar:", list(muestras.keys()))

# Colores por categoría (fijos para mantener consistencia)
colores_textura = {
    "Mudstone": "skyblue",
    "Wackestone": "orange",
    "Packstone": "green",
    "Grainstone": "purple",
    "Cristalina": "red"
}

colores_folk = {
    "Micrita": "blue",
    "Biomicrita": "orange",
    "Biosparita": "green",
    "No aplica": "gray"
}

colores_ambiente = {
    "Marino somero": "navy",
    "Plataforma carbonatada": "cyan",
    "Plataforma interna": "teal",
    "Laguna": "brown",
    "Evaporítico": "pink",
    "Alta energía costera": "gold",
    "Hidrotermal o evaporítico": "darkred"
}

def graficar_clasificacion(titulo, atributo, colores_dict):
    fig, ax = plt.subplots()
    categorias = list(colores_dict.keys())
    valores = {cat: [] for cat in categorias}
    muestras_x = seleccionadas

    for muestra in seleccionadas:
        cat = muestras[muestra][atributo]
        for c in categorias:
            valores[c].append(1 if c == cat else 0)

    for cat in categorias:
        ax.bar(muestras_x, valores[cat], label=cat, color=colores_dict[cat], bottom=[sum(valores[c][i] for c in list(valores.keys())[:list(valores.keys()).index(cat)]) for i in range(len(muestras_x))])

    ax.set_ylabel("Clasificación")
    ax.set_title(titulo)
    ax.set_xticks(range(len(muestras_x)))
    ax.set_xticklabels(muestras_x, rotation=45, ha="right")
    ax.legend(title="Categorías")
    st.pyplot(fig)

if seleccionadas:
    graficar_clasificacion("Clasificación Textural (Dunham, 1962)", "textura_dunham", colores_textura)
    graficar_clasificacion("Clasificación de Calizas (Folk, 1974)", "clasificacion_folk", colores_folk)
    graficar_clasificacion("Ambiente Sedimentario", "ambiente", colores_ambiente)
else:
    st.info("Selecciona al menos una muestra para visualizar los gráficos.")


