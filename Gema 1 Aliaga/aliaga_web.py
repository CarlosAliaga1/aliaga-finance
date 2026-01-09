import streamlit as st

# 1. Configuración y Estética de Marca Dr. Aliaga
st.set_page_config(page_title="Aliaga Finance Pro", layout="wide")

st.markdown("""
    <style>
    /* Centrado total del reporte en la pantalla de PC */
    .main {
        display: flex;
        justify-content: center;
    }
    .block-container {
        max-width: 900px;
        padding-top: 1rem;
        padding-bottom: 0rem;
    }
    
    /* ENCABEZADO ROJO: Ajuste de altura simétrico a los azules */
    .caja-roja {
        background-color: #FF0000; 
        color: #FFFFFF; 
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .titulo-mayuscula {
        font-size: 26px !important; 
        font-weight: bold;
        text-transform: uppercase;
        margin: 0;
    }
    
    /* MARCA PERSONAL: Dr. Carlos Aliaga Valdez (Tamaño Máximo) */
    .marca-personal {
        font-size: 32px !important;
        font-weight: 800;
        color: #1A1A1A;
        text-align: center;
        margin: 15px 0px;
        display: block;
        font-family: 'Arial Black', Gadget, sans-serif;
    }
    
    /* RESULTADOS AZUL INTENSO (Simetría total con la roja) */
    .caja-azul {
        background-color: #0000FF; 
        color: #FFFFFF; 
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px; 
        margin-top: 10px;
        font-weight: bold;
    }
    .texto-resultado {
        font-size: 26px !important;
        margin: 0;
    }
    
    /* Estética de Reportes de Salida */
    .etiqueta-salida {
        font-size: 20px !important;
        text-align: center;
        font-weight: bold;
        margin-top: 10px;
    }

    /* Botón de limpieza profesional */
    div.stButton > button { 
        width: 100%; font-weight: bold; font-size: 16px;
        color: #0000FF; border: 2px solid #0000FF; border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Lógica de Reseteo (Limpieza total incluyendo capitalización)
if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0

def limpiar_interfaz():
    st.session_state.reset_id += 1

# 3. Interfaz Centrada
st.markdown("<div class='caja-roja'><p class='titulo-mayuscula'>MONTO COMPUESTO CON TASA NOMINAL CAPITALIZABLE</p></div>", unsafe_allow_html=True)
st.markdown("<span class='marca-personal'>Dr. Carlos Aliaga Valdez</span>", unsafe_allow_html=True)

# --- BARRA LATERAL (ENTRADAS A CERO) ---
with st.sidebar:
    st.header("Configuración")
    rid = st.session_state.reset_id
    
    # Todos los campos inician en 0 para recibir nuevos datos
    p = st.number_input("Capital Principal (P)", min_value=0.0, value=0.0, key=f"p_{rid}")
    tn = st.number_input("Tasa Nominal (j %)", min_value=0.0, value=0.0, format="%.2f", key=f"tn_{rid}")
    d_tn = st.number_input("Periodo de la TN (días)", min_value=0, value=0, key=f"dtn_{rid}")
    d_cap = st.number_input("Periodo de Capitalización (días)", min_value=0, value=0, key=f"dcap_{rid}")
    plazo = st.number_input("Plazo del depósito (días)", min_value=0, value=0, key=f"plazo_{rid}")
    
    st.write("---")
    st.button("🔄 LIMPIAR PARA NUEVOS DATOS", on_click=limpiar_interfaz)

# --- LÓGICA DE CÁLCULO (Seguridad contra división por cero) ---
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
st.markdown("<p class='etiqueta-salida'>REPORTES DE SALIDA</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: st.metric("Frecuencia (m)", f"{m:.8f}")
with col2: st.metric("Capitalizaciones (n)", f"{n:.8f}")
with col3: st.metric("Tasa Efectiva", f"{i_ef:.8f}")

# --- RESULTADOS FINALES (AZUL INTENSO SIMÉTRICO) ---
st.markdown(f"""
    <div class='caja-azul'>
        <p class='texto-resultado'>MONTO COMPUESTO (S): {s:,.2f}</p>
    </div>
    <div class='caja-azul'>
        <p class='texto-resultado'>INTERÉS COMPUESTO (I): {interes:,.2f}</p>
    </div>
    """, unsafe_allow_html=True)
