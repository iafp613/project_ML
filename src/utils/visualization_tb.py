import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn import metrics
from sklearn.metrics import r2_score


def grafica(tipo, datos, x, y, titulo):
    try:
        fig = plt.figure(dpi=100, figsize=(8,5))
        ax = fig.gca()
        if tipo == 'lineplot':
            sns.lineplot(x=x, y=y, data=datos, ax=ax, color='red', linewidth=1)
            ax.set_ylabel(y)
            ax.set_xlabel(x)
            return ax.set_title(titulo)
    except Exception as error:
        print('Ha ocurrido un error')


def grafica_interactiva(tipo, datos, x, y, titulo):
    try:
        if tipo == 'line':
            fig = px.line(datos, x=x, y=y, title=titulo)
            return fig.show()

        if tipo == 'scatter':
            fig = px.scatter(data_frame=datos, x=x, y=y, title=titulo)
            return fig.show()
    except Exception as error:
        print('Ha ocurrido un error')

def grafico_regresion(pred, y, sort=True):
    plt.figure(figsize=(15,6))
    t = pd.DataFrame({'pred' : pred, 'y' : y})
    if sort:
        t.sort_values(by=['y'],inplace=True)
    a = plt.plot(t['y'].tolist(),label='real')
    b = plt.plot(t['pred'].tolist(),label='predicción')
    plt.ylabel('salida')
    plt.legend()
    plt.show()


def visualizar_modelo(modelo, x_test, y_test):
    pred = modelo.predict(x_test)
    print("Shape: {}".format(pred.shape))
    score = np.sqrt(metrics.mean_squared_error(pred,y_test))
    print("Puntuación final (RMSE): {}".format(score))
    print('Puntuación R cuadrática: %2f' % r2_score(y_test,pred))
    grafico_regresion(pred.flatten()[0:100],y_test[0:100])
