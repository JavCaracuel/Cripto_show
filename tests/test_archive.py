import sys
sys.path.append('./src/')
import kraken_functions
from kraken_functions import krakenex
from kraken_functions import KrakenAPI
from kraken_functions import get_cripto_pairs,recoger_datos,calcular_media_movil_simple,calcular_media_movil_exponencial
from libraries import *
import pytest

def test_get_cripto_pairs():
    assert type(get_cripto_pairs('EUR'))== list
def test_recoger_datos():
    df=pd.DataFrame()
    data=recoger_datos('ADAEUR', 5)
    assert type(data)==type(df)