import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import streamlit as st

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

# Energía de ambiente (con valores numéricos entre 1-10)
energia_ambiente = {
    "Caliza de Tacna": 7,
    "Caliza de Puno": 6,
    "Caliza con fósil": 5,
    "Marga de Tacna": 6,
    "Halita": 9,
    "Yeso": 9,
    "Coquina": 4,
    "Baritina": 8
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
def graficar_categorizacion(titulo, datos, rotar_ejes=False):
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

    # Rotar las etiquetas del eje X si es necesario
    if rotar_ejes:
        plt.xticks(rotation=45, ha="right")

    ax.text(0.5, -0.25, 'Fuente: Cutipa C. Jaramillo A. Quenaya F. Amaro M.', 
            horizontalalignment='center', verticalalignment='center', 
            transform=ax.transAxes, fontsize=8)
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

# Función para graficar regresión lineal con la descripción debajo del gráfico
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
    
    # Fuente debajo del gráfico
    ax.text(0.5, -0.15, 'Fuente: Cutipa C. Jaramillo A. Quenaya F. Amaro M.', 
            horizontalalignment='center', verticalalignment='center', 
            transform=ax.transAxes, fontsize=8)

    st.pyplot(fig)

    # Descripción y análisis del gráfico de regresión lineal
    st.markdown("""
    **Descripción y análisis del gráfico de regresión lineal:**

    > La regresión lineal compara la energía del ambiente con los valores categóricos asignados a los tipos de ambiente de formación. Aunque la relación no es perfectamente lineal, se observa una **tendencia positiva**, lo que indica que ambientes más energéticos (como playas o plataformas someras) tienden a estar asociados a valores más altos en la escala de energía asignada. Esto es coherente con la clasificación ambiental de las rocas seleccionadas.
    """)

# Función para graficar la regresión entre energía de ambiente y clasificación Dunham
def regresion_energia_clasificacion_dunham():
    # Extraer datos para la regresión
    x = [energia_ambiente[muestra] for muestra in muestras_seleccionadas]
    y = [mapear_clasificacion(clasificacion_dunham)[0].get(clasificacion_dunham[muestra], 0) 
         for muestra in muestras_seleccionadas]

    # Llamar la función para graficar
    graficar_regresion_lineal(x, y, "Regresión entre Energía de Ambiente y Clasificación Dunham")


# ---- Sección de preguntas interpretativas ----
st.markdown("---")
st.header("Preguntas interpretativas")

preguntas_respuestas = {
    "¿Cómo se pueden identificar los tres elementos texturales: armazón, matriz y cemento? ¿Por su color, tamaño, etc.?":
        "El armazón se identifica como los granos más grandes y visibles, la matriz como el material fino entre estos granos, y el cemento como el material que une los granos. Se pueden diferenciar por tamaño, forma, y en ocasiones color o brillo bajo el microscopio.",
    
    "Si se tiene una roca denominada caliza aloquímica microcristalina, ¿qué tipo de ambiente deposicional pudo tener?":
        "Ambientes de baja energía, posiblemente lagunas o plataformas carbonatadas protegidas, donde se favorece la deposición de partículas finas como micrita.",
    
    "¿Qué tipos de rocas calcáreas se generan en ambientes de baja energía? ¿Y en ambientes de alta energía? Explique.":
        "En ambientes de baja energía se forman micritas y wackestones, con partículas finas y abundante matriz. En ambientes de alta energía se forman grainstones y packstones, con granos bien seleccionados y poco o nada de matriz.",
    
    "Sitúe en una clasificación triangular los siguientes tipos de rocas:\n- Calizas aloquímicas esparíticas.\n- Calizas aloquímicas microcristalinas.\n- Calizas microcristalinas micríticas.":
        "Estas calizas se ubican según la proporción de allochem (componentes aloquímicos), matriz micrítica y cemento esparítico. Las esparíticas irían hacia el vértice de cemento, las microcristalinas al de matriz, y las aloquímicas al de componentes.",
    
    "De acuerdo con la naturaleza de los componentes aloquímicos, indique una clasificación que involucre:\n- Intraclastos.\n- Oolitos.\n- Pellets y fósiles.":
        "Las rocas se clasifican como intraclásticass, oolíticas, pelletal o bioclásticas dependiendo del componente dominante. Ej: una roca con oolitos será una caliza oolítica.",
    
    "¿En qué difiere la clasificación para rocas calcáreas de Dunham y de Folk?":
        "La clasificación de Dunham se basa en la textura y en cómo están ligados los granos, útil en campo; la de Folk considera los componentes minerales y es más detallada, útil en laboratorio.",
    
    "¿En qué tipo de ambiente sedimentario se puede encontrar una roca tipo Grainstone?":
        "En ambientes de alta energía como playas o barras de arena, donde la corriente elimina la matriz fina y permite la acumulación de granos limpios.",
    
    "Si una roca presenta ooides, ¿esto ayuda a inferir que se formó en un ambiente de alta o baja energía?":
        "Alta energía, ya que los ooides se forman por recubrimientos concéntricos de carbonato debido al movimiento constante en aguas agitadas.",
    
    "Si una roca presenta alto contenido de micrita, ¿a qué tipo de ambiente podemos referirnos?":
        "Ambientes de baja energía, como lagunas restringidas o zonas protegidas de plataformas carbonatadas, donde se acumulan partículas finas.",
    
    "¿Qué importancia tienen las rocas carbonatadas en la generación y acumulación de hidrocarburos?":
        "Son excelentes rocas reservorio por su porosidad secundaria y fracturas. Además, pueden actuar como roca generadora si tienen materia orgánica, especialmente en ambientes anóxicos marinos."
}

# Barra desplegable para seleccionar y mostrar pregunta + respuesta
pregunta_seleccionada = st.selectbox("Selecciona una pregunta para ver su respuesta:", list(preguntas_respuestas.keys()))
st.markdown(f"**Pregunta:** {pregunta_seleccionada}")
st.markdown(f"**Respuesta:** {preguntas_respuestas[pregunta_seleccionada]}")


# Interfaz principal
st.title("Comparación de Clasificaciones de Rocas Carbonatadas y Evaporíticas")

muestras_seleccionadas = st.multiselect("Selecciona las muestras a comparar:", muestras, default=muestras)

if muestras_seleccionadas:
    st.subheader("Clasificación según Dunham (1962)")
    graficar_categorizacion("Clasificación Dunham", {k: v for k, v in clasificacion_dunham.items() if k in muestras_seleccionadas}, rotar_ejes=True)

    st.subheader("Clasificación según Folk (1974)")
    graficar_categorizacion("Clasificación Folk", {k: v for k, v in clasificacion_folk.items() if k in muestras_seleccionadas}, rotar_ejes=True)

    st.subheader("Ambiente de Formación")
    graficar_categorizacion("Ambiente de Formación", {k: v for k, v in ambiente_formacion.items() if k in muestras_seleccionadas}, rotar_ejes=True)

    st.subheader("Energía del Ambiente")
    graficar_energia_ambiente()

    # Añadir la regresión lineal entre energía de ambiente y clasificación Dunham
    st.subheader("Regresión entre Energía de Ambiente y Clasificación Dunham")
    regresion_energia_clasificacion_dunham()

else:
    st.warning("Por favor selecciona al menos una muestra para continuar.")

