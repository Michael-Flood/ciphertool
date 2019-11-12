import tkinter
from tkinter import filedialog
import os
import PIL

class Interface:
    def __init__(self):
        self.gui = {}
        self.root = tkinter.Tk()
        self.mainframe = tkinter.Frame(self.root)
        self.mainframe.grid(row=0,column=0)

        # program variables
        self.infile = None # location for the imported .txt file
        self.infilepath = None
        self.infilepreview = None
        self.outfile = None # location for the output .txt file



        self.makeStartGUI()

    def loadFile(self):
        """
        Open the file loading dialog. After the user selects a .txt file, the file is opened in self.infile and the window widgets
        are replaced by the main GUI.
        """
        print("loadFile")
        currentpath = os.getcwd()
        fpath = filedialog.askopenfilename(initialdir = currentpath,title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        self.infile = open(fpath, 'rb')
        self.infilepath = fpath
        self.infilepreview = self.infile.readline()
        self.makeMainGUI()

    def quit(self):
        """
        Function to terminate the application
        """
        self.root.destroy()

    def makeStartGUI(self):
        """
        Function to build the initial file loading dialogue for the program.
        """
        startGUI = {}
        startGUI['canvas'] = tkinter.Canvas(self.mainframe, width=300, height=300)
        startGUI['canvas'].grid(row=0,column=0)
        startGUI['logo'] = tkinter.PhotoImage(file="key.gif")
        startGUI['canvas'].create_image(150, 150, image=startGUI['logo'])
        startGUI['load-file-button'] = tkinter.Button(self.mainframe, text='Load', command=self.loadFile, width=20)
        startGUI['load-file-button'].grid(row=1,column=0)
        startGUI['cancel-button'] = tkinter.Button(self.mainframe, text="Quit", command=self.quit, width=20)
        startGUI['cancel-button'].grid(row=2,column=0)
        self.gui = startGUI

    def makeMainGUI(self):
        """
        Function to clear self.gui, and replace it with new widgets
        """
        # remove StartGUI widgets
        self.gui['cancel-button'].grid_forget()
        self.gui['load-file-button'].grid_forget()
        self.gui['canvas'].grid_forget()
        del(self.gui['logo'])
        # build MaiNGUI widgets
        self.gui['frame'] = tkinter.Frame(self.mainframe, width=100)
        self.gui['frame'].grid(row=0, column=0)
        self.gui['mainframe-infile-label'] = tkinter.Label(self.gui['frame'], text="File: ")
        self.gui['mainframe-infile-label'].grid(row=0, column=0, sticky=tkinter.W)
        self.gui['mainframe-infile-name'] = tkinter.Label(self.gui['frame'], text=self.infilepath)
        self.gui['mainframe-infile-name'].grid(row=0, column=1)
        self.gui['mainframe-preview-label'] = tkinter.Label(self.gui['frame'], text="Preview: ")
        self.gui['mainframe-preview-label'].grid(row=1, column=0, sticky=tkinter.W)
        self.gui['infile-preview'] = tkinter.Text(self.gui['frame'], width=30, height=3)
        self.gui['infile-preview'].grid(row=1, column=1, sticky=tkinter.W)
        self.gui['infile-preview'].insert(tkinter.END,self.infilepreview)

        self.gui['radio-frame-label'] = tkinter.Label(self.gui['frame'], text="Option: ")
        self.gui['radio-frame-label'].grid(row=2,column=0)
        self.gui['radio-frame'] = tkinter.Frame(self.gui['frame'])
        self.gui['radio-frame'].grid(row=2, column=1, sticky=tkinter.W)
        self.gui['radio-variable'] = tkinter.StringVar()
        self.gui['radio-variable'].set('cipher')
        self.gui['radio-cipher'] = tkinter.Radiobutton(self.gui['radio-frame'], text='Cipher', variable=self.gui['radio-variable'], value='cipher')
        self.gui['radio-cipher'].grid(row=0, column=0, sticky=tkinter.W)
        self.gui['radio-decipher'] = tkinter.Radiobutton(self.gui['radio-frame'], text="Decipher", variable=self.gui['radio-variable'], value='decipher')
        self.gui['radio-decipher'].grid(row=0, column=1, sticky=tkinter.W)


if __name__ == '__main__':
    app = Interface()
    app.root.mainloop()
