import streamlit as st

# 1. Configuración de página y Estilo CSS Personalizado
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    /* Reducir espacios generales */
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    
    /* Fondo azul intenso con letras blancas para resultados */
    .fondo-azul {
        background-color: #0000FF; 
        color: #FFFFFF; 
        padding: 20px; 
        border-radius: 10px; 
        margin-bottom: 10px;
        text-align: center;
    }
    
    /* Centrado de textos */
    .centrado { text-align: center; }
    
    /* Botón de reseteo ocupando todo el ancho */
    div.stButton > button { width: 100%; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo (Versión Robusta)
if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0

def resetear():
    st.session_state.reset_id += 1

# 3. Encabezados Centrados
st.markdown("<h1 class='centrado'>Monto compuesto con TN capitalizable</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='centrado'>Dr. Carlos Aliaga Valdez</h2>", unsafe_allow_html=True)

# --- BARRA LATERAL (ENTRADAS) ---
with st.sidebar:
    st.header("Configuración")
    # La key dinámica obliga a Streamlit a destruir y recrear los campos al resetear
    rid = st.session_state.reset_id
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=10000.0, key=f"p_{rid}")
    tasa_nominal = st.number_input("Tasa Nominal (j %)", value=2.0, step=0.1, format="%.2f", key=f"tn_{rid}")
    dias_tn = st.number_input("Periodo de la TN (días)", value=30, key=f"dtn_{rid}")
    dias_cap = st.number_input("Periodo de Capitalización (días)", value=15, key=f"dcap_{rid}")
    plazo_total = st.number_input("Plazo del depósito (días)", value=180, key=f"plazo_{rid}")
    
    st.write("---")
    st.button("🔄 Resetear Información", on_click=resetear)

# --- LÓGICA DE CÁLCULO ---
j = tasa_nominal / 100
m = dias_tn / dias_cap
n = plazo_total / dias_cap
i_efectiva = j / m
s = p * (1 + i_efectiva)**n
interes_i = s - p

# --- REPORTES DE SALIDA ---
st.write("---")
st.markdown("<h3 class='centrado'>REPORTES DE SALIDA</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("Frecuencia (m)", f"{m:.8f}")
with col2: st.metric("Capitalizaciones (n)", f"{n:.8f}")
with col3: st.metric("Tasa Efectiva", f"{i_efectiva:.8f}")

# --- RESULTADOS CON SU IDENTIDAD (AZUL INTENSO) ---
st.write("---")
st.markdown(f"""
    <div class='fondo-azul'>
        <h2>MONTO COMPUESTO (S): {s:,.2f}</h2>
    </div>
    <div class='fondo-azul'>
        <h2>INTERÉS COMPUESTO (I): {interes_i:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
