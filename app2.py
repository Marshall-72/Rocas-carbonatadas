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

# Nueva clasificación de energía del ambiente (escala 1-10)
energia_ambiente = {
    "Caliza de Tacna": 3,   # Baja energía
    "Caliza de Puno": 3,    # Baja energía
    "Caliza con fósil": 4,  # Baja energía
    "Marga de Tacna": 2,    # Baja energía
    "Halita": 9,            # Alta energía
    "Yeso": 8,              # Alta energía
    "Coquina": 7,           # Alta energía
    "Baritina": 6           # Moderada energía
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
def graficar_categorizacion(titulo, datos, etiquetas=None):
    mapa, categorias = mapear_clasificacion(datos)
    x = []
    y = []
    colores = []
    etiquetas_lista = []

    for i, muestra in enumerate(muestras):
        categoria = datos.get(muestra, "N/A")
        if categoria != "N/A" and muestra in muestras_seleccionadas:
            x.append(muestra)
            y.append(mapa[categoria])
            colores.append(i)
            etiquetas_lista.append(categoria)

    fig, ax = plt.subplots()
    ax.scatter(x, y, c=colores, cmap='tab10', s=100)
    ax.set_yticks(list(mapa.values()))
    ax.set_yticklabels(categorias)
    ax.set_xlabel("Muestras")
    ax.set_title(titulo)
    ax.grid(True, axis='y', linestyle='--', alpha=0.4)
    
    # Rotar las etiquetas del eje X
    plt.xticks(rotation=45, ha='right')
    
    # Añadir fuente debajo del gráfico
    ax.text(0.5, -0.25, 'Fuente: Cutipa C. Jaramillo A. Quenaya F. Amaro M.', 
            horizontalalignment='center', verticalalignment='center', 
            transform=ax.transAxes, fontsize=8)
    
    if etiquetas:
        for i, etiqueta in enumerate(etiquetas_lista):
            ax.annotate(etiqueta, (x[i], y[i]), fontsize=8, ha='center')
    
    st.pyplot(fig)

# Función para graficar energía del ambiente
def graficar_energia_ambiente():
    x = [muestra for muestra in muestras_seleccionadas]
    y = [energia_ambiente.get(muestra, 0) for muestra in muestras_seleccionadas]
    
    fig, ax = plt.subplots()
    scatter = ax.scatter(x, y, c=y, cmap='viridis', s=100)
    ax.set_xlabel("Muestras")
    ax.set_ylabel("Energía del ambiente (1-10)")
    ax.set_title("Energía del ambiente de las rocas")
    fig.colorbar(scatter, ax=ax, label='Energía')
    ax.grid(True, linestyle='--', alpha=0.4)
    
    # Rotar las etiquetas del eje X
    plt.xticks(rotation=45, ha='right')
    
    # Añadir fuente debajo del gráfico
    ax.text(0.5, -0.25, 'Fuente: Cutipa C. Jaramillo A. Quenaya F. Amaro M.', 
            horizontalalignment='center', verticalalignment='center', 
            transform=ax.transAxes, fontsize=8)
    
    st.pyplot(fig)
####################################################################################    
# Función para graficar regresión lineal
def graficar_regresion_lineal(x_data, y_data, titulo):
    # Calcular la regresión lineal
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
    
    # Crear los valores predichos de y basados en la regresión
    y_pred = slope * np.array(x_data) + intercept

    # Crear el gráfico de dispersión y la línea de regresión
    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, color='blue', label='Datos reales')
    ax.plot(x_data, y_pred, color='red', label=f'Regresión lineal: y={slope:.2f}x + {intercept:.2f}')
    
    # Añadir título y etiquetas
    ax.set_xlabel("Energía del ambiente (1-10)")
    ax.set_ylabel("Clasificación Dunham (Valor numérico)")
    ax.set_title(titulo)
    ax.grid(True, linestyle='--', alpha=0.4)
    
    # Añadir la ecuación y el valor R² en el gráfico
    ax.text(0.05, 0.95, f'$R^2$ = {r_value**2:.2f}', transform=ax.transAxes, fontsize=12, verticalalignment='top')
    
    # Añadir fuente debajo del gráfico
    ax.text(0.5, -0.15, 'Fuente: Cutipa C. Jaramillo A. Quenaya F. Amaro M.', 
            horizontalalignment='center', verticalalignment='center', 
            transform=ax.transAxes, fontsize=8)

    st.pyplot(fig)

# Función para graficar la regresión entre energía de ambiente y clasificación Dunham
def regresion_energia_clasificacion_dunham():
    # Extraer datos para la regresión
    x = [energia_ambiente[muestra] for muestra in muestras_seleccionadas]
    y = [mapear_clasificacion(clasificacion_dunham)[0].get(clasificacion_dunham[muestra], 0) 
         for muestra in muestras_seleccionadas]

    # Llamar la función para graficar
    graficar_regresion_lineal(x, y, "Regresión entre Energía de Ambiente y Clasificación Dunham")
################################################################################
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

    st.subheader("Energía del Ambiente")
    graficar_energia_ambiente()

else:
    st.warning("Por favor selecciona al menos una muestra para comparar.")
