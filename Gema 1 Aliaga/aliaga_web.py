import streamlit as st

# 1. Configuración de Marca y Estética Premium Dr. Aliaga
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    /* Centrado del reporte y control de ancho */
    .block-container {
        max-width: 900px;
        padding-top: 1rem;
        padding-bottom: 0rem;
        margin: auto;
    }
    
    /* ENCABEZADO ROJO: 80px de alto con centrado vertical total */
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

# 3. Estructura Visual Principal
st.markdown("<div class='caja-roja'><p class='titulo-grande'>MONTO COMPUESTO CON TASA NOMINAL CAPITALIZABLE</p></div>", unsafe_allow_html=True)
st.markdown("<span class='marca-autor'>Dr. Carlos Aliaga Valdez</span>", unsafe_allow_html=True)

# --- BARRA LATERAL: CONFIGURACIÓN CON CAMPOS EN BLANCO ---
with st.sidebar:
    st.header("Configuración")
    rid = st.session_state.reset_id
    
    # Campos que quedan en blanco al resetear usando text_input
    p_in = st.text_input("1. Capital Principal (P)", value="", key=f"p_{rid}")
    tn_in = st.text_input("2. Tasa Nominal (j %)", value="", key=f"tn_{rid}")
    dtn_in = st.text_input("3. Periodo de la TN (días)", value="", key=f"dtn_{rid}")
    dcap_in = st.text_input("4. Periodo de Capitalización (días)", value="", key=f"dcap_{rid}")
    
    # Actualización de etiqueta a "Plazo de la inversión"
    plazo_in = st.text_input("5. Plazo de la inversión (días)", value="", key=f"plazo_{rid}")
    
    # Conversión y validación de entradas
    try:
        p = float(p_in) if p_in else 0.0
        tn = float(tn_in) if tn_in else 0.0
        d_tn = float(dtn_in) if dtn_in else 0.0
        d_cap = float(dcap_in) if dcap_in else 0.0
        plazo = float(plazo_in) if plazo_in else 0.0
    except ValueError:
        p = tn = d_tn = d_cap = plazo = 0.0
        st.error("⚠️ Ingrese solo valores numéricos.")

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
    m = n = i_ef = s = interes = 0.0

# --- REPORTES DE SALIDA ---
st.markdown("<p class='etiqueta-reporte'>REPORTES DE SALIDA</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("Frecuencia (m)", f"{m:.8f}")
with col2: st.metric("Capitalizaciones (n)", f"{n:.8f}")
with col3: st.metric("Tasa Efectiva", f"{i_ef:.8f}")

# --- RESULTADOS FINALES EN AZUL INTENSO ---
st.markdown(f"""
    <div class='caja-azul'>
        <p class='texto-azul'>MONTO COMPUESTO (S): {s:,.2f}</p>
    </div>
    <div class='caja-azul'>
        <p class='texto-azul'>INTERÉS COMPUESTO (I): {interes:,.2f}</p>
    </div>
    """, unsafe_allow_html=True)
