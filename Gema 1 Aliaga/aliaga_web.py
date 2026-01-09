import streamlit as st

# 1. Configuración y Estilos de Identidad Dr. Aliaga
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    /* Eliminación de espacios para que todo quepa en una pantalla */
    .block-container {padding-top: 0.5rem; padding-bottom: 0rem; max-width: 95%;}
    
    /* ENCABEZADO ROJO: Título en Mayúsculas y perfectamente centrado */
    .cabecera-roja {
        background-color: #FF0000; 
        color: #FFFFFF; 
        padding: 15px; 
        border-radius: 8px; 
        text-align: center;
        margin-bottom: 5px;
    }
    .titulo-principal {
        font-size: 24px !important; 
        margin: 0px; 
        text-transform: uppercase; 
        font-weight: bold;
        line-height: 1.2;
    }
    
    /* MARCA PERSONAL: Dr. Carlos Aliaga Valdez (Aumentado) */
    .marca-autor {
        font-size: 22px !important;
        font-weight: bold;
        color: #333333;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
        display: block;
    }
    
    /* RESULTADOS AZUL INTENSO */
    .resultado-azul {
        background-color: #0000FF; 
        color: #FFFFFF; 
        padding: 12px; 
        border-radius: 8px; 
        margin-top: 8px;
        text-align: center;
        font-weight: bold;
    }
    
    /* Etiquetas de reportes */
    .etiqueta-reporte {
        font-size: 18px !important;
        text-align: center;
        font-weight: bold;
        margin-top: 15px;
    }

    /* Botón de limpieza */
    div.stButton > button { 
        width: 100%; font-weight: bold; color: #0000FF; border: 2px solid #0000FF;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo Total
if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0

def realizar_limpieza():
    st.session_state.reset_id += 1

# 3. Estructura Visual (Título y Nombre)
st.markdown("<div class='cabecera-roja'><p class='titulo-principal'>MONTO COMPUESTO CON TASA NOMINAL CAPITALIZABLE</p></div>", unsafe_allow_html=True)
st.markdown("<span class='marca-autor'>Dr. Carlos Aliaga Valdez</span>", unsafe_allow_html=True)

# --- BARRA LATERAL (ENTRADAS QUE VUELVEN A CERO) ---
with st.sidebar:
    st.header("Configuración")
    rid = st.session_state.reset_id
    
    # Todos los campos inician en 0 al limpiar
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=0.0, key=f"p_{rid}")
    tn = st.number_input("Tasa Nominal (j %)", min_value=0.0, value=0.0, format="%.2f", key=f"tn_{rid}")
    d_tn = st.number_input("Periodo de la TN (días)", min_value=0, value=0, key=f"dtn_{rid}")
    d_cap = st.number_input("Periodo de Capitalización (días)", min_value=0, value=0, key=f"dcap_{rid}")
    plazo = st.number_input("Plazo del depósito (días)", min_value=0, value=0, key=f"plazo_{rid}")
    
    st.button("🔄 LIMPIAR PARA NUEVOS DATOS", on_click=realizar_limpieza)

# --- LÓGICA DE CÁLCULO (Control de error de división por cero) ---
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

# --- RESULTADOS FINALES (AZUL INTENSO) ---
st.markdown(f"""
    <div class='resultado-azul'>
        <h2 style='margin:0; font-size: 22px;'>MONTO COMPUESTO (S): {s:,.2f}</h2>
    </div>
    <div class='resultado-azul'>
        <h2 style='margin:0; font-size: 22px;'>INTERÉS COMPUESTO (I): {interes:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)
