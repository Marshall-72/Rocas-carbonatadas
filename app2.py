import streamlit as st
import matplotlib.pyplot as plt

# Funciones de clasificación textural según Dunham (1962)
def clasificar_textura_dunham(grano_fino, grano_grueso, porcentaje_limoso):
    if porcentaje_limoso >= 50:
        return "Limoso"
    if grano_fino > grano_grueso:
        return "Lime Mudstone"
    if grano_fino == grano_grueso:
        return "Limestone"
    return "Lime Wackestone"

# Función para la clasificación de rocas calcareas según Folk (1974)
def clasificar_roca_folk(cemento, matriz, grano):
    if cemento > 60:
        return "Caliza Cementada"
    if matriz > 50:
        return "Lime Mudstone"
    if grano > 30:
        return "Grano Limoso"
    return "Lime Wackestone"

# Datos de ejemplo (muestras)
muestras = [
    {'Muestra': 'Caliza Tacna', 'Grano_fino': 20, 'Grano_grueso': 70, 'Porcentaje_limoso': 10, 'Cemento': 40, 'Matriz': 50, 'Grano': 10},
    {'Muestra': 'Caliza Puno', 'Grano_fino': 15, 'Grano_grueso': 75, 'Porcentaje_limoso': 10, 'Cemento': 60, 'Matriz': 40, 'Grano': 5},
    {'Muestra': 'Caliza Puno con fósil', 'Grano_fino': 25, 'Grano_grueso': 60, 'Porcentaje_limoso': 10, 'Cemento': 55, 'Matriz': 35, 'Grano': 10},
    {'Muestra': 'Marga Tacna', 'Grano_fino': 5, 'Grano_grueso': 90, 'Porcentaje_limoso': 5, 'Cemento': 70, 'Matriz': 20, 'Grano': 10},
    {'Muestra': 'Halita', 'Grano_fino': 0, 'Grano_grueso': 100, 'Porcentaje_limoso': 0, 'Cemento': 0, 'Matriz': 0, 'Grano': 0},
    {'Muestra': 'Yeso', 'Grano_fino': 0, 'Grano_grueso': 100, 'Porcentaje_limoso': 0, 'Cemento': 0, 'Matriz': 0, 'Grano': 0},
    {'Muestra': 'Coquina', 'Grano_fino': 50, 'Grano_grueso': 30, 'Porcentaje_limoso': 20, 'Cemento': 10, 'Matriz': 60, 'Grano': 30},
    {'Muestra': 'Baritina', 'Grano_fino': 10, 'Grano_grueso': 80, 'Porcentaje_limoso': 10, 'Cemento': 50, 'Matriz': 30, 'Grano': 20}
]

# Clasificación según Dunham (1962) y Folk (1974)
for muestra in muestras:
    muestra['Clasificación Textural'] = clasificar_textura_dunham(muestra['Grano_fino'], muestra['Grano_grueso'], muestra['Porcentaje_limoso'])
    muestra['Clasificación Folk'] = clasificar_roca_folk(muestra['Cemento'], muestra['Matriz'], muestra['Grano'])

# Mostrar los resultados de las clasificaciones
st.write("Clasificación de Rocas Carbonatadas y Evaporíticas")
for muestra in muestras:
    st.write(f"Muestra: {muestra['Muestra']}")
    st.write(f"Clasificación Textural (Dunham, 1962): {muestra['Clasificación Textural']}")
    st.write(f"Clasificación Folk (1974): {muestra['Clasificación Folk']}")
    st.write("")

# Gráficos comparativos de las clasificaciones
textural_counts = {'Limoso': 0, 'Lime Mudstone': 0, 'Limestone': 0, 'Lime Wackestone': 0}
folk_counts = {'Caliza Cementada': 0, 'Lime Mudstone': 0, 'Grano Limoso': 0, 'Lime Wackestone': 0}

# Contar las frecuencias
for muestra in muestras:
    textural_counts[muestra['Clasificación Textural']] += 1
    folk_counts[muestra['Clasificación Folk']] += 1

# Gráfico de clasificación textural según Dunham (1962)
st.subheader("Gráfico Comparativo: Clasificación Textural según Dunham (1962)")
fig, ax = plt.subplots()
ax.bar(textural_counts.keys(), textural_counts.values(), color='skyblue')
ax.set_title('Distribución de Clasificación Textural de Rocas')
ax.set_ylabel('Cantidad')
ax.set_xlabel('Clasificación Textural')
st.pyplot(fig)

# Gráfico de clasificación según Folk (1974)
st.subheader("Gráfico Comparativo: Clasificación según Folk (1974)")
fig, ax = plt.subplots()
ax.bar(folk_counts.keys(), folk_counts.values(), color='lightcoral')
ax.set_title('Distribución de Clasificación de Rocas según Folk (1974)')
ax.set_ylabel('Cantidad')
ax.set_xlabel('Clasificación Folk')
st.pyplot(fig)

# Información adicional sobre ambientes
ambientes = [
    {'Ambiente': 'Submarino', 'Muestra': 'Caliza Tacna'},
    {'Ambiente': 'Costeros', 'Muestra': 'Caliza Puno'},
    {'Ambiente': 'Lagos', 'Muestra': 'Halita'},
    {'Ambiente': 'Desértico', 'Muestra': 'Yeso'}
]

# Mostrar los ambientes
st.write("Ambientes de las Rocas")
for ambiente in ambientes:
    st.write(f"Muestra: {ambiente['Muestra']} - Ambiente: {ambiente['Ambiente']}")

# Gráfico de ambientes
st.subheader("Gráfico Comparativo: Tipos de Ambiente de las Rocas")
ambient_counts = {'Submarino': 0, 'Costeros': 0, 'Lagos': 0, 'Desértico': 0}

# Contar las frecuencias de ambientes
for ambiente in ambientes:
    ambient_counts[ambiente['Ambiente']] += 1

# Graficar los ambientes
fig, ax = plt.subplots()
ax.bar(ambient_counts.keys(), ambient_counts.values(), color='lightgreen')
ax.set_title('Distribución de Ambientes de las Rocas')
ax.set_ylabel('Cantidad')
ax.set_xlabel('Ambiente')
st.pyplot(fig)
