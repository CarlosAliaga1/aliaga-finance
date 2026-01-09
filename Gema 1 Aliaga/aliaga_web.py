import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

# 2. LÓGICA DE RESETEO DEFINITIVA
def reset_total():
    for key in st.session_state.keys():
        del st.session_state[key]

st.title("Monto compuesto con TN capitalizable")
st.markdown("### Dr. Carlos Aliaga Valdez")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("Configuración del Modelo")
    
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=10000.0, key="p")
    tasa_nominal = st.number_input("Tasa Nominal (j %)", value=2.0, step=0.1, format="%.2f", key="tn")
    dias_tn = st.number_input("Periodo de la TN (días)", value=30, key="dtn")
    dias_cap = st.number_input("Periodo de Capitalización (días)", value=15, key="dcap")
    plazo_total = st.number_input("Plazo del depósito (días)", value=180, key="plazo")
    
    st.write("---")
    st.button("🔄 Resetear Información", on_click=reset_total)

# --- LÓGICA DE CÁLCULO ---
j = tasa_nominal / 100
m = dias_tn / dias_cap
n = plazo_total / dias_cap
i_efectiva = j / m
s = p * (1 + i_efectiva)**n
interes_i = s - p

# --- REPORTES DE SALIDA (PRECISIÓN 8 DECIMALES) ---
st.write("---")
st.header("REPORTES DE SALIDA (PRECISIÓN 8 DECIMALES)")
col1, col2, col3 = st.columns(3)
col1.metric("Frecuencia (m)", f"{m:.8f}")
col2.metric("Capitalizaciones (n)", f"{n:.8f}")
col3.metric("Tasa Efectiva", f"{i_efectiva:.8f}")

# --- RESULTADOS FINALES (TAMAÑO IGUAL A REPORTES DE SALIDA) ---
st.write("---")
# Usamos st.header para que el tamaño sea igual al anterior
st.header(f"MONTO COMPUESTO (S): {s:,.2f}")
st.header(f"INTERÉS COMPUESTO (I): {interes_i:,.2f}")
