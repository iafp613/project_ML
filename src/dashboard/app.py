import streamlit as st
import pandas as pd
import keras
import json
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
SEP = os.sep
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + SEP + 'resources')
import utils.mining_data_tb as mdtb





path = os.path.dirname(os.path.abspath(__file__))

# Cargar las imágenes
ruta_image = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + SEP + 'resources' + SEP + 'images' + SEP
calavera = Image.open(ruta_image + 'calavera.jpg')
btc_image = Image.open(ruta_image + 'btc.png')


# Cargar los DataFrames que se van a utilizar
ruta_data = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + SEP + 'data' + SEP
btc_train = pd.read_csv(ruta_data + SEP + 'entrenamiento' + SEP + 'BTC-USD.csv')
btc_test = pd.read_csv(ruta_data + SEP + 'testeo' + SEP + 'btc_test.csv')


st.set_page_config(
    page_title="Bitcoin",
    page_icon=calavera,
    layout="wide"
)
menu = st.sidebar.selectbox('Menu:',
            options=["Bienvenida", "Visualizaciones", "Predicción", "SQL", "API"])

if menu == 'Bienvenida':
    st.image(btc_image, width=200,output_format='png')
    st.sidebar.markdown('### Hola, me llamo *Nacho Fontal*')
    st.sidebar.markdown('Este es mi **segundo dashboard**, hecho el día *11/06/2021*')
    st.sidebar.markdown('Espero que te guste y puedas aprender más sobre ML')
    for i in range(9): st.sidebar.write("")
    st.sidebar.write('Link to my Github account [here](https://github.com/iafp613)')
    st.sidebar.write('Link to my public Tableau [here](https://public.tableau.com/shared/42RZT5MC5?:display_count=n&:origin=viz_share_link)')
    st.sidebar.write('Link to my LinkedIn profile [here](https://www.linkedin.com/in/iafp/)')
    st.sidebar.markdown('#### *Created by:*')
    st.sidebar.markdown('##### Nacho Fontal')
    st.markdown("# **BITCOIN**")
    st.markdown("### *Predicción de precio*")
    st.write('Ahora está muy de moda todo el tema de las criptomonedas. Si bien ya existen desde hace unos años, \
        su evolución y la facilidad de acceso a los pequeños y medianos inversores, han hecho que haya un boom en \
        la apuesta por esta forma de dinero. Antes de nada, hay que saber que toda inversión a corto, medio o largo \
        plazo supone un riesgo. Un riesgo que aumenta considerablemente en las criptomonedas frente a otro tipo de \
        divisas FIAT (o acciones en bolsa). Esto es debido a su alta volatilidad. Mientras que en la bolsa común se \
        manejan aumentos o descensos diarios de menos del 1% (normalmente), en el mercado cripto las variaciones diarias \
        están muy por encima de ese porcentaje. Aunque lo común es ver variaciones entre el 1 y el 5% diarias, pueden \
        haber picos de hasta un 20% o 40% diarios. Ni que decir tiene que es un altísimo riesgo del capital invertido. \
        Se puede ganar mucho, pero también se puede perder mucho. Por tanto, quiero aclarar que este proyecto no es, \
        ni mucho menos, una herramienta fiable para invertir eficazmente en este mercado. Más bien es un proyecto con \
        fines didácticos y de ejemplo de cómo usar el aprendizaje automático para hacer una aproximación predictora del \
        precio futuro. Evidentemente entran en juego muchos factores humanos que no se tienen en cuenta en este \
        proyecto debido a que son difícilmente cuantificables y predecibles. El simple hecho de que un día, una gran \
        empresa como Amazon, permita comprar sus productos con bitcoins, daría un impulso a su precio. O basta un tweet \
        negativo de Elon Musk (como ya vimos), para hacer caer el precio casi un 40%. Además es un mercado que está \
        bastante influenciado por el FOMO (fear of missing out) y, por tanto, también depende mucho de las sensaciones \
        de los inversores.')
    st.write('El objetivo de esta aplicación es poder predecir el precio que tendrá Bitcoin en función del volumen y \
        los demás precios.')

if menu == 'Visualizaciones':
    list0 = ['---', 'Datos', 'Gráficos']
    list1 = [
        '---',
        'Todos los datos', 
        'Evolución del precio de cierre', 
        'Evolución del volumen' 
    ]
    list2 = [
        '---',
        'Evolución del precio de Bitcoin',
        'Evolución del volumen de Bitcoin'
    ]
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Datos y Visualizaciones')
    st.write("En esta sección podrás ver los datos y algunas gráficas sobre ellos.")
    
    platform_0 = st.selectbox('Primero, elige una opción:', options=list0)
    if platform_0 == 'Datos':
        platform_1 = st.selectbox('Selecciona los datos:', options=list1)
        if platform_1 == 'Todos los datos':
            if st.button('Mostrar'):
                st.table(btc_train)

        if platform_1 == 'Evolución del precio de cierre':
            if st.button('Mostrar'):
                st.table(btc_train[['Date', 'Close']])

        if platform_1 == 'Evolución del volumen':
            if st.button('Mostrar'):
                st.table(btc_train[['Date', 'Volume']])
    
    if platform_0 == 'Gráficos':
        platform_2 = st.selectbox('Elije los datos que quieres ver', options=list2)
        if platform_2 == 'Evolución del precio de Bitcoin':
            fig = plt.figure(dpi=100, figsize=(10,7))
            ax = fig.gca()
            sns.lineplot(x=btc_train['Date'], y=btc_train['Close'], data=btc_train, ax=ax, color='red', linewidth=1)
            ax.set_ylabel("Precio (USD)")
            ax.set_xlabel("Tiempo")
            ax.set_title("Evolución del precio de Bitcoin")
            st.pyplot()

        if platform_2 == 'Evolución del volumen de Bitcoin':
            fig = plt.figure(dpi=100, figsize=(10,6))
            ax = fig.gca()
            sns.lineplot(x=btc_train['Date'], y=btc_train['Volume'], data=btc_train, ax=ax, color='red', linewidth=1)
            ax.set_ylabel("Volumen")
            ax.set_xlabel("Tiempo")
            ax.set_title("Evolución del volumen de Bitcoin")
            st.pyplot()     


if menu == 'Predicción':
    btc_test.columns = ['fecha', 'apertura', 'maximo', 'minimo', 'cierre', 'cierre_ajustado', 'volumen']
    btc_test.drop(['cierre', 'cierre_ajustado', 'fecha'], axis=1, inplace=True)
    modelo_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + SEP + 'models' + SEP
    list3 = [
        '---', 
        'Red Neuronal Adam Relu', 
        'Red Neuronal Rmsprop Relu', 
        'Red Neuronal LSTM con Dropout', 
        'Red Neuronal LSTM sin DropOut', 
        'Red Neuronal LSTM Rmsprop', 
        'Red Neuronal LSTM Rmsprop 500 neuronas'
    ]
    platform_0 = st.selectbox('Primero, elige una opción:', options=list3)
    if platform_0 == 'Red Neuronal Adam Relu':
        st.write('Es una red neuronal con un modo de activación Relu, optimizador ADAM y dos capas ocultas: \
            la primera de 50 neuronas y la segunda de 25. Una capa de salida con una neurona y un entrenamiento \
            de 1000 épocas.')
        model = keras.models.load_model(modelo_path + 'mejores_pesos_adam_relu.hdf5')
        st.write(model.summary())
        x = st.number_input('Precio de apertura', min_value=0, max_value=80000)
        y = st.number_input('Precio maximo', min_value=0, max_value=80000)
        z = st.number_input('Precio minimo', min_value=0, max_value=80000)
        v = st.number_input('Precio volumen', min_value=10000000, max_value=5000000000000)
        nuevos_datos = [(x, y, z, v)]
        nuevo_df=pd.DataFrame(nuevos_datos, columns = ['apertura' , 'maximo', 'minimo', 'volumen'])
        btc_para_testeo = btc_test.append(nuevo_df, ignore_index=True)
        mdtb.normalizar(btc_para_testeo, 'apertura')
        mdtb.normalizar(btc_para_testeo, 'maximo')
        mdtb.normalizar(btc_para_testeo, 'minimo')
        mdtb.normalizar(btc_para_testeo, 'volumen')
        if st.button('Mostrar predicción'):
            st.success('NOTA: La predicción está en la última fila de la tabla.')
            st.table(model.predict(btc_para_testeo))
    
    if platform_0 == 'Red Neuronal Rmsprop Relu':
        st.write('Es una red neuronal con un modo de activación Relu, optimizador RMSprop y dos capas ocultas: \
            la primera de 50 neuronas y la segunda de 25. Una capa de salida con una neurona y un entrenamiento \
            de 1000 épocas.')
        model = keras.models.load_model(modelo_path + 'mejores_pesos_rmsprop_relu.hdf5')
        x = st.number_input('Precio de apertura', min_value=0, max_value=80000)
        y = st.number_input('Precio maximo', min_value=0, max_value=80000)
        z = st.number_input('Precio minimo', min_value=0, max_value=80000)
        v = st.number_input('Precio volumen', min_value=10000000, max_value=5000000000000)
        nuevos_datos = [(x, y, z, v)]
        nuevo_df=pd.DataFrame(nuevos_datos, columns = ['apertura' , 'maximo', 'minimo', 'volumen'])
        btc_para_testeo = btc_test.append(nuevo_df, ignore_index=True)
        mdtb.normalizar(btc_para_testeo, 'apertura')
        mdtb.normalizar(btc_para_testeo, 'maximo')
        mdtb.normalizar(btc_para_testeo, 'minimo')
        mdtb.normalizar(btc_para_testeo, 'volumen')
        if st.button('Mostrar predicción'):
            st.success('NOTA: La predicción está en la última fila de la tabla.')
            st.table(model.predict(btc_para_testeo))

    if platform_0 == 'Red Neuronal LSTM con Dropout':
        st.markdown('Es una red neuronal recurrente **LSTM** con un optimizador adam y dos capas: la primera LSTM de 100 \
            neuronas y la segunda Dense de 50, con dropout. Una capa de salida con una neurona y un entrenamiento \
            de 10 épocas. Tiene un parámetro `patience=5`, lo que significa que debe de esperar al menos 5 épocas \
            sin que haya mejoras para activar el EarlyStopping.')
        model = keras.models.load_model(modelo_path + 'mejores_pesos_lstm_conDO.hdf5')
        x = st.number_input('Precio de apertura', min_value=0, max_value=80000)
        y = st.number_input('Precio maximo', min_value=0, max_value=80000)
        z = st.number_input('Precio minimo', min_value=0, max_value=80000)
        v = st.number_input('Precio volumen', min_value=10000000, max_value=5000000000000)
        nuevos_datos = [(x, y, z, v)]
        nuevo_df=pd.DataFrame(nuevos_datos, columns = ['apertura' , 'maximo', 'minimo', 'volumen'])
        btc_para_testeo = btc_test.append(nuevo_df, ignore_index=True)
        mdtb.normalizar(btc_para_testeo, 'apertura')
        mdtb.normalizar(btc_para_testeo, 'maximo')
        mdtb.normalizar(btc_para_testeo, 'minimo')
        mdtb.normalizar(btc_para_testeo, 'volumen')
        if st.button('Mostrar predicción'):
            st.success('NOTA: La predicción está en la última fila de la tabla.')
            st.table(model.predict(btc_para_testeo))

    if platform_0 == 'Red Neuronal LSTM sin DropOut':
        st.markdown('Es una red neuronal recurrente **LSTM** con un optimizador adam y dos capas: la primera LSTM de 100 \
            neuronas y la segunda Dense de 50, sin dropout. Una capa de salida con una neurona y un entrenamiento \
            de 10 épocas. Tiene un parámetro `patience=5`.')
        model = keras.models.load_model(modelo_path + 'mejores_pesos_lstm_sinDO.hdf5')
        x = st.number_input('Precio de apertura', min_value=0, max_value=80000)
        y = st.number_input('Precio maximo', min_value=0, max_value=80000)
        z = st.number_input('Precio minimo', min_value=0, max_value=80000)
        v = st.number_input('Precio volumen', min_value=10000000, max_value=5000000000000)
        nuevos_datos = [(x, y, z, v)]
        nuevo_df=pd.DataFrame(nuevos_datos, columns = ['apertura' , 'maximo', 'minimo', 'volumen'])
        btc_para_testeo = btc_test.append(nuevo_df, ignore_index=True)
        mdtb.normalizar(btc_para_testeo, 'apertura')
        mdtb.normalizar(btc_para_testeo, 'maximo')
        mdtb.normalizar(btc_para_testeo, 'minimo')
        mdtb.normalizar(btc_para_testeo, 'volumen')
        if st.button('Mostrar predicción'):
            st.success('NOTA: La predicción está en la última fila de la tabla.')
            st.table(model.predict(btc_para_testeo))

    if platform_0 == 'Red Neuronal LSTM Rmsprop':
        st.markdown('Es una red neuronal recurrente **LSTM** con un optimizador RMSprop y dos capas: la primera LSTM de 100 \
            neuronas y la segunda Dense de 50, con dropout. Una capa de salida con una neurona y un entrenamiento \
            de 10 épocas. Tiene un parámetro `patience=5`.')
        model = keras.models.load_model(modelo_path + 'mejores_pesos_lstm_rmsprop.hdf5')
        x = st.number_input('Precio de apertura', min_value=0, max_value=80000)
        y = st.number_input('Precio maximo', min_value=0, max_value=80000)
        z = st.number_input('Precio minimo', min_value=0, max_value=80000)
        v = st.number_input('Precio volumen', min_value=10000000, max_value=5000000000000)
        nuevos_datos = [(x, y, z, v)]
        nuevo_df=pd.DataFrame(nuevos_datos, columns = ['apertura' , 'maximo', 'minimo', 'volumen'])
        btc_para_testeo = btc_test.append(nuevo_df, ignore_index=True)
        mdtb.normalizar(btc_para_testeo, 'apertura')
        mdtb.normalizar(btc_para_testeo, 'maximo')
        mdtb.normalizar(btc_para_testeo, 'minimo')
        mdtb.normalizar(btc_para_testeo, 'volumen')
        if st.button('Mostrar predicción'):
            st.success('NOTA: La predicción está en la última fila de la tabla.')
            st.table(model.predict(btc_para_testeo))

    if platform_0 == 'Red Neuronal LSTM Rmsprop 500 neuronas':
        st.markdown('Es una red neuronal recurrente **LSTM** con un optimizador RMSprop y dos capas: la primera LSTM de 500 \
            neuronas y la segunda Dense de 50, con dropout. Una capa de salida con una neurona y un entrenamiento \
            de 10 épocas. Tiene un parámetro `patience=5`.')
        model = keras.models.load_model(modelo_path + 'mejores_pesos_lstm_rmsprop500.hdf5')
        x = st.number_input('Precio de apertura', min_value=0, max_value=80000)
        y = st.number_input('Precio maximo', min_value=0, max_value=80000)
        z = st.number_input('Precio minimo', min_value=0, max_value=80000)
        v = st.number_input('Precio volumen', min_value=10000000, max_value=5000000000000)
        nuevos_datos = [(x, y, z, v)]
        nuevo_df=pd.DataFrame(nuevos_datos, columns = ['apertura' , 'maximo', 'minimo', 'volumen'])
        btc_para_testeo = btc_test.append(nuevo_df, ignore_index=True)
        mdtb.normalizar(btc_para_testeo, 'apertura')
        mdtb.normalizar(btc_para_testeo, 'maximo')
        mdtb.normalizar(btc_para_testeo, 'minimo')
        mdtb.normalizar(btc_para_testeo, 'volumen')
        if st.button('Mostrar predicción'):
            st.success('NOTA: La predicción está en la última fila de la tabla.')
            st.table(model.predict(btc_para_testeo))


if menu == 'API':
    st.markdown('## Aquí podrás ver los datos originales, después de limpiarlos')
    st.markdown('#### Solo las personas autorizadas podrán acceder a esta sección')
    user_input = st.text_input('Por favor, escribe la contraseña', type='password')
    password_file = os.path.dirname(os.path.dirname(__file__)) + SEP + 'api' + SEP + 'password.json'
    with open(password_file, "r") as json_pass_readed:
        json_password = json.load(json_pass_readed)
    if st.button('Login'):
        if user_input == json_password['password']:
            st.success('Eres una persona acreditada')
            st.balloons()
            try:
                x = pd.read_json('http://localhost:6060/get/df?tok=' + user_input)
                st.write(x)
            except:
                st.warning('El administrador debe inicializar la API primero')
        else:
            st.warning('Contraseña incorrecta. Prueba de nuevo.')
    