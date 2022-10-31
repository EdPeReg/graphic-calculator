import numpy as np
import matplotlib.pyplot as plt

from Grapher import Grapher

if __name__ == '__main__':
    plotter = Grapher(plt)
    print("Que function desea probar?")
    print("1. lineal")
    print("2. cuadratica")
    option = int(input('--> '))

    if option == 1:
        print("Ingrese la funcion lineal de la forma f(x)=mx+b: ")
        linear = input("")
    else:
        pass

    plotter.plot()


