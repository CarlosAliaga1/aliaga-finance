import streamlit as st

# 1. Configuración de página y Estilos CSS Ultra-Compactos
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    /* Eliminación de márgenes para visualización completa en una pantalla */
    .block-container {padding-top: 0rem; padding-bottom: 0rem; max-width: 95%;}
    .stMetric {padding: 0px !important; margin: 0px !important;}
    hr {margin: 0.3rem 0 !important;}
    
    /* Encabezado ROJO INTENSO - Todo Mayúsculas y Alineado */
    .fondo-rojo {
        background-color: #FF0000; 
        color: #FFFFFF; 
        padding: 10px; 
        border-radius: 5px; 
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 60px;
    }
    
    /* Resultados AZUL INTENSO */
    .fondo-azul {
        background-color: #0000FF; 
        color: #FFFFFF; 
        padding: 10px; 
        border-radius: 5px; 
        margin-bottom: 5px;
        text-align: center;
    }
    
    h1 {font-size: 20px !important; margin: 0px; text-transform: uppercase; font-weight: bold;}
    h2 {font-size: 16px !important; margin: 5px 0px; text-align: center;}
    h3 {font-size: 15px !important; margin: 2px; text-align: center; font-weight: bold;}
    
    /* Botón de limpieza personalizado */
    div.stButton > button { 
        width: 100%; font-weight: bold; padding: 2px;
        color: #0000FF; border: 2px solid #0000FF;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo (Limpieza de campos)
if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0

def limpiar_datos():
    st.session_state.reset_id += 1

# 3. Interfaz Principal
st.markdown("<div class='fondo-rojo'><h1>MONTO COMPUESTO CON TASA NOMINAL CAPITALIZABLE</h1></div>", unsafe_allow_html=True)
st.markdown("<h2>Dr. Carlos Aliaga Valdez</h2>", unsafe_allow_html=True)

# --- BARRA LATERAL (ENTRADAS) ---
with st.sidebar:
    st.header("Configuración")
    rid = st.session_state.reset_id
    
    # Valores vuelven a 0, excepto capitalización que queda en 1 por seguridad
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=0.0, key=f"p_{rid}")
    tn = st.number_input("Tasa Nominal (j %)", min_value=0.0, value=0.0, format="%.2f", key=f"tn_{rid}")
    d_tn = st.number_input("Periodo de la TN (días)", min_value=0, value=0, key=f"dtn_{rid}")
    d_cap = st.number_input("Periodo de Capitalización (días)", min_value=1, value=1, key=f"dcap_{rid}")
    plazo = st.number_input("Plazo del depósito (días)", min_value=0, value=0, key=f"plazo_{rid}")
    
    st.button("🔄 LIMPIAR PARA NUEVOS DATOS", on_click=limpiar_datos)

# --- LÓGICA DE CÁLCULO ---
if d_cap > 0 and d_tn > 0 and p > 0:
    j = tn / 100
    m = d_tn / d_cap
    n = plazo / d_cap
    i_ef = j / m
    s = p * (1 + i_ef)**n
    interes = s - p
else:
    m, n, i_ef, s, interes = 0.0, 0.0, 0.0, 0.0, 0.0

# --- REPORTES DE SALIDA ---
st.markdown("<h3>REPORTES DE SALIDA</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("Frecuencia (m)", f"{m:.8f}")
with col2: st.metric("Capitalizaciones (n)", f"{n:.8f}")
with col3: st.metric("Tasa Efectiva", f"{i_ef:.8f}")

# --- RESULTADOS FINALES (AZUL INTENSO) ---
st.markdown(f"""
    <div class='fondo-azul'>
        <h2 style='margin:0;'>MONTO COMPUESTO (S): {s:,.2f}</h2>
    </div>
    <div class='fondo-azul'>
        <h2 style='margin:0;'>INTERÉS COMPUESTO (I): {interes:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
