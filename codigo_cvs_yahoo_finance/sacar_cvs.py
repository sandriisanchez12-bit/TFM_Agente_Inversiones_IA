import yfinance as yf

activos = {
    "Oro2": "GC=F",
    "Plata2": "SI=F",
    "Cobre2": "HG=F",
    "Petroleo_WTI2": "CL=F",
    "Gas_Natural2": "NG=F",
    "NASDAQ2": "^IXIC",
    "SP5002": "^GSPC",
    "Dolar2": "DX-Y.NYB",      
    "VIX2": "^VIX"     

}

for nombre, ticker in activos.items():

    datos = yf.download(
        ticker,
        start="1995-01-01",
        end="2026-01-01",
        auto_adjust=True
    )

    datos.to_csv(f"{nombre}.csv")

    print(f"{nombre}: {len(datos)} registros descargados")