import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Datos aproximados de la composición mineralógica de cada muestra
# Los valores son representaciones de la composición mineral (porcentaje aproximado de cada mineral)
samples_composition = {
    'Caliza de Tacna': {'calcita': 85, 'arcilla': 5, 'cuarzo': 7, 'otros': 3},
    'Caliza de Puno': {'calcita': 80, 'arcilla': 10, 'cuarzo': 5, 'otros': 5},
    'Caliza de Puno con fósil': {'calcita': 75, 'arcilla': 12, 'cuarzo': 8, 'otros': 5},
    'Marga de Tacna': {'calcita': 70, 'arcilla': 15, 'cuarzo': 10, 'otros': 5},
    'Halita': {'calcita': 10, 'arcilla': 5, 'cuarzo': 1, 'otros': 84},
    'Yeso': {'calcita': 5, 'arcilla': 3, 'cuarzo': 2, 'otros': 90},
    'Coquina': {'calcita': 95, 'arcilla': 0, 'cuarzo': 3, 'otros': 2},
    'Baritina': {'calcita': 30, 'arcilla': 2, 'cuarzo': 1, 'otros': 67}
}

# Configuración de la barra lateral para seleccionar las muestras a comparar
st.sidebar.title('Seleccionar Muestras a Comparar')
samples_list = list(samples_composition.keys())
selected_samples = st.sidebar.multiselect('Selecciona las muestras para comparar', samples_list, default=samples_list)

# Mostrar las muestras seleccionadas
st.write(f"Comparando las composiciones mineralógicas de las muestras seleccionadas:")

# Función para graficar la comparación
def plot_mineral_composition(selected_samples):
    # Preparar los datos
    categories = ['Calcita', 'Arcilla', 'Cuarzo', 'Otros']
    num_samples = len(selected_samples)
    
    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.2  # Ancho de las barras
    index = np.arange(len(categories))  # Las posiciones para las barras

    for i, sample in enumerate(selected_samples):
        composition = samples_composition[sample]
        ax.bar(index + i * bar_width, list(composition.values()), bar_width, label=sample)

    # Etiquetas y leyenda
    ax.set_xlabel('Minerales')
    ax.set_ylabel('Porcentaje (%)')
    ax.set_title('Composición Mineralógica de las Muestras')
    ax.set_xticks(index + bar_width * (num_samples / 2 - 0.5))
    ax.set_xticklabels(categories)
    ax.legend(title='Muestras', loc='upper left', bbox_to_anchor=(1, 1))
    
    # Fuente
    st.text("Fuente: Elaboración propia")
    
    # Mostrar el gráfico
    st.pyplot(fig)

# Graficar las muestras seleccionadas
plot_mineral_composition(selected_samples)
