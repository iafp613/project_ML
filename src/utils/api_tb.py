import os
SEP = os.sep
import pandas as pd
ruta = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'data' + SEP + 'entrenamiento' + SEP + 'BTC-USD.csv'

def preparar_datos():
    datos = pd.read_csv(ruta)
    return datos.to_json()

