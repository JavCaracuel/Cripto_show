import sys
sys.path.append('./src/')
import kraken_functions
from kraken_functions import get_cripto_pairs,recoger_datos,calcular_media_movil_simple,calcular_media_movil_exponencial, calcular_rsi
from libraries import *
import pytest

'''
Se presentan los test de cobertura para las funciones contenidas en el archivo kraken_functions.py
'''

def test_get_cripto_pairs():
    assert type(get_cripto_pairs('EUR')) == list

def test_recoger_datos():
    df = pd.DataFrame()
    data = recoger_datos('ADAEUR', 5)
    assert type(data)==type(df)

def test_calcular_media_movil_simple():
    df = pd.DataFrame()
    # Recogida de datos con Krakenex:
    data=kraken_functions.recoger_datos('ADAEUR', 5)

    # Cambiar el tiempo de timestamp a datetime (meter en src)
    data['time_dt'] = pd.to_datetime(data['time'], unit='s')
    data = calcular_media_movil_simple(data, 10)
    assert type(data)==type(df)

def test_calcular_media_movil_exponencial():
    df = pd.DataFrame()
    data=kraken_functions.recoger_datos('ADAEUR', 5)

    # Cambiar el tiempo de timestamp a datetime (meter en src)
    data['time_dt'] = pd.to_datetime(data['time'], unit='s')
    data = calcular_media_movil_exponencial(data, 10)
    assert type(data)==type(df)

def test_calcular_rsi():
    data=kraken_functions.recoger_datos('ADAEUR', 5)

    # Cambiar el tiempo de timestamp a datetime (meter en src)
    data['time_dt'] = pd.to_datetime(data['time'], unit='s')
    rsi = calcular_rsi(data, 10)
    assert type(rsi)==type(list())