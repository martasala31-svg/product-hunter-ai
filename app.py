import streamlit as st

st.set_page_config(page_title="LUXN Analytics", page_icon="📊", layout="centered")

st.title("📊 LUXN Analytics")
st.caption("Herramienta profesional para análisis de rentabilidad y viabilidad e-commerce.")

tab1, tab2, tab3 = st.tabs(["🧮 Calculadora", "🔥 Productos Ganadores", "📋 Checklist Viabilidad"])

with tab1:
    st.subheader("Calculadora de Rentabilidad")
    
    precio_venta = st.number_input("Precio de venta al público (con IVA) (€)", value=29.99, step=1.0)
    incluir_iva = st.checkbox("Descontar IVA (21% España/UE)", value=True)
    
    costo_producto = st.number_input("Coste de adquisición / Proveedor (€)", value=5.00, step=0.5)
    costo_envio = st.number_input("Coste de envío / Logística (€)", value=3.50, step=0.5)
    publicidad_cpa = st.number_input("CPA estimado (Coste por Adquisición Publicitaria) (€)", value=8.00, step=0.5)
    
    if st.button("Calcular Beneficios"):
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
            
        informe = f"""=================================
INFORME LUXN ANALYTICS
=================================
Precio Venta (PVP): {precio_venta:.2f} €
Coste Proveedor: {costo_producto:.2f} €
Coste Envío: {costo_envio:.2f} €
CPA Publicidad: {publicidad_cpa:.2f} €
---------------------------------
BENEFICIO NETO REAL: {beneficio_neto:.2f} €
MARGEN NETO: {margen:.1f}%
=================================
Generado por LUXN Analytics
"""
        st.download_button(
            label="📥 Descargar Informe LUXN",
            data=informe,
            file_name="informe_rentabilidad_LUXN.txt",
            mime="text/plain"
        )

with tab2:
    st.subheader("🔥 Catálogo de Productos Ganadores")
    st.write("Estructura de costes precargada de productos con alta demanda:")
    
    prod = st.selectbox("Selecciona un producto para ver su desglose:", [
        "Humidificador de Llama RGB",
        "Depiladora IPL Luz Pulsada",
        "Proyector de Galaxia / Estrellas"
    ])
    
    if prod == "Humidificador de Llama RGB":
        st.info("**PVP Sugerido:** 34.99 € | **Proveedor:** 7.50 € | **Envío:** 4.20 € | **CPA Publicidad:** 9.00 €")
        st.write("👉 **Beneficio Estimado:** ~8.22 € (23.5% Margen Neto)")
        st.caption("Puntos fuertes: Alto impacto visual en TikTok/Reels, ideal para compras de impulso.")
        
    elif prod == "Depiladora IPL Luz Pulsada":
        st.info("**PVP Sugerido:** 49.99 € | **Proveedor:** 14.00 € | **Envío:** 4.50 € | **CPA Publicidad:** 12.00 €")
        st.write("👉 **Beneficio Estimado:** ~10.81 € (21.6% Margen Neto)")
        st.caption("Puntos fuertes: Alta resolución de problema percibido, margen elevado.")
        
    elif prod == "Proyector de Galaxia / Estrellas":
        st.info("**PVP Sugerido:** 29.99 € | **Proveedor:** 6.00 € | **Envío:** 3.80 € | **CPA Publicidad:** 8.00 €")
        st.write("👉 **Beneficio Estimado:** ~6.99 € (23.3% Margen Neto)")
        st.caption("Puntos fuertes: Regalo estrella, facilísimo de promocionar con vídeos a oscuras.")

with tab3:
    st.subheader("📋 Checklist de Viabilidad de Producto")
    c1 = st.checkbox("¿Tiene 'Factor WOW' o resuelve un problema claro?")
    c2 = st.checkbox("¿El precio de venta percibido supera los 25€ - 30€?")
    c3 = st.checkbox("¿Es fácil y seguro de enviar (ligero/no frágil)?")
    c4 = st.checkbox("¿Existen vídeos publicitarios viables en TikTok/Reels?")
    
    puntuacion = sum([c1, c2, c3, c4])
    st.write(f"**Puntuación:** {puntuacion} / 4")
    
    if puntuacion == 4:
        st.success("🟢 Producto Altamente Viable para E-commerce.")
    elif puntuacion >= 2:
        st.warning("🟡 Viabilidad Media. Requiere testear muy bien la publicidad.")
    else:
        st.error("🔴 Riesgo Alto. Se recomienda buscar otro producto.")
