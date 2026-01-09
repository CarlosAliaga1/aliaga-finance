import streamlit as st

# 1. Configuración de página y Estilo para reducir espacios
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

# CSS para reducir espacios entre filas y personalizar títulos
st.markdown("""
    <style>
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    .stMetric {padding: 5px;}
    h1, h2, h3 {margin-top: -10px; margin-bottom: 10px; text-align: center;}
    div.stButton > button {width: 100%;}
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo
if "version" not in st.session_state:
    st.session_state.version = 0

def reset_total():
    st.session_state.version += 1

# 3. Encabezado Centrado
st.title("Monto compuesto con TN capitalizable")
st.markdown("<h2 style='text-align: center;'>Dr. Carlos Aliaga Valdez</h2>", unsafe_allow_html=True)

# --- BARRA LATERAL (Entradas con llave de reseteo) ---
with st.sidebar:
    st.header("Configuración")
    v = st.session_state.version
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=10000.0, key=f"p_{v}")
    tasa_nominal = st.number_input("Tasa Nominal (j %)", value=2.0, step=0.1, format="%.2f", key=f"tn_{v}")
    dias_tn = st.number_input("Periodo de la TN (días)", value=30, key=f"dtn_{v}")
    dias_cap = st.number_input("Periodo de Capitalización (días)", value=15, key=f"dcap_{v}")
    plazo_total = st.number_input("Plazo del depósito (días)", value=180, key=f"plazo_{v}")
    
    st.write("---")
    st.button("🔄 Resetear Información", on_click=reset_total)

# --- LÓGICA DE CÁLCULO ---
j = tasa_nominal / 100
m = dias_tn / dias_cap
n = plazo_total / dias_cap
i_efectiva = j / m
s = p * (1 + i_efectiva)**n
interes_i = s - p

# --- REPORTES DE SALIDA CON FONDO ---
st.markdown("<div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px;'>", unsafe_allow_html=True)
st.subheader("REPORTES DE SALIDA")
col1, col2, col3 = st.columns(3)
col1.metric("Frecuencia (m)", f"{m:.8f}")
col2.metric("Capitalizaciones (n)", f"{n:.8f}")
col3.metric("Tasa Efectiva", f"{i_efectiva:.8f}")
st.markdown("</div>", unsafe_allow_html=True)

st.write("") # Espacio mínimo

# --- RESULTADOS FINALES CON FONDO Y TAMAÑO GRANDE ---
st.success(f"### **MONTO COMPUESTO (S): {s:,.2f}**")
st.info(f"### **INTERÉS COMPUESTO (I): {interes_i:,.2f}**")
