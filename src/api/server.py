import os, sys
from flask import Flask, request
import json
#import argparse
SEP = os.sep
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.api_tb as atb


#parser = argparse.ArgumentParser()
#parser.add_argument("-x", type=str, help="Introduce la contraseña correcta", required=True)
#args = vars(parser.parse_args())

# ----------------------
# $$$$$$$ FLASK $$$$$$$$
# ----------------------

app = Flask(__name__)  # init

@app.route("/") 
def home():
    mensaje = " <h1> Análisis del Bitcoin </h1> <p> Datos sobre la evolución de BTC-USD <h3>"
    mensaje +=  "<br>" + " <h6> Token: DNI con la letra, sin espacios ni caracteres especiales. </h6>"
    return mensaje

# ----------------------
# $$$$$$$ FLASK GET $$$$$$$$
# ----------------------

@app.route('/get/df', methods=['GET'])
def api_df():
    """
    Recibe como argumento un token. Si es válido (según las especificaciones), retorna un archivo resumido y depurado con los datos
    Busca los datos en el directorio /resources/dataset. EL directorio resources está al mismo nivel que el directorio src
    """
    token_id = None
    password_file = os.path.dirname(os.path.abspath(__file__)) + SEP + "password.json"
    with open(password_file, "r") as json_pass_readed:
        json_password = json.load(json_pass_readed)
    if 'tok' in request.args:
        token_id = str(request.args['tok'])
    if token_id == json_password['password']:           
        resp =  atb.preparar_datos()      
        return resp
    else:
        return "<h1> Error: Invalid Token" + "<br>" + "<br>" + '<h4> Please, insert the correct ID'

# ----------------------
# $$$$$$$ MAIN $$$$$$$$
# ----------------------

def main():
    

    print("---------STARTING PROCESS---------")
    print(os.path.dirname(os.path.abspath(__file__)))
    
    # Get the settings fullpath
    settings_file = os.path.dirname(os.path.abspath(__file__)) + SEP + "settings.json"
    # Load json from file 
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + "Please, allow it to run it.")
            

def __get_root_project(number_of_descent): 
    __file = __file__ 
    for _ in range(number_of_descent):
        __file = os.path.dirname(__file)
        sys.path.append(__file)
    sys.path = list(set(sys.path))

if __name__ == "__main__":
    #if args['x'] == 'Nacho':
    main()
    #else:
        #print('No has introducido la contraseña correcta')
