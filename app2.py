import streamlit as st
import matplotlib.pyplot as plt

# Datos simulados de 8 muestras de rocas carbonatadas y evaporíticas
muestras = [
    {
        "nombre": "Caliza de Tacna",
        "tipo_particula": {"grava": 5, "arena": 90, "lodo": 5},
        "componentes": {"armazon": 70, "matriz": 20, "cemento": 5, "porosidad": 5},
        "color": "blanco", "color_alteracion": "amarillo",
        "minerales": {"calcita": 90, "arcilla": 5, "dolomita": 5}
    },
    {
        "nombre": "Caliza de Puno",
        "tipo_particula": {"grava": 10, "arena": 80, "lodo": 10},
        "componentes": {"armazon": 75, "matriz": 15, "cemento": 5, "porosidad": 5},
        "color": "beige", "color_alteracion": "gris",
        "minerales": {"calcita": 85, "arcilla": 10, "dolomita": 5}
    },
    {
        "nombre": "Caliza de Puno con fósil",
        "tipo_particula": {"grava": 15, "arena": 75, "lodo": 10},
        "componentes": {"armazon": 80, "matriz": 10, "cemento": 5, "porosidad": 5},
        "color": "amarillo", "color_alteracion": "blanco sucio",
        "minerales": {"calcita": 88, "arcilla": 7, "dolomita": 5}
    },
    {
        "nombre": "Marga de Tacna",
        "tipo_particula": {"grava": 0, "arena": 30, "lodo": 70},
        "componentes": {"armazon": 50, "matriz": 40, "cemento": 5, "porosidad": 5},
        "color": "gris", "color_alteracion": "verde",
        "minerales": {"calcita": 50, "arcilla": 40, "dolomita": 5, "otros": 5}
    },
    {
        "nombre": "Halita",
        "tipo_particula": {"grava": 80, "arena": 15, "lodo": 5},
        "componentes": {"armazon": 90, "matriz": 5, "cemento": 5, "porosidad": 5},
        "color": "blanco", "color_alteracion": "naranja",
        "minerales": {"halita": 100}
    },
    {
        "nombre": "Yeso",
        "tipo_particula": {"grava": 10, "arena": 80, "lodo": 10},
        "componentes": {"armazon": 70, "matriz": 25, "cemento": 5, "porosidad": 5},
        "color": "blanco", "color_alteracion": "amarillo claro",
        "minerales": {"yeso": 100}
    },
    {
        "nombre": "Coquina",
        "tipo_particula": {"grava": 90, "arena": 5, "lodo": 5},
        "componentes": {"armazon": 60, "matriz": 30, "cemento": 5, "porosidad": 5},
        "color": "blanco", "color_alteracion": "ocre",
        "minerales": {"calcita": 95, "fragmentos_biológicos": 5}
    },
    {
        "nombre": "Baritina",
        "tipo_particula": {"grava": 60, "arena": 30, "lodo": 10},
        "componentes": {"armazon": 85, "matriz": 10, "cemento": 5, "porosidad": 5},
        "color": "gris claro", "color_alteracion": "amarillo",
        "minerales": {"baritina": 100}
    }
]

# Interfaz Streamlit
st.title("Comparación de Muestras de Rocas Carbonatadas y Evaporíticas")

muestras_nombres = [m["nombre"] for m in muestras]
seleccionadas = st.multiselect("Selecciona muestras para comparar:", muestras_nombres, default=muestras_nombres[:2])

# Filtro de datos
muestras_filtradas = [m for m in muestras if m["nombre"] in seleccionadas]

# Gráfico de distribución de tamaño de partículas
if muestras_filtradas:
    fig, ax = plt.subplots(figsize=(10, 6))
    ancho = 0.2
    x = range(len(muestras_filtradas))

    for i, comp in enumerate(["grava", "arena", "lodo"]):
        valores = [m["tipo_particula"][comp] for m in muestras_filtradas]
        ax.bar([v + ancho*i for v in x], valores, width=ancho, label=comp)

    ax.set_xticks([v + ancho for v in x])
    ax.set_xticklabels([m["nombre"] for m in muestras_filtradas], rotation=45)
    ax.set_ylabel("Porcentaje (%)")
    ax.set_title("Distribución de Tamaño de Partículas")
    ax.legend()
    st.pyplot(fig)

    # Gráfico de composición mineral
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ancho = 0.2
    x = range(len(muestras_filtradas))

    for i, comp in enumerate(["calcita", "arcilla", "dolomita", "halita", "yeso", "baritina"]):
        valores = [m["minerales"].get(comp, 0) for m in muestras_filtradas]
        ax2.bar([v + ancho*i for v in x], valores, width=ancho, label=comp)

    ax2.set_xticks([v + ancho*1.5 for v in x])
    ax2.set_xticklabels([m["nombre"] for m in muestras_filtradas], rotation=45)
    ax2.set_ylabel("Porcentaje (%)")
    ax2.set_title("Composición Mineral de las Muestras")
    ax2.legend()
    st.pyplot(fig2)

    # Tabla resumen
    st.write("### Resumen de Composición Mineral")
    for m in muestras_filtradas:
        st.write(f"**{m['nombre']}**")
        st.write(m["minerales"])

# Lista de preguntas y respuestas predefinidas
preguntas_respuestas = {
    "¿Qué diferencias hay entre la caliza de Tacna y la caliza de Puno?": 
        {"respuestas": [
            "La caliza de Tacna tiene una mayor proporción de calcita, mientras que la de Puno tiene más arcilla, lo que puede influir en su color y durabilidad.",
            "La principal diferencia radica en la textura, siendo la caliza de Tacna más homogénea y la de Puno con una mayor variabilidad.",
            "La caliza de Puno incluye fósiles, lo que le otorga características paleontológicas adicionales que la caliza de Tacna no posee."
        ],
        "palabras_clave": ["caliza", "Tacna", "Puno"]},
    
    "¿En qué se diferencia la coquina de otras rocas carbonatadas?": 
        {"respuestas": [
            "La coquina está formada principalmente por fragmentos biológicos cementados, lo que le otorga una textura distintiva frente a otras rocas carbonatadas.",
            "A diferencia de las calizas, la coquina tiene una alta proporción de fragmentos biológicos como conchas y esqueletos marinos.",
            "La coquina tiene una estructura gruesa y porosa, a diferencia de las calizas más compactas."
        ],
        "palabras_clave": ["coquina", "carbonatadas", "biológicos"]},
}

# Mostrar preguntas frecuentes
st.write("### Preguntas Frecuentes")
for pregunta, contenido in preguntas_respuestas.items():
    st.write(f"**{pregunta}**")
    for respuesta in contenido["respuestas"]:
        st.write(f"- {respuesta}")

