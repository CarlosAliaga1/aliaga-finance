import streamlit as st

# 1. Configuración de Marca y Estética Premium Dr. Aliaga
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    .block-container {
        max-width: 900px;
        padding-top: 1rem;
        padding-bottom: 0rem;
        margin: auto;
    }
    
    /* ENCABEZADO ROJO INTENSO: 80px de alto */
    .caja-roja {
        background-color: #FF0000; 
        color: #FFFFFF; 
        height: 80px; 
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    .titulo-grande {
        font-size: 26px !important; 
        font-weight: bold;
        text-transform: uppercase;
        margin: 0;
        text-align: center;
    }
    
    /* MARCA PERSONAL: Dr. Carlos Aliaga Valdez */
    .marca-autor {
        font-size: 38px !important;
        font-weight: 900;
        color: #111111;
        text-align: center;
        margin: 10px 0px;
        display: block;
        font-family: 'Arial Black', sans-serif;
    }
    
    /* RESULTADOS AZUL INTENSO: 80px de alto */
    .caja-azul {
        background-color: #0000FF; 
        color: #FFFFFF; 
        height: 80px; 
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px; 
        margin-top: 10px;
    }
    .texto-azul {
        font-size: 26px !important;
        font-weight: bold;
        margin: 0;
    }
    
    .etiqueta-reporte {
        font-size: 22px !important;
        text-align: center;
        font-weight: bold;
        margin-top: 5px;
    }

    /* Botón de limpieza profesional */
    div.stButton > button { 
        width: 100%; font-weight: bold; font-size: 16px;
        color: #0000FF; border: 2px solid #0000FF; border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo Integral
if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0

def limpiar_pantalla():
    st.session_state.reset_id += 1

# 3. Estructura Visual
st.markdown("<div class='caja-roja'><p class='titulo-grande'>MONTO COMPUESTO CON TASA NOMINAL CAPITALIZABLE</p></div>", unsafe_allow_html=True)
st.markdown("<span class='marca-autor'>Dr. Carlos Aliaga Valdez</span>", unsafe_allow_html=True)

# --- BARRA LATERAL: CONFIGURACIÓN CON CAMPOS QUE QUEDAN EN BLANCO ---
with st.sidebar:
    st.header("Configuración")
    rid = st.session_state.reset_id
    
    # Usamos text_input para permitir que el campo quede vacío al resetear
    p_str = st.text_input("1. Capital Principal (P)", value="", key=f"p_{rid}")
    tn_str = st.text_input("2. Tasa Nominal (j %)", value="", key=f"tn_{rid}")
    
    # Estos se mantienen numéricos por precisión de días
    d_tn = st.number_input("3. Periodo de la TN (días)", min_value=0, value=0, key=f"dtn_{rid}")
    d_cap = st.number_input("4. Periodo de Capitalización (días)", min_value=0, value=0, key=f"dcap_{rid}")
    plazo = st.number_input("5. Plazo del depósito (días)", min_value=0, value=0, key=f"plazo_{rid}")
    
    # Conversión segura de texto a número
    try:
        p = float(p_str) if p_str else 0.0
        tn = float(tn_str) if tn_str else 0.0
    except ValueError:
        p, tn = 0.0, 0.0
        st.error("Por favor, ingrese solo números.")

    st.write("---")
    st.button("🔄 LIMPIAR PARA NUEVOS DATOS", on_click=limpiar_pantalla)

# --- LÓGICA DE CÁLCULO PROFESIONAL ---
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
st.markdown("<p class='etiqueta-reporte'>REPORTES DE SALIDA</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("Frecuencia (m)", f"{m:.8f}")
with col2: st.metric("Capitalizaciones (n)", f"{n:.8f}")
with col3: st.metric("Tasa Efectiva", f"{i_ef:.8f}")

# --- RESULTADOS FINALES EN AZUL ---
st.markdown(f"""
    <div class='caja-azul'>
        <p class='texto-azul'>MONTO COMPUESTO (S): {s:,.2f}</p>
    </div>
    <div class='caja-azul'>
        <p class='texto-azul'>INTERÉS COMPUESTO (I): {interes:,.2f}</p>
    </div>
    """, unsafe_allow_html=True)
