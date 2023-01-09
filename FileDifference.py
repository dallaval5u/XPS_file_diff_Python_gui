from delphivcl import *
from FileDif import FileDifWnd

def main():
    Application.Initialize()
    Application.Title = 'Python_file_dif'
    MainForm = FileDifWnd(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()

if __name__ == '__main__':
    main()
