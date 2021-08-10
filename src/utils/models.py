import numpy as np
import pandas as pd
import collections

def xy(df, target):
    '''Convierte un DataFrame de Pandas en variables x e y que necesita TensorFlow.
    Asegurando que los datos sean númericos de tipo float o int.
        Argumentos:
        df ----> DataFrame que queremos convertir.
        target ----> Nombre de la columna target (y)
    Retorna los datos transformados en arrays de Numpy.
    '''
    resultado = []
    for x in df.columns:
        if x != target:
            resultado.append(x)
    # Busca los tipos de la columna target. 
    target_type = df[target].dtypes
    target_type = target_type[0] if isinstance(target_type, collections.Sequence) else target_type
    # Codifica int o a float. Mejor con 32 bits para TensorFlow.
    if target_type in (np.int64, np.int32):
        dummies = pd.get_dummies(df[target])
        return df[resultado].values.astype(np.float32), dummies.values.astype(np.float32)
    else:
        return df[resultado].values.astype(np.float32), df[target].values.astype(np.float32)

def secuenciar(secuencia, df, data):
    '''Realiza una secuencia de los datos.
    Parámetros:
        secuencia ----> Tamaño de la secuencia
        df ----> Valores del DataFrame
        data ----> Datos del target
    Retorna dos arrays de NumPy (x, y)

    '''
    x = []
    y = []
    for i in range(len(data)-secuencia-1):
        #print(i)
        window = df[i:(i+secuencia)]
        after_window = data[i+secuencia]
        x.append(window)
        y.append(after_window)
    return np.array(x),np.array(y)
