import streamlit as st
import matplotlib.pyplot as plt

# Datos de ejemplo (puedes modificarlos según tus muestras reales)
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

# Función para obtener los valores únicos y mapear a números para eje Y

def mapear_clasificacion(diccionario):
    categorias = list(sorted(set(diccionario.values())))
    if "N/A" in categorias:
        categorias.remove("N/A")
        categorias.append("N/A")  # para que "N/A" vaya al final
    mapa = {cat: i for i, cat in enumerate(categorias)}
    return mapa, categorias

# Función para graficar clasificaciones

def graficar_categorizacion(titulo, datos):
    mapa, categorias = mapear_clasificacion(datos)
    x = []
    y = []
    colores = []
    etiquetas = []

    for i, muestra in enumerate(muestras):
        categoria = datos.get(muestra, "N/A")
        if categoria != "N/A":
            x.append(muestra)
            y.append(mapa[categoria])
            colores.append(i)
            etiquetas.append(categoria)

    fig, ax = plt.subplots()
    ax.scatter(x, y, c=colores, cmap='tab10', s=100)
    ax.set_yticks(list(mapa.values()))
    ax.set_yticklabels(categorias)
    ax.set_xlabel("Muestras")
    ax.set_title(titulo)
    ax.grid(True, axis='y', linestyle='--', alpha=0.4)
    st.pyplot(fig)

# Interfaz principal
st.title("Comparación de Clasificaciones de Rocas Carbonatadas y Evaporíticas")

muestras_seleccionadas = st.multiselect("Selecciona las muestras a comparar:", muestras, default=muestras)

if muestras_seleccionadas:
    st.subheader("Clasificación según Dunham (1962)")
    graficar_categorizacion("Clasificación Dunham", {k: v for k, v in clasificacion_dunham.items() if k in muestras_seleccionadas})

    st.subheader("Clasificación según Folk (1974)")
    graficar_categorizacion("Clasificación Folk", {k: v for k, v in clasificacion_folk.items() if k in muestras_seleccionadas})

    st.subheader("Ambiente de Formación")
    graficar_categorizacion("Ambiente de Formación", {k: v for k, v in ambiente_formacion.items() if k in muestras_seleccionadas})
else:
    st.warning("Por favor selecciona al menos una muestra para comparar.")

