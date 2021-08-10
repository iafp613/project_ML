import matplotlib.pyplot as plt
import os

def guardar_grafico(name):
    SEP = os.sep
    ruta = os.path.dirname(os.getcwd()) + SEP + 'resources' + SEP + 'graphics' + SEP
    plt.savefig(ruta + name)