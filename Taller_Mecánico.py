#Program to deploy a web app using streamlit and gspread to manage a mechanical workshop.
import streamlit as st
import pandas as pd
from datetime import datetime

st.title("🔧 Taller Mecánico")
st.markdown(f"📅 **Fecha:** {datetime.today().strftime('%d/%m/%Y')}")

# Enlaces
st.markdown(
    '[➕ Nueva Orden de Trabajo](https://docs.google.com/forms/d/1Hkv92UpsXGSGK7IJyPZzFnO8rDfoyOYqywR3rSd92T0/viewform?pli=1&pli=1&edit_requested=true) | '
    '[📊 Historial de Órdenes](https://docs.google.com/spreadsheets/d/1WgrSXq29ynLOtlT-zDRlrahWq0t0n_ZjYk8ZHplITTA/edit?resourcekey=&gid=1125927724#gid=1125927724)'
)

st.subheader("🛠️ Estado de unidades")

motivo = [
    "Mantenimiento Preventivo", "Motor y Transmisión", "Sistema hidráulico y Accesorios",
    "Sistema neumático y Frenos", "Suspensión o Dirección", "Llantas o Sistema de tracción",
    "Sistema de Control o eléctrico", "Chasis o Carrocería", "Sistema de Enfriamiento o Refrigeración"
]

nombres = [
    "Asignar","Flavio Hernandez", "David Aguayo", "Luis Nájera", "Taller/Personal Externo", "José Salas",
    "Ildefonso Reyes", "Noé Ordaz", "Llantero José", "Agustín", "Adán Gonzales", "Miguel Otero",
    "Jesús del Carmen", "Roy Galloso", "Julio Castillo", "Hiram Yammir", "Rafael Perez",
    "Esteban Cohuo", "Alberto Suarez", "Sin Asignar"
]

# Inicializar estado
if "data" not in st.session_state:
    st.session_state.data = []

if "mostrar_formulario" not in st.session_state:
    st.session_state.mostrar_formulario = False

# Botón que muestra/oculta el formulario
if st.button("Unidad Ingresa a Taller"):
    st.session_state.mostrar_formulario = not st.session_state.mostrar_formulario

# Formulario debajo de la tabla
if st.session_state.mostrar_formulario:
    with st.form("form_activo"):
        Unidad = st.text_input("🔩 Nombre del Activo")
        Estado = st.selectbox("📌 Estado", motivo)
        Encargado = st.selectbox("👨‍🔧 Encargado", nombres)
        Orden = st.number_input("🧾 Número de Orden", step=1)
        submitted = st.form_submit_button("➕ Agregar") #agregar junto a este botón, otro boton para cerrar el formulario. 'button("❌")'
        if submitted:
            nuevo = {
                "Unidad": Unidad,
                "Estado": Estado,
                "Encargado": Encargado,
                "Orden": int(Orden)
            }
            st.session_state.data.append(nuevo)
            st.session_state.mostrar_formulario = False
            

# Mostrar la tabla actualizada SIEMPRE
if st.session_state.data:
    st.subheader("📋 Unidades en taller")
    for i, item in enumerate(st.session_state.data):
        cols = st.columns([3, 3, 3, 2, 1])
        cols[0].write(f"🔩 {item['Unidad']}")
        cols[1].write(f"📌 {item['Estado']}")
        cols[2].write(f"👨‍🔧 {item['Encargado']}")
        cols[3].write(f"🧾 {item['Orden']}")
        if cols[4].button("❌", key=f"del_{i}"):
            st.session_state.data.pop(i)
            
#AttributeError: module 'streamlit' has no attribute 'experimental_rerun'
