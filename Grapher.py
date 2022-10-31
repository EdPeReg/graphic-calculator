import numpy as np

class Grapher:
    def __init__(self, plt):
        self.plt = plt
        self.setup()

    def setup(self):
        self.plt.ylabel('y')
        self.plt.xlabel('x')
        self.plt.axis([-10,10,-10,10])

    def plot(self, function_type='lineal'):
        # self.plt.plot(self.x, self.y, 'r-')
        # self.plt.show()
        pass