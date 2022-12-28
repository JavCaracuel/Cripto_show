import sys
sys.path.append('libraries')
from libraries import krakenex
from libraries import KrakenAPI

def get_cripto_pairs(tipo):
    api = krakenex.API()
    k = KrakenAPI(api)
    aux=k.get_tradable_asset_pairs()
    aux=aux[aux["altname"].str.contains(tipo,case=False)]
    aux=aux["altname"]
    lista_aux=aux.to_list()
    lista=[]
    for i,j in enumerate(lista_aux):
        lista.append((j,i))
    return lista

def recoger_datos(moneda, intervalo):
    api = krakenex.API()
    k = KrakenAPI(api)
    ohlc,_ = k.get_ohlc_data(moneda, interval=intervalo)
    return ohlc

def calcular_media_movil_simple(data_close, ventana):
    data_close = data_close.sort_index(ascending=True)
    data_close[f'ma_{ventana}'] = data_close['close'].rolling(ventana, min_periods=1).mean()
    data_close = data_close.sort_index(ascending=False)
    return data_close

def calcular_media_movil_exponencial(data_close, ventana):
    data_close = data_close.sort_index(ascending=True)
    data_close[f'me_{ventana}'] = data_close['close'].ewm(span=ventana).mean()
    data_close = data_close.sort_index(ascending=False)
    return data_close

def calcular_rsi(data_close, ventana):
    import numpy as np
    data_close["cambio"] = (data_close["close"].shift(-1) - data_close["close"]) * (-1)  # Calcula el cambio diario en el precio de cierre
    data_close = data_close.reset_index(drop=True).sort_index()
    rsi_values =  [] # Vector para almacenar los valores del RSI. 
    for i, row in data_close.iterrows():
        # selección de la ventana
        try:
            data_ventana = data_close.iloc[i:i+ventana]
        except:
            data_ventana = data_close.iloc[i:]
        #cálculo de la media de los uintervalos de subida (up) y bajada (down)
        up = data_ventana[data_ventana["cambio"] > 0]["cambio"].mean()
        if np.isnan(up):
            up = 0
        down = data_ventana[data_ventana["cambio"] < 0]["cambio"].mean()
        if np.isnan(down):
            down = 0
        # cálculo del RSI:
        try: 
            rsi = 100 - (100 / (1 + (up / abs(down))))
        except ZeroDivisionError:
            rsi = 100 
        rsi_values.append(rsi)
    return rsi_values