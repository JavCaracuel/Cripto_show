import sys
sys.path.append('./libraries')
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