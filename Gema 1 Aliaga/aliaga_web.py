import streamlit as st

# 1. Configuración de página y CSS ultra-compacto
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    /* Eliminación total de espacios sobrantes */
    .block-container {padding-top: 0.5rem; padding-bottom: 0rem; max-width: 95%;}
    .stMetric {padding: 2px !important; margin: 0px !important;}
    hr {margin: 0.5rem 0 !important;}
    
    /* ROJO INTENSO para el Título (Compacto) */
    .fondo-rojo {
        background-color: #FF0000; 
        color: #FFFFFF; 
        padding: 8px; 
        border-radius: 8px; 
        margin-bottom: 5px;
        text-align: center;
    }
    
    /* AZUL INTENSO para los Resultados (Compacto) */
    .fondo-azul {
        background-color: #0000FF; 
        color: #FFFFFF; 
        padding: 8px; 
        border-radius: 8px; 
        margin-bottom: 5px;
        text-align: center;
    }
    
    /* Títulos y textos reducidos */
    h1 {font-size: 22px !important; margin: 0px;}
    h2 {font-size: 18px !important; margin: 0px; text-align: center;}
    h3 {font-size: 16px !important; margin: 5px; text-align: center;}
    
    /* Botón de limpieza */
    div.stButton > button { 
        width: 100%; 
        font-weight: bold;
        padding: 2px;
        color: #0000FF;
        border: 2px solid #0000FF;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo (Vuelve a cero)
if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0

def limpiar_todo():
    st.session_state.reset_id += 1

# 3. Encabezado en ROJO INTENSO
st.markdown("<div class='fondo-rojo'><h1>Monto compuesto con TN capitalizable</h1></div>", unsafe_allow_html=True)
st.markdown("<h2>Dr. Carlos Aliaga Valdez</h2>", unsafe_allow_html=True)

# --- BARRA LATERAL (CAMPOS EN CERO) ---
with st.sidebar:
    st.header("Configuración")
    rid = st.session_state.reset_id
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=0.0, key=f"p_{rid}")
    tasa_nominal = st.number_input("Tasa Nominal (j %)", min_value=0.0, value=0.0, format="%.2f", key=f"tn_{rid}")
    dias_tn = st.number_input("Periodo de la TN (días)", min_value=0, value=0, key=f"dtn_{rid}")
    dias_cap = st.number_input("Periodo de Capitalización (días)", min_value=1, value=1, key=f"dcap_{rid}")
    plazo_total = st.number_input("Plazo del depósito (días)", min_value=0, value=0, key=f"plazo_{rid}")
    
    st.button("🔄 LIMPIAR PARA NUEVOS DATOS", on_click=limpiar_todo)

# --- LÓGICA DE CÁLCULO ---
if dias_cap > 0 and dias_tn > 0 and p > 0:
    j = tasa_nominal / 100
    m = dias_tn / dias_cap
    n = plazo_total / dias_cap
    i_efectiva = j / m
    s = p * (1 + i_efectiva)**n
    interes_i = s - p
else:
    m, n, i_efectiva, s, interes_i = 0, 0, 0, 0, 0

# --- REPORTES DE SALIDA ---
st.write("---")
st.markdown("<h3>REPORTES DE SALIDA</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("Frecuencia (m)", f"{m:.8f}")
with col2: st.metric("Capitalizaciones (n)", f"{n:.8f}")
with col3: st.metric("Tasa Efectiva", f"{i_efectiva:.8f}")

# --- RESULTADOS FINALES EN AZUL INTENSO ---
st.write("---")
st.markdown(f"""
    <div class='fondo-azul'>
        <h2 style='margin:0;'>MONTO COMPUESTO (S): {s:,.2f}</h2>
    </div>
    <div class='fondo-azul'>
        <h2 style='margin:0;'>INTERÉS COMPUESTO (I): {interes_i:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
