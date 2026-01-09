import streamlit as st
import math
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.title("📊 Monto compuesto con TN capitalizable")
st.markdown("### Dr. Carlos Aliaga Valdez")

# --- BARRA LATERAL PARA ENTRADA DE DATOS ---
with st.sidebar:
    st.header("Configuración del Modelo")
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=10000.0)
    tasa_nominal = st.sidebar.number_input("Tasa Nominal (j %)", value=2.0, step=0.1, format="%.2f")
    dias_tn = st.number_input("Periodo de la TN (días)", value=360)
    dias_cap = st.number_input("Periodo de Capitalización (días)", value=45)
    plazo_total = st.number_input("Plazo del depósito (días)", value=180)

# --- CÁLCULOS FINANCIEROS ---
j = j_porc / 100
m = dias_tn / dias_cap
n = plazo_total / dias_cap
i_efectiva = j / m
s = p * math.pow((1 + i_efectiva), n)
interes = s - p

# --- PRESENTACIÓN DE RESULTADOS ---
col1, col2 = st.columns(2)
with col1:
    st.success(f"**Monto Compuesto (S):** ${s:,.2f}")
with col2:
    st.info(f"**Interés Compuesto (I):** ${interes:,.2f}")

# Gráfico Profesional
st.subheader("Crecimiento de la Inversión")
data = pd.DataFrame({
    "Categoría": ["Capital Inicial", "Intereses"],
    "Monto": [p, interes]
})

st.bar_chart(data=data, x="Categoría", y="Monto")

