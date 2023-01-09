import os
from delphivcl import *

class FileDifWnd(Form):

    def __init__(self, owner):
        self.OpenFileABt = None
        self.FileAEdt = None
        self.OpenFileBBt = None
        self.FileBEdt = None
        self.Panel1 = None
        self.GroupBox3 = None
        self.ShiftEdt = None
        self.GroupBox4 = None
        self.Label1 = None
        self.Label2 = None
        self.XEdt = None
        self.DXEdt = None
        self.SaveFileBt = None
        self.SaveWinBt = None
        self.Panel3 = None
        self.Channel = None
        self.EKin = None
        self.EBind = None
        self.MouseY = None
        self.Counts = None
        self.Intensity = None
        self.Edit2 = None
        self.Edit3 = None
        self.Edit4 = None
        self.Edit5 = None
        self.Edit6 = None
        self.Edit7 = None
        self.GroupBox1 = None
        self.Label5 = None
        self.Label6 = None
        self.Label7 = None
        self.ApplyABt = None
        self.BEiAEdt = None
        self.BEfAEdt = None
        self.nptsAEdt = None
        self.RestoreABt = None
        self.GroupBox2 = None
        self.Label8 = None
        self.Label9 = None
        self.Label10 = None
        self.ApplyBBt = None
        self.BEiBEdt = None
        self.BEfBEdt = None
        self.NPTSBEdt = None
        self.RestoreBBt = None
        self.SaveFileBBt = None
        self.Panel4 = None
        self.FileACheck = None
        self.FileDifCheck = None
        self.FileBCheck = None
        self.GroupBox5 = None
        self.FileAScBt = None
        self.SubtrScBt = None
        self.MainMenu1 = None
        self.Exit1 = None
        self.Help1 = None
        self.OpenDialog1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "FileDif.pydfm"))

    def FormShow(self, Sender):
        print('ciao')
        pass

    def OpenFileABtClick(self, Sender):
        print('ciao')
        pass

    def OpenFileBBtClick(self, Sender):
        print('ciao')
        pass

    def ShiftEdtExit(self, Sender):
        print('ciao')
        pass

    def ShiftEdtKeyPress(self, Sender, Key):
        print('ciao')
        pass

    def XEdtExit(self, Sender):
        pass

    def XEdtKeyPress(self, Sender, Key):
        pass

    def DXEdtExit(self, Sender):
        pass

    def DXEdtKeyPress(self, Sender, Key):
        pass

    def SaveFileBtClick(self, Sender):
        pass

    def SaveWinBtClick(self, Sender):
        pass

    def ApplyABtClick(self, Sender):
        pass

    def RestoreABtClick(self, Sender):
        pass

    def ApplyBBtClick(self, Sender):
        pass

    def RestoreBBtClick(self, Sender):
        pass

    def SaveFileBBtClick(self, Sender):
        pass

    def FileACheckClick(self, Sender):
        pass

    def FileDifCheckClick(self, Sender):
        pass

    def FileBCheckClick(self, Sender):
        pass

    def FileAScBtClick(self, Sender):
        pass

    def SubtrScBtClick(self, Sender):
        pass

    def Exit1Click(self, Sender):
        pass