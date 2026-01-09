import streamlit as st

# 1. Configuración de página y Estilo CSS para su identidad visual
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    /* Compactar vista y eliminar márgenes */
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    
    /* ROJO INTENSO con letras blancas (Identidad Dr. Aliaga) */
    .fondo-identidad {
        background-color: #FF0000; 
        color: #FFFFFF; 
        padding: 15px; 
        border-radius: 10px; 
        margin-bottom: 10px;
        text-align: center;
        border: 2px solid #CC0000;
    }
    
    .centrado { text-align: center; }
    
    /* Estilo del botón de reseteo */
    div.stButton > button { 
        width: 100%; 
        border-radius: 5px; 
        background-color: #f0f2f6;
        font-weight: bold;
        color: #FF0000;
        border: 1px solid #FF0000;
    }
    div.stButton > button:hover {
        background-color: #FF0000;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo para vaciar campos
if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0

def limpiar_campos():
    st.session_state.reset_id += 1

# 3. Título Principal en Rojo Intenso
st.markdown("<div class='fondo-identidad'><h1>Monto compuesto con TN capitalizable</h1></div>", unsafe_allow_html=True)
st.markdown("<h2 class='centrado'>Dr. Carlos Aliaga Valdez</h2>", unsafe_allow_html=True)

# --- BARRA LATERAL (CAMPOS QUE SE VACÍAN) ---
with st.sidebar:
    st.header("Configuración")
    rid = st.session_state.reset_id
    
    # Al resetear, estos campos vuelven a 0.0 o 0 (vacíos de datos anteriores)
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=0.0, step=100.0, key=f"p_{rid}")
    tasa_nominal = st.number_input("Tasa Nominal (j %)", min_value=0.0, value=0.0, step=0.1, format="%.2f", key=f"tn_{rid}")
    dias_tn = st.number_input("Periodo de la TN (días)", min_value=0, value=0, key=f"dtn_{rid}")
    dias_cap = st.number_input("Periodo de Capitalización (días)", min_value=1, value=1, key=f"dcap_{rid}")
    plazo_total = st.number_input("Plazo del depósito (días)", min_value=0, value=0, key=f"plazo_{rid}")
    
    st.write("---")
    # Botón que limpia todos los valores trabajados
    st.button("🔄 LIMPIAR PARA NUEVOS DATOS", on_click=limpiar_campos)

# --- LÓGICA DE CÁLCULO (Evita división por cero si los campos están vacíos) ---
if dias_cap > 0 and dias_tn > 0:
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
st.markdown("<h3 class='centrado'>REPORTES DE SALIDA</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("Frecuencia (m)", f"{m:.8f}")
with col2: st.metric("Capitalizaciones (n)", f"{n:.8f}")
with col3: st.metric("Tasa Efectiva", f"{i_efectiva:.8f}")

# --- RESULTADOS FINALES EN ROJO INTENSO ---
st.write("---")
st.markdown(f"""
    <div class='fondo-identidad'>
        <h2>MONTO COMPUESTO (S): {s:,.2f}</h2>
    </div>
    <div class='fondo-identidad'>
        <h2>INTERÉS COMPUESTO (I): {interes_i:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
