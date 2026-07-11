import streamlit as st

def visualizacion_app():
    st.header('Análisis de acciones en Bolsa')
    st.write('A continuación, se van a visualizar análisis de diferentes categorías entre 2015 y 2026.')
    
    eleccion_visualizacion = st.radio("**Elige la categoría que desea analizar:**", ['Índices Bursátiles', 'Acciones Individuales','ETFs', 'Materias Primas'])
    st.write('-----------')


    if eleccion_visualizacion == 'Índices Bursátiles':
        st.subheader('Índices Bursátiles')
        st.write('A continuación, se comparan los siguientes índices:')
        st.markdown("""
        - S&P500
        - Nasdaq Composite
                    """)
        with st.expander('**Si desea más información sobre Indices Bursátiles:**'):
            st.write('Un índice bursátil es un indicador que mide el comportamiento de un grupo de empresas cotizadas. Su función es mostrar cómo evoluciona un mercado o sector.')
            st.markdown("""
            - **S&P 500 (^GSPC)**: Incluye aproximadamente 500 de las mayores empresas de Estados Unidos, por ello se considera el indicador más representativo de la economía estadounidense. Empresas como Apple, Microsoft, Amazon o Nvidia tienen gran peso.
            - **NASDAQ Composite (^IXIC)**: Incluye miles de empresas cotizadas en la bolsa NASDAQ. Este tiene una fuerte concentración tecnológica ya que está muy influenciado por Apple, Microsoft, Nvidia, Amazon y Meta.
                        """)
        
        if st.button('Mostrar gráficas de visualización'):
            st.write('A')
    
    elif eleccion_visualizacion == 'Acciones Individuales':
        st.subheader('Acciones Individuales')
        st.write('A continuación, se comparan las siguientes acciones individuales:')
        st.markdown("""
        - Apple Inc.
        - Microsoft Corporation
        - NVIDIA Corporation
        - Amazon.com, Inc.
        - Tesla, Inc.
        - Meta Platforms, Inc.
                    """)
        with st.expander('**Si desea más información sobre acciones individuales:**'):
            st.write('Una acción representa una pequeña parte de la propiedad de una empresa. Cuando compras una acción, estás participando en las ganancias o pérdidas de la empresa y el precio de esta depende de la oferta y demanada')
            st.markdown("""
            - **Apple Inc. (AAPL)**: Una de las empresas más valiosas del mundo, conocida por diseñar iPhones, iPads, Macs y servicios digitales.
            - **Microsoft Corporation (MSFT)**: Líder en software y computación en la nube. Este desarrolla Windows, Office y Azure.
            - **NVIDIA Corporation (NVDA)**: Una de las empresas más beneficiadas por el auge de la IA, ya que desarrolla GPUs y chips.
            - **Amazon.com, Inc. (AMZN)**: Empresa famosa tanto por su comercio electrónico como por Cloud computing mediante AWS.
            - **Tesla, Inc. (TSLA)**: Conocida por la fabricación de vehículos eléctricos, pero también se dedica a la energía solar y las baterías
            - **Meta Platforms, Inc. (META)**: Empresa propietaria de Facebook, Instagram y WhatsApp.  
                        """)
        
        if st.button('Mostrar gráficas de visualización'):
            st.write('B')
        
    
    elif eleccion_visualizacion == 'ETFs':
        st.subheader('ETFs')
        st.write('A continuación, se comparan los siguientes ETFs:')
        st.markdown("""
        - SPDR S&P 500 ETF Trust
        - Invesco QQQ Trust
        - Vanguard Total Stock Market ETF
        - iShares MSCI Emerging Markets ETF
                    """)
        with st.expander('**Si desea más información sobre ETFs:**'):
            st.write('ETF (Exchange Traded Fund): Es un fondo de inversión que cotiza en bolsa como si fuera una acción. Este puede contener cientos de acciones, bonos, materias primas y criptomonedas y su mayor ventaja es la diversificación.')
            st.markdown("""
            - **SPDR S&P 500 ETF Trust (SPY)**: Replica el comportamiento del S&P 500.
            - **Invesco QQQ Trust (QQQ)**: Replica el NASDAQ-100 y está muy centrado en tecnología.
            - **Vanguard Total Stock Market ETF (VTI)**: Incluye miles de empresas, prácticamente todo el mercado estadounidense
            - **iShares MSCI Emerging Markets ETF (EEM)**: Incluye empresas de mercados emergentes como China, India o Brasil, entre otros.
                        """)
        
        if st.button('Mostrar gráficas de visualización'):
            st.write('C')
        

    elif eleccion_visualizacion == 'Materias Primas':
        st.subheader('Materias Primas')
        st.write('A continuación, se comparan las siguientes materias primas:')
        st.markdown("""
        - Oro
        - Plata
        - Petróleo WTI
        - Gas Natural
        - Cobre
                    """)
        with st.expander('**Si desea más información sobre materias primas**'):
            st.write('Son recursos físicos que se compran y venden en mercados internacionales. Su precio depende de la oferta y la demanda, conflictos geopolíticos, clima y crecimiento económico.')
            st.markdown("""
            - **Oro (GC=F)**: Es un activo refugio, al cual acuden y sube cuando hay incertidumbre económica.
            - **Plata (SI=F)**: Utilizada tanto como inversión como en industria.
            - **Petróleo WTI (CL=F)**: Es la referencia principal del petróleo estadounidense. Este es muy sensible a guerras y decisiones de la OPEP (Organización de Países Exportadores de Petróleo).
            - **Gas Natural (NG=F)**: Fuente energética importante, el cual está muy influenciado por el clima.
            - **Cobre (HG=F)**: Es considerado un indicador adelantado de la actividad económica y se utiliza en construcción, electrónica y energía.
                        """)
        
        if st.button('Mostrar gráficas de visualización'):
            st.write('D')
        