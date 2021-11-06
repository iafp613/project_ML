<h1 align="center"> Bitcoin. Predicción de precio - Proyecto individual de Machine Learning.</h1>
<p align="center"><img src="https://phantom-expansion.unidadeditorial.es/398c5ec1e2602e119b85119ef761b11e/crop/0x1068/1414x2008/resize/414/f/jpg/assets/multimedia/imagenes/2020/11/22/16060757043088.jpg"/></p>

_Ahora está muy de moda todo el tema de las criptomonedas. Si bien ya existen desde hace unos años, su evolución y la facilidad de acceso a los pequeños y medianos inversores, han hecho que haya un boom en la apuesta por esta forma de dinero._

_Antes de nada, hay que saber que toda inversión a corto, medio o largo plazo supone un riesgo. Un riesgo que aumenta considerablemente en las criptomonedas frente a otro tipo de divisas FIAT (o acciones en bolsa). Esto es debido a su alta volatilidad. Mientras que en la bolsa común se manejan aumentos o descensos diarios de menos del 1% (normalmente), en el mercado cripto las variaciones diarias están muy por encima de ese porcentaje. Aunque lo común es ver variaciones entre el 1 y el 5% diarias, pueden haber picos de hasta un 20% o 40% diarios. Ni que decir tiene que es un altísimo riesgo del capital invertido. Se puede ganar mucho, pero también se puede perder mucho._

_Por tanto, quiero aclarar que este proyecto no es, ni mucho menos, una herramienta fiable para invertir eficazmente en este mercado. Más bien es un proyecto con fines didácticos y de ejemplo de cómo usar el aprendizaje automático para hacer una aproximación predictora del precio futuro. Evidentemente entran en juego muchos factores humanos que no se tienen en cuenta en este proyecto debido a que son difícilmente cuantificables y predecibles. El simple hecho de que un día, una gran empresa como Amazon, permita comprar sus productos con bitcoins, daría un impulso a su precio. O basta un tweet negativo de Elon Mask (como ya vimos), para hacer caer el precio casi un 40%. Además es un mercado que está bastante influenciado por el FOMO (fear of missing out) y, por tanto, también depende mucho de las sensaciones de los inversores._

_Después de esta aclaración, el propósito del proyecto no es más que aplicar varios conceptos de Machine Learning a un tema tan actual para intentar acercarse a una predicción del precio de Bitcoin._

![GitHub watchers](https://img.shields.io/github/watchers/iafp613/project_ML?style=social)


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo, pruebas o visualización._

Dentro de la carpeta `src` están contenidos todos los archivos ejecutables. El notebook principal es `main`, el cual contiene toda la información del proceso de limpieza, visualización de datos y machine learning. 

Dentro de `utils`, los archivos `folders_tb.py`, `visualization_tb.py` y `mining_data_tb.py` contienen las funcionalidades que se importan en el notebook principal. El archivo `dashboard_tb.py`contiene las funcionalidades para ejecutar el dashboard y el archivo `api_tb` las necesarias para ejecutar la API.

En la carpeta `dashboard` encontramos `app.py` y todo el código necesario para poder ver el trabajo mediante Streamlit.

En la carpeta `api` hay un archivo `server.py` que contiene el código para ejecutar una API que nos retornará un *json* con todos los datos limpios. Para ejecutar la API desde la consola o desde el menú de Streamlit, se requieren dos contraseñas que no se han subido al repositorio (por seguridad). Así que, aunque el código es visible, no se podrá ejecutar.

Si nos vamos a la carpeta `data`, podemos acceder a todos los archivos .csv que se han utilizado en este proyecto. En `resources` encontraremos copias de las gráficas, imágenes y datos definitivos utilizados. Y, por último, en la carpeta `models` encontraremos los pesos de los modelos que se han utilizado en este proyecto.


### Pre-requisitos 📋

_Para poder ejecutar el código entero, necesitarás tener instaladas una serie de librerías (así como Python v.3.7.4). Todas las librerías que se han usado son:_

```
os 
sys
pandas
numpy 
pyplot
csv
seaborn
json
flask
argparse
streamlit 
keras
request
time
sklearn

```


### Instalación 🔧

**Recuerda:**

*En la terminal del sistema operativo:*

```
pip3 install pandas
```

```
pip3 install numpy
```
*Etc.*


## Construido con 🛠️

* [VSC](https://code.visualstudio.com/download) - Editor de código
* [OPENCV](https://opencv.org/) - Visión por computador


![Your Repository's Stats](https://github-readme-stats.vercel.app/api/top-langs/?username=iafp613&theme=blue-green)


## Contribuyendo 🖇️

*Por favor, déjame una estrella en mi perfil y/o hazme un follow, ayudas a seguir subiendo más contenido.* 😊

![GitHub followers](https://img.shields.io/github/followers/iafp613?style=social)
![GitHub User's stars](https://img.shields.io/github/stars/iafp613?style=social)
![GitHub forks](https://img.shields.io/github/forks/iafp613/projects_tb?style=social)



## Autor ✒️

* **Nacho Fontal** - *Proyecto* - [![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/iafp/)


## Licencia 📄

Este proyecto está bajo la Licencia (mira el archivo [LICENSE.md](LICENSE.md) para detalles).


## Expresiones de Gratitud 🎁

Muchísimas gracias a todo el equipo de The Bridge School y, en especial, a mis profesores:
* *Gabriel Vázquez Torres, Leonardo Sánchez y Borja Puig de la Bellacasa* 📢 
* Porque gracias a vosotros y a vuestra paciencia, en menos de dos meses, he aprendido muchísimo 🤓.
* ¡Os debo una cerveza 🍺 o un café ☕! ¡Gracias de corazón!
---