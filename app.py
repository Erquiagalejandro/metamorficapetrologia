import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de página
st.set_page_config(
    page_title="MetamorPETRO - Petrología Metamórfica",
    page_icon="🪨",
    layout="wide"
)

st.title("🪨 MetamorPETRO: Catálogo y Guía Metamórfica")
st.caption("Basado en recomendaciones de la IUGS (Subcommission on Metamorphic Rocks) y J.D. Winter (2010)")

# Menú lateral
menu = st.sidebar.radio(
    "Selecciona un módulo:",
    [
        " Catálogo de Texturas y Fábricas",
        " Clasificación de Rocas",
        " Facies y Diagrama P-T",
        " Minerales Índice y Protostos",
        " Guía de Nomenclatura IUGS"
    ]
)

# -----------------------------------------------------------------------------
# MÓDULO 1: TEXTURAS
# -----------------------------------------------------------------------------
if menu == " Catálogo de Texturas y Fábricas":
    st.header(" Catálogo de Texturas y Fábricas Metamórficas")
    
    texturas = {
        "Granoblástica": "Cristales de forma equigranular (mosaico o poligonal). Típica de rocas monominerales (cuarcitas, mármoles) o metamorfismo de contacto (hornfels).",
        "Nematoblástica": "Alineación preferencial de minerales prismáticos o aciculares (anfíboles, sillimanita). Define lineaciones minerales.",
        "Lepodoblástica": "Alineación paralela de minerales filosilicatados (micas, clorita). Define la esquistosidad.",
        "Porfidoblástica": "Cristales de gran tamaño (porfidoblastos: granate, estaurolita, cordierita) rodeados por una matriz de menor grano (blastecis).",
        "Poiquiloblástica": "Porfidoblastos que contienen numerosas inclusiones de minerales de la matriz (textura en 'nido de abeja' o 'tamiz').",
        "Milonítica / Cataclástica": "Producida por deformación dúctil/frágil en zonas de cizalla. Muestra porfiroclastos en una matriz milonítica con foliación de cizalla (S-C)."
    }
    
    col1, col2 = st.columns([1, 2])
    with col1:
        tex_sel = st.selectbox("Selecciona una textura:", list(texturas.keys()))
    with col2:
        st.subheader(tex_sel)
        st.write(texturas[tex_sel])

# -----------------------------------------------------------------------------
# MÓDULO 2: ROCAS
# -----------------------------------------------------------------------------
elif menu == " Clasificación de Rocas":
    st.header(" Clasificación e Identificación de Rocas")
    
    df_rocas = pd.DataFrame([
        {"Roca": "Pizarra", "Foliación": "Pizarrosa", "Grano": "Muy fino", "Protolito": "Pelita / Lutita", "Minerales clave": "Clorita, Illita, Cuarzo"},
        {"Roca": "Filita", "Foliación": "Filitosa (brillo satinado)", "Grano": "Fino", "Protolito": "Pelita", "Minerales clave": "Sericita, Clorita, Moscovita"},
        {"Roca": "Esquisto", "Foliación": "Esquistosidad visible", "Grano": "Medio a grueso", "Protolito": "Pelita / Basalto", "Minerales clave": "Biotita, Moscovita, Granate, Estaurolita"},
        {"Roca": "Gneis", "Foliación": "Bandamiento Gneísico", "Grano": "Grueso", "Protolito": "Granito / Pelita", "Minerales clave": "Cuarzo, Feldespato K, Plagioclasa, Biotita"},
        {"Roca": "Anfibolita", "Foliación": "Foliada o Maciza", "Grano": "Medio a grueso", "Protolito": "Basalto / Gabro", "Minerales clave": "Hornblenda, Plagioclasa (Oligoclasa/Andesina)"},
        {"Roca": "Eclogita", "Foliación": "Generalmente Maciza", "Grano": "Medio a grueso", "Protolito": "Basalto / Gabro", "Minerales clave": "Onfacita (Piroxeno Na) + Granate (Almandino-Píropo)"},
        {"Roca": "Granulita", "Foliación": "Débil / Granoblástica", "Grano": "Medio a grueso", "Protolito": "Diversos", "Minerales clave": "Hiperstena (Ortopiroxeno) + Plagioclasa ± Granate"}
    ])
    
    st.dataframe(df_rocas, use_container_width=True)

# -----------------------------------------------------------------------------
# MÓDULO 3: DIAGRAMA P-T Y FACIES
# -----------------------------------------------------------------------------
elif menu == " Facies y Diagrama P-T":
    st.header(" Diagrama Presión - Temperatura y Campo de Facies")
    
    # Gráfico interactivo con Plotly
    fig = go.Figure()
    
    # Facies aproximadas en P-T
    facies_data = [
        {"nombre": "Esquistos Verdes", "T": [300, 500, 500, 300], "P": [2, 3, 8, 7]},
        {"nombre": "Anfibolita", "T": [500, 750, 700, 500], "P": [3, 4, 10, 8]},
        {"nombre": "Granulita", "T": [700, 950, 900, 700], "P": [3, 5, 12, 10]},
        {"nombre": "Esquistos Azules", "T": [150, 400, 350, 150], "P": [5, 10, 13, 8]},
        {"nombre": "Eclogita", "T": [400, 850, 800, 400], "P": [12, 18, 20, 13]}
    ]
    
    for f in facies_data:
        fig.add_trace(go.Scatter(
            x=f["T"], y=f["P"],
            fill="toself",
            name=f["nombre"],
            mode="lines+text",
            text=[f["nombre"], "", "", ""],
            textposition="top center"
        ))
        
    fig.update_layout(
        title="Campos P-T Aproximados de Facies Metamórficas",
        xaxis_title="Temperatura (°C)",
        yaxis_title="Presión (kbar)",
        yaxis=dict(autorange="reversed"), # La profundidad/presión aumenta hacia abajo
        template="plotly_white"
    )
    
    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------
# MÓDULO 4: MINERALES ÍNDICE
# -----------------------------------------------------------------------------
elif menu == "💎 Minerales Índice y Protostos":
    st.header("💎 Minerales Índice en Pelitas Metamórficas")
    st.markdown("Secuencia metamórfica de Barroviano (Grado Barroviano creciente):")
    
    zonas = [
        ("1. Zona de la Clorita", "Bajo grado (~200 - 300 °C)", "Clorita, Moscovita, Cuarzo, Albita"),
        ("2. Zona de la Biotita", "Bajo-Medio grado (~300 - 400 °C)", "Biotita, Clorita, Moscovita, Cuarzo"),
        ("3. Zona del Granate", "Medio grado (~400 - 500 °C)", "Granate (Almandino), Biotita, Moscovita"),
        ("4. Zona de la Estaurolita", "Medio-Alto grado (~500 - 600 °C)", "Estaurolita, Granate, Biotita, Muscovita"),
        ("5. Zona de la Cianita (Kyanita)", "Alto grado (Presión media-alta, ~600 °C)", "Cianita, Estaurolita/Granate, Biotita"),
        ("6. Zona de la Sillimanita", "Muy alto grado (> 650 °C)", "Sillimanita, Feldespato K, Biotita, Cuarzo")
    ]
    
    for z, temp, min_assoc in zonas:
        with st.expander(z):
            st.write(f"**Rango aprox.:** {temp}")
            st.write(f"**Paragénesis típica:** {min_assoc}")

# -----------------------------------------------------------------------------
# MÓDULO 5: NOMENCLATURA IUGS
# -----------------------------------------------------------------------------
elif menu == " Guía de Nomenclatura IUGS":
    st.header(" Guía Rápida de Nomenclatura (IUGS / Winter)")
    
    st.markdown("""
    ### Reglas para nombrar una roca metamórfica:
    
    1. **Nombre Basal Estructural / Textural:**
       - Usar el término estructural principal si la roca tiene foliación evidente (ej. *Esquisto*, *Gneis*, *Filita*, *Milonita*).
       - Usar términos composicionales/específicos si es monomineralic/no foliada (ej. *Cuarcita*, *Mármol*, *Hornfels*).

    2. **Prefijos Mineralógicos (Minerales Accesorio/Índice):**
       - Se colocan antes del nombre principal en **orden creciente de abundancia**.
       - *Ejemplo:* Un esquisto con 35% moscovita, 15% biotita y 5% granate se nombra **Esquisto de granate-biotita-moscovita**.

    3. **Calificadores de Protolito (Opcionales):**
       - **Ortometamórfica (Orto-):** Derivada de roca ígnea (ej. *Ortogneis*).
       - **Parametamórfica (Para-):** Derivada de roca sedimentaria (ej. *Paragneis*).
    """)
