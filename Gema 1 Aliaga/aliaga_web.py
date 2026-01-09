import streamlit as st

# 1. Configuración de página y Títulos
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

# 2. LÓGICA DE RESETEO (Sin errores de callback)
if "reset_key" not in st.session_state:
    st.session_state.reset_key = 0

# Función que limpia la memoria al presionar el botón
def reset_total():
    st.session_state.reset_key += 1

st.title("Monto compuesto con TN capitalizable")
st.markdown("### Dr. Carlos Aliaga Valdez")

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("Configuración del Modelo")
    
    # Cada entrada usa una 'key' que cambia cuando reseteamos
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=10000.0, key=f"p_{st.session_state.reset_key}")
    tasa_nominal = st.number_input("Tasa Nominal (j %)", value=2.0, step=0.1, format="%.2f", key=f"tn_{st.session_state.reset_key}")
    dias_tn = st.number_input("Periodo de la TN (días)", value=30, key=f"dtn_{st.session_state.reset_key}")
    dias_cap = st.number_input("Periodo de Capitalización (días)", value=15, key=f"dcap_{st.session_state.reset_key}")
    plazo_total = st.number_input("Plazo del depósito (días)", value=180, key=f"plazo_{st.session_state.reset_key}")
    
    st.write("---")
    # Al hacer clic, se activa la función reset_total
    st.button("🔄 Resetear Información", on_click=reset_total)

# --- LÓGICA DE CÁLCULO (Réplica de Windows) ---
j = tasa_nominal / 100
m = dias_tn / dias_cap           # Frecuencia
n = plazo_total / dias_cap       # Capitalizaciones
i_efectiva = j / m               # Tasa efectiva del periodo

s = p * (1 + i_efectiva)**n
interes_i = s - p

# --- REPORTES DE SALIDA (PRECISIÓN 8 DECIMALES) ---
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
