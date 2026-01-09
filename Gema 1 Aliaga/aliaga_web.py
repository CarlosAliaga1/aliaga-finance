import streamlit as st

# Configuración y Títulos
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")
st.title("Monto compuesto con TN capitalizable")
st.markdown("### Dr. Carlos Aliaga Valdez")

# --- BARRA LATERAL (ENTRADAS DE DATOS) ---
with st.sidebar:
    st.header("Configuración del Modelo")
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=10000.0)
    # Cambio 1: Solo "Tasa Nominal"
    tasa_nominal = st.number_input("Tasa Nominal (j %)", value=2.0, step=0.1, format="%.2f")
    dias_tn = st.number_input("Periodo de la TN (días)", value=30)
    dias_cap = st.number_input("Periodo de Capitalización (días)", value=15)
    plazo_total = st.number_input("Plazo del depósito (días)", value=180)
    
    st.write("---")
    # Cambio 3: Botón para resetear (limpiar información)
    if st.button("Resetear Información"):
        st.rerun()

# --- LÓGICA DE CÁLCULO (Réplica de Windows) ---
j = tasa_nominal / 100
m = dias_tn / dias_cap           # Frecuencia
n = plazo_total / dias_cap       # Capitalizaciones
i_efectiva = j / m               # Tasa efectiva del periodo

s = p * (1 + i_efectiva)**n
interes_i = s - p

# --- REPORTES DE SALIDA (CAMBIO 2: PRECISIÓN 8 DECIMALES) ---
st.write("---")
st.header("REPORTES DE SALIDA (PRECISIÓN 8 DECIMALES)")
col1, col2, col3 = st.columns(3)
col1.metric("Frecuencia (m)", f"{m:.8f}")
col2.metric("Capitalizaciones (n)", f"{n:.8f}")
col3.metric("Tasa Efectiva del periodo", f"{i_efectiva:.8f}")

# --- RESULTADOS FINALES ---
st.write("---")
st.success(f"**MONTO COMPUESTO (S):** {s:,.2f}")
st.info(f"**INTERÉS COMPUESTO (I):** {interes_i:,.2f}")
