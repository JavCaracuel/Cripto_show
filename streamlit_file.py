from src import kraken_functions
from src.libraries import *
from src.display_UI import *
st.title("Cripto Show")
divisas=['EUR', 'USD']
selected_divisa=st.selectbox('Elije una divisa:',divisas)
st.write(f'Has seleccionado la divisa: {selected_divisa}')
intervals=[1, 5, 15,30,60,240,1440,10080,21600]
selected_interval=st.selectbox('Elije un intervalo en segundos:',intervals)
st.write(f'Has seleccionado el intervalo: {selected_divisa}')
if selected_divisa:
    pair_list=get_cripto_pairs(selected_divisa)
    pair_list = [t[0] for t in pair_list]
selected_cripto=st.selectbox('Elije una divisa:',pair_list)
st.write(f'Has seleccionado la criptomoneda: {selected_cripto}')
data,_=kraken_functions.recoger_datos(selected_cripto, selected_interval)
fig = go.Figure(data=[go.Candlestick(
    x=data["time"],
    open=data["open"],
    high=data["high"],
    low=data["low"],
    close=data["close"]
)])
st.plotly_chart(fig)