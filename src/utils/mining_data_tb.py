
def nombres_columnas(df):
    print('Las columnas actuales son:', df.columns)
    df.columns = ['fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'cierre_ajustado', 'volumen']
    print('------------------------------------------------')
    print('Las nuevas columnas son:', df.columns)
    return df



def eliminar_columnas(df, columna):
    df.drop([columna], axis=1, inplace=True)
    print('######## ATENCIÓN ########')
    print(f'La columna "{columna}" ha sido eliminada del DataFrame')
    return df


def analisis_df(data):
    '''Imprime a partir de DataFrame:
    La cantidad de filas y columnas que contiene.
    La información general.
    Una breve descripción estadística de los datos.
    La cantidad de valores NaN que tiene por columna.

    Parámetros:
    data ---> Un DataFrame.

    '''
    print('-----------------------# FILAS Y COLUMNAS #-------------------------')
    print(f'Cantidad de filas: {data.shape[0]} \nCantidad de columnas: {data.shape[1]}')
    print('\n----------------------# INFORMACIÓN GENERAL #-----------------------')
    print(data.info())
    print('\n-------------------# DESCRIPCIÓN ESTADÍSTICA #----------------------')
    print(data.describe())
    print('\n---------------------# CANTIDAD VALORES NaN #-----------------------')
    print('Valores NaN por columna:','\n', data.isnull().sum())
    print('Valores NaN totales en todo el DataFrame:', data.isnull().sum().sum())


def normalizar(df, name, normalized_low=0, normalized_high=1, data_low=None, data_high=None):
    if data_low is None:
        data_low = min(df[name])
        data_high = max(df[name])
    df[name] = ((df[name] - data_low) / (data_high - data_low)) * (normalized_high - normalized_low) + normalized_low