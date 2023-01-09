import os
from delphivcl import *

class SaveFileWindow(Form):

    def __init__(self, owner):
        self.GroupBox1 = None
        self.Label1 = None
        self.Label2 = None
        self.BEIEdt = None
        self.BEFEdt = None
        self.SaveBt = None
        self.Button1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "SaveFileWindowUnit.pydfm"))

    def FormCreate(self, Sender):
        pass

    def FormShow(self, Sender):
        pass

    def SaveBtClick(self, Sender):
        pass

    def Button1Click(self, Sender):
        pass