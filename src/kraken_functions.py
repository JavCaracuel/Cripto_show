from .libraries import krakenex
from .libraries import KrakenAPI

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

def recoger_datos(moneda,since):
    api = krakenex.API()
    k = KrakenAPI(api)
    ohlc, last = k.get_ohlc_data(moneda,since=since)
    return ohlc, last