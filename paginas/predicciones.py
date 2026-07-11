import streamlit as st
import pandas as pd
from pathlib import Path
from functools import reduce

def predicciones_app():
    st.subheader('Modelo predictivo')
    st.write('A continuación se va a realizar una comparación experimental, donde se busca confirmar si la siguiente hipótesis es cierta:')
    st.write('¿Mejora la capacidad predictiva de un modelo bursátil cuando se incorporan variables procedentes de índices, ETFs y materias primas?')

    #cargar datos
    ruta = Path('csvs_visualizacion')
    datos = {}
    for archivo in ruta.rglob('*.csv'):
        nombre = archivo.stem
        categoria = archivo.parent.name
        df = pd.read_csv(archivo, skiprows=2)
        rename_dict = {
            "Price": "Date",
            "Unnamed: 1": f"Price_Close_{nombre}",
            "Unnamed: 2": f"Price_High_{nombre}",
            "Unnamed: 3": f"Price_Low_{nombre}",
            "Unnamed: 4": f"Price_Open_{nombre}",
            "Unnamed: 5": f"Volume_{nombre}"
        }
        df = df.rename(columns=rename_dict)
        df = df.dropna()
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])

        datos[nombre] = {
            'Categoría': categoria,
            'df' : df
        }
        #print(datos.keys())
    #st.write(datos)

    #merge por fecha
    dfs = [info['df'] for info in datos.values()]

    df_final = reduce(
        lambda left, right: pd.merge(left, right, on='Date', how='outer'),
        dfs
    )
    df_final = df_final.sort_values('Date')
    df_final = df_final.set_index('Date')
    df_final = df_final.dropna()
    #st.write(df_final.head())

    #retorno y la volatilidad
    columnas_precios_cierre = [col for col in df_final.columns if col.startswith("Price_Close_")]

    retorno = df_final[columnas_precios_cierre].pct_change()
    retorno.columns = [col.replace("Price_Close_", "Return_") for col in retorno.columns]

    volatilidad = retorno.std()
    volatilidad = volatilidad.rename(lambda x: x.replace("Return_", "Volatility_"))

    volatilidad_movil = retorno.rolling(window=20).std() #volatilidad 20 días
    volatilidad_movil.columns = [
        col.replace("Return_", "Volatility_20d_") for col in volatilidad_movil.columns
    ]

    df_final = df_final.loc[:, ~df_final.columns.str.contains("Return_|Volatility_")]
    df_final = pd.concat([df_final, retorno, volatilidad_movil], axis=1)
    st.write(df_final)


    #limpieza de datos, primeras filas de retorno y volatilidad nan
    df_ml = df_final.iloc[20:].dropna()