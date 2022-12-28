import sys
sys.path.append('./src/')
import kraken_functions
from libraries import *

#### SELECCIÓN DE VARIABLES DE CONTORNO ####
# Título de la aplicación: 
st.title("Cripto Show")

# Selección de la divisa:
divisas=['EUR', 'USD']
selected_divisa=st.selectbox('Elije una divisa:',divisas)
st.write(f'Has seleccionado la divisa: {selected_divisa}')

# Selección del intervalo de las velas: 
intervals=[1, 5, 15, 30, 60, 240, 1440, 10080, 21600]
selected_interval=st.selectbox('Elije un intervalo en segundos:',intervals)
st.write(f'Has seleccionado el intervalo: {selected_divisa}')

# Selección de la criptomoneda:
if selected_divisa:
    pair_list=kraken_functions.get_cripto_pairs(selected_divisa)
    pair_list = [t[0] for t in pair_list]
selected_cripto=st.selectbox('Elije una divisa:',pair_list)
st.write(f'Has seleccionado la criptomoneda: {selected_cripto}')

# Selección de la ventana de media móvil:
ventana = st.slider("Selecciona la ventana de la media móvil", 1, 100, 20)



#### REPRESENTACIONES GRÁFICA ####
# Recogida de datos con Krakenex:
data=kraken_functions.recoger_datos(selected_cripto, selected_interval)

# Cambiar el tiempo de timestamp a datetime (meter en src)
data['time_dt'] = pd.to_datetime(data['time'], unit='s')

# Creación del gráfico de velas japonesas
from plotly.subplots import make_subplots
fig = make_subplots(specs=[[{"secondary_y": True}]])
#  fig = go.Figure()
fig.add_trace(go.Candlestick(
              x=data["time_dt"], 
              open=data["open"],
              high=data["high"],
              low=data["low"],
              close=data["close"],
              name="Candlestick"),
            secondary_y=False,
            )

# Generación del gráfico de media móvil simple: 
data = kraken_functions.calcular_media_movil_simple(data, ventana)
fig.add_trace(go.Scatter(x=data["time_dt"], 
                         y=data[f'ma_{ventana}'],
                         mode='lines', 
                         name=f'Media Simple - {ventana}',
                         line = dict(color='cyan', width=1)),
                        secondary_y=False,
                        )

# Generación del gráfico de media móvil exponencial:
data = kraken_functions.calcular_media_movil_exponencial(data, ventana)
fig.add_trace(go.Scatter(x=data["time_dt"], 
                         y=data[f'me_{ventana}'],
                         mode='lines', 
                         name=f'Media Exponencial - {ventana}',
                         line = dict(color='royalblue', width=1)),
                        secondary_y=False,
                        )

# Cálculo del RSI:
rsi_values = kraken_functions.calcular_rsi(data.copy(), ventana)
data[f"rsi_{ventana}"] = rsi_values
print(data)
fig.add_trace(go.Scatter(x=data["time_dt"], 
                         y=data[f'rsi_{ventana}'],
                         mode='lines', 
                         name=f'RSI - {ventana}',
                         line = dict(color='orange', width=1)),
                        secondary_y=True,
                        )

fig.update_layout(yaxis2=dict(side="right"))

# Representacion gráfica en la aplicación:
st.plotly_chart(fig)