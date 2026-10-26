
import streamlit as st

st.set_page_config(page_title="Product Hunter AI", page_icon="🛍️", layout="centered")

st.title("🛍️ Product Hunter AI")
st.markdown("### Validador de Productos y Calculadora de Márgenes para E-commerce")

tab1, tab2 = st.tabs(["📊 Calculadora de Márgenes", "✅ Checklist de Validación"])

with tab1:
    st.subheader("Calculadora de Rentabilidad")
    precio_venta = st.number_input("Precio de venta al público (€)", value=29.99, step=1.0)
    costo_producto = st.number_input("Coste de adquisición / Proveedor (€)", value=5.00, step=0.5)
    costo_envio = st.number_input("Coste de envío / Logística (€)", value=3.50, step=0.5)
    publicidad_cpa = st.number_input("CPA estimado (Coste por Adquisición Publicitaria) (€)", value=8.00, step=0.5)

    if st.button("Calcular Beneficios"):
        costes_totales = costo_producto + costo_envio + publicidad_cpa
        beneficio_neto = precio_venta - costes_totales
        margen = (beneficio_neto / precio_venta) * 100 if precio_venta > 0 else 0

        st.metric(label="Beneficio Neto por Unidad", value=f"{beneficio_neto:.2f} €")
        st.metric(
