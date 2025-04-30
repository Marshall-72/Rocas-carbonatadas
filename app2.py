import streamlit as st
import matplotlib.pyplot as plt

# Diccionario con los datos de las muestras
muestras = {
    "Caliza de Tacna": {
        "dunham": "Mudstone",
        "folk": "Micrite",
        "ambiente": "Marino somero"
    },
    "Caliza de Puno": {
        "dunham": "Wackestone",
        "folk": "Biomicrite",
        "ambiente": "Marino somero"
    },
    "Caliza de Puno con fósil": {
        "dunham": "Packstone",
        "folk": "Fossiliferous micrite",
        "ambiente": "Marino somero"
    },
    "Marga de Tacna": {
        "dunham": "Mudstone",
        "folk": "Marl",
        "ambiente": "Lagunar"
    },
    "Halita": {
        "dunham": "No aplica",
        "folk": "Evaporita",
        "ambiente": "Ambiente árido"
    },
    "Yeso": {
        "dunham": "No aplica",
        "folk": "Evaporita",
        "ambiente": "Ambiente árido"
    },
    "Coquina": {
        "dunham": "Grainstone",
        "folk": "Biomicrite",
        "ambiente": "Playa o mar somero"
    },
    "Baritina": {
        "dunham": "No aplica",
        "folk": "Sulfato",
        "ambiente": "Hidrotermal"
    }
}

st.title("Comparador de Rocas Carbonatadas y Evaporíticas")

seleccionadas = st.multiselect("Selecciona las muestras a comparar:", list(muestras.keys()))

if len(seleccionadas) >= 2:
    # Recuento para gráficos
    dunham_count = {}
    folk_count = {}
    ambiente_count = {}

    for nombre in seleccionadas:
        data = muestras[nombre]

        dunham = data["dunham"]
        dunham_count[dunham] = dunham_count.get(dunham, 0) + 1

        folk = data["folk"]
        folk_count[folk] = folk_count.get(folk, 0) + 1

        ambiente = data["ambiente"]
        ambiente_count[ambiente] = ambiente_count.get(ambiente, 0) + 1

    # Función para gráfico de barras
    def plot_bar_chart(data_dict, title, xlabel):
        fig, ax = plt.subplots()
        ax.bar(data_dict.keys(), data_dict.values(), color='skyblue')
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Cantidad")
        plt.xticks(rotation=30, ha='right')
        st.pyplot(fig)

    st.subheader("Clasificación textural según Dunham (1962)")
    plot_bar_chart(dunham_count, "Clasificación Dunham", "Tipo de textura")

    st.subheader("Clasificación de rocas calcáreas según Folk (1974)")
    plot_bar_chart(folk_count, "Clasificación Folk", "Tipo Folk")

    st.subheader("Ambiente de depósito")
    plot_bar_chart(ambiente_count, "Ambientes sedimentarios", "Ambiente")

else:
    st.info("Selecciona al menos dos muestras para comparar.")

