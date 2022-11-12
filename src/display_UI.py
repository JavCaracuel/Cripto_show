from .libraries import *
from .kraken_functions import *
style = {'description_width': 'initial'}

button = widgets.Button(
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)

metricas = widgets.ToggleButtons(
    options=['Media movil', 'RSI'],
    description='Seleccione el tipo de métrtica que mostrar:',
    disabled=False,
    style=style,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltips=[""],
#     icons=['check'] * 3
)

divisa=widgets.RadioButtons(
    options=['EUR', 'USD'],
#    value='pineapple', # Defaults to 'pineapple'
#    layout={'width': 'max-content'}, # If the items' names are long
    style=style,
    description='Seleccione el tipo de divisa',
    disabled=False
)

intervalos=widgets.Dropdown(
    options=[1, 5, 15,30,60,240,1440,10080,21600],
    value=5,
    description='Seleccione intervalo:',
    style=style,
    disabled=False,
)
def display_criptos(divisa):
    pair_list=get_cripto_pairs(divisa)
    pair=widgets.Dropdown(
        options=pair_list,
        value=2,
        style=style,
        description='Elija la criptomoneda a mostrar:',
    )
    display(pair)
    return pair, pair_list

button = widgets.Button(description="Click Me!")
output = widgets.Output()

def on_button_clicked(b):
    with output:
        # clear_output(wait=True)
        # display(display_criptos(divisa.value))
        divisa.value
date=widgets.DatePicker(
    description='Pick a Date',
    disabled=False,
    style=style
)