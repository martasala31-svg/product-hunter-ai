import streamlit as st

st.set_page_config(page_title="Product Hunter AI", page_icon="🛍️", layout="centered")

st.title("🛍️ Product Hunter AI")
st.markdown("### Validador de Productos y Calculadora de Márgenes para E-commerce")

tab1, tab2 = st.tabs(["📊 Calculadora de Márgenes", "✅ Checklist de Validación"])

with tab1:
    st.subheader("Calculadora de Rentabilidad")
    
    precio_venta = st.number_input("Precio de venta al público (con IVA) (€)", value=29.99, step=1.0)
    incluir_iva = st.checkbox("Descontar IVA (21% España/UE)", value=True)
    
    costo_producto = st.number_input("Coste de adquisición / Proveedor (€)", value=5.00, step=0.5)
    costo_envio = st.number_input("Coste de envío / Logística (€)", value=3.50, step=0.5)
    publicidad_cpa = st.number_input("CPA estimado (Coste por Adquisición Publicitaria) (€)", value=8.00, step=0.5)

    if st.button("Calcular Beneficios"):
        # Cálculo de IVA
        precio_base = precio_venta / 1.21 if incluir_iva else precio_venta
        iva_pagado = precio_venta - precio_base if incluir_iva else 0
        
        costes_totales = costo_producto + costo_envio + publicidad_cpa
        beneficio_neto = precio_base - costes_totales
        margen = (beneficio_neto / precio_venta) * 100 if precio_venta > 0 else 0

        st.divider()
        st.metric(label="Beneficio Neto Real por Unidad", value=f"{beneficio_neto:.2f} €")
        st.metric(label="Margen de Beneficio Neto", value=f"{margen:.1f}%")
        
        if incluir_iva:
            st.caption(f"ℹ️ Se han descontado {iva_pagado:.2f} € de IVA del precio de venta.")

        if beneficio_neto > 10:
            st.success("¡Excelente margen! Este producto es muy viable para E-commerce.")
        elif beneficio_neto > 0:
            st.warning("Margen ajustado. Vigila los costes de publicidad.")
        else:
            st.error("¡Cuidado! Estás perdiendo dinero con este precio y costes.")

        # Generador de informe para descargar
        informe = f"""--- INFORME PRODUCT HUNTER AI ---
Precio Venta: {precio_venta:.2f} €
Coste Proveedor: {costo_producto:.2f} €
Coste Envío: {costo_envio:.2f} €
CPA Publicidad: {publicidad_cpa:.2f} €
---------------------------------
BENEFICIO NETO: {beneficio_neto:.2f} €
MARGEN NETO: {margen:.1f}%
---------------------------------
"""
        st.download_button("📥 Descargar Informe", informe, file_name="analisis_producto.txt")

with tab2:
    st.subheader("Checklist de Producto Ganador")
    c1 = st.checkbox("¿Resuelve un problema claro o aporta un factor 'WOW'?")
    c2 = st.checkbox("¿Tiene un precio percibido superior a 25-30€?")
    c3 = st.checkbox("¿Es fácil de enviar y no es frágil ni voluminoso?")
    c4 = st.checkbox("¿Hay creatividades o vídeos virales disponibles para anuncios?")

    puntuacion = sum([c1, c2, c3, c4])
    st.markdown(f"**Puntuación de viabilidad:** {puntuacion} / 4")
    
    if puntuacion == 4:
        st.success("¡Producto altamente viable! Listo para testear en campañas.")
    elif puntuacion >= 2:
        st.info("Producto moderado. Analiza bien la competencia.")
    else:
        st.warning("Pocos puntos positivos. Te sugerimos buscar otra alternativa.")
