import os
from delphivcl import *

class Grafik(Form):

    def __init__(self, owner):
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "graph.pydfm"))

    def MouseClicked(self, Sender):
        pass

    def Init1(self, Sender):
        pass

    def MoveMouse(self, Sender, Shift, X, Y):
        pass

    def FormPaint(self, Sender):
        pass