import streamlit as st

# 1. Configuración de página y Estilos CSS
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    
    /* ROJO INTENSO para el Título */
    .fondo-rojo {
        background-color: #FF0000; 
        color: #FFFFFF; 
        padding: 15px; 
        border-radius: 10px; 
        margin-bottom: 10px;
        text-align: center;
    }
    
    /* AZUL INTENSO para los Resultados (S e I) */
    .fondo-azul {
        background-color: #0000FF; 
        color: #FFFFFF; 
        padding: 15px; 
        border-radius: 10px; 
        margin-bottom: 10px;
        text-align: center;
    }
    
    .centrado { text-align: center; }
    
    /* Estilo del botón de limpieza */
    div.stButton > button { 
        width: 100%; 
        font-weight: bold;
        color: #0000FF;
        border: 2px solid #0000FF;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo para vaciar campos
if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0

def limpiar_todo():
    st.session_state.reset_id += 1

# 3. Encabezado en ROJO INTENSO
st.markdown("<div class='fondo-rojo'><h1>Monto compuesto con TN capitalizable</h1></div>", unsafe_allow_html=True)
st.markdown("<h2 class='centrado'>Dr. Carlos Aliaga Valdez</h2>", unsafe_allow_html=True)

# --- BARRA LATERAL (CAMPOS EN BLANCO/CERO AL RESETEAR) ---
with st.sidebar:
    st.header("Configuración")
    rid = st.session_state.reset_id
    
    # Todos los valores inician en 0 para recibir nuevos datos
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=0.0, key=f"p_{rid}")
    tasa_nominal = st.number_input("Tasa Nominal (j %)", min_value=0.0, value=0.0, format="%.2f", key=f"tn_{rid}")
    dias_tn = st.number_input("Periodo de la TN (días)", min_value=0, value=0, key=f"dtn_{rid}")
    dias_cap = st.number_input("Periodo de Capitalización (días)", min_value=1, value=1, key=f"dcap_{rid}")
    plazo_total = st.number_input("Plazo del depósito (días)", min_value=0, value=0, key=f"plazo_{rid}")
    
    st.write("---")
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
st.markdown("<h3 class='centrado'>REPORTES DE SALIDA</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("Frecuencia (m)", f"{m:.8f}")
with col2: st.metric("Capitalizaciones (n)", f"{n:.8f}")
with col3: st.metric("Tasa Efectiva", f"{i_efectiva:.8f}")

# --- RESULTADOS FINALES EN AZUL INTENSO ---
st.write("---")
st.markdown(f"""
    <div class='fondo-azul'>
        <h2>MONTO COMPUESTO (S): {s:,.2f}</h2>
    </div>
    <div class='fondo-azul'>
        <h2>INTERÉS COMPUESTO (I): {interes_i:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
