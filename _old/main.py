# main.py - Main class for Krypton Cipher Tool

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import cipherfunctions

class CipherModule:
    def __init__(self):
        self.infile = None
        self.outfile = None
        self.setcipher = None
        self.cipherlist = ['Caesar', 'Vigenere']
        self.plaintext = None
        self.ciphertext = None

    def loadPlainText(self, filename):
        self.infile = open(filename, 'rb')

class Interface:
    def __init__(self):
        self.windowx = 500
        self.windowy = 600
        self.windowgeometry = (str(self.windowx) + "x" + str(self.windowy))
        self.ciphermodule = CipherModule()
        self.gui = None
        # create main window, size, and title
        self.root = Tk()
        self.root.geometry(self.windowgeometry)
        self.root.title("Krypton Cipher Tool")

        # create main interface widgets
        self.createMainWidgets()

    def loadFile(self):
        filepath = filedialog.askopenfilename(initialdir="/", title="Load File", filetypes= [(".txt file","*.txt")])
        self.gui['infile_path'].insert(0,filepath)
        self.ciphermodule.infile = open(filepath, 'rb')
        self.ciphermodule.plaintext = self.ciphermodule.infile.read()

    def saveFile(self):
        filepath = filedialog.asksaveasfilename(initialdir="/", title="Save File", filetypes= [(".txt file","*.txt")] )
        self.gui['outfile_path'].insert(0, filepath)
        self.ciphermodule.outfile = open(filepath + ".txt", 'wb')

    def caesarcipher(self):
        check_decipher = self.gui['radio-value'].get()
        rotation = 0
        if check_decipher == 1:
            rotation = int(self.gui['notebook-frame1-rot-text'].get())
        elif check_decipher == 2:
            rotation = -(int(self.gui['notebook-frame1-rot-text'].get()))
        self.ciphermodule.ciphertext = cipherfunctions.caesarcipher(self.ciphermodule.plaintext, rotation)
        self.ciphermodule.outfile.write(self.ciphermodule.ciphertext)
        self.ciphermodule.outfile.close()


    def createMainWidgets(self):
        widgets = {}

        # create the main widgets (set filepath for plaintext, set filepath for ciphertext)
        widgets['infile_label'] = Label(self.root, text="Plaintext File: ")
        widgets['infile_label'].grid(row=0,column=0)
        widgets['infile_strvariable'] = StringVar()
        widgets['infile_path'] = Entry(self.root, width=50, textvariable = widgets['infile_strvariable'])
        widgets['infile_path'].grid(row=0,column=1)
        widgets['loadbutton'] = Button(self.root, text="Load File", command=self.loadFile)
        widgets['loadbutton'].grid(row=0,column=2)
        widgets['outfile_label'] = Label(self.root, text="Ciphertext Name:")
        widgets['outfile_label'].grid(row=1,column=0)
        widgets['outfile_strvariable'] = StringVar()
        widgets['outfile_path'] = Entry(self.root, width=50, textvariable = widgets['outfile_strvariable'])
        widgets['outfile_path'].grid(row=1,column=1)
        widgets['savebutton'] = Button(self.root, text="Save File", command=self.saveFile)
        widgets['savebutton'].grid(row=1,column=2)
        widgets['radio-value'] = IntVar()
        widgets['radio-value'].set(1)
        widgets['radio-cipher'] = Radiobutton(self.root, text="Cipher", variable=widgets['radio-value'], value=1)
        widgets['radio-cipher'].grid(row=2,column=0)
        widgets['radio-decipher'] = Radiobutton(self.root, text="Decipher", variable=widgets['radio-value'], value=2)
        widgets['radio-decipher'].grid(row=2,column=1)

        # create cipher frame widgets
        widgets['cipherframe'] = ttk.LabelFrame(self.root, text="Cipher")
        widgets['cipherframe'].grid(row=2, column=0)
        widgets['notebook'] = ttk.Notebook(self.root)
        widgets['notebook'].grid(row=3,column=0)
        widgets['notebook-frame1'] = ttk.Frame(widgets['notebook'])
        widgets['notebook-frame2'] = ttk.Frame(widgets['notebook'])
        widgets['notebook'].add(widgets['notebook-frame1'], text="Caesar")
        widgets['notebook'].add(widgets['notebook-frame2'], text="Vigenere")
        widgets['notebook-frame1-rot-label'] = Label(widgets['notebook-frame1'], text="ROT")
        widgets['notebook-frame1-rot-label'].grid(row=0,column=0)
        widgets['notebook-frame1-rot-text'] = StringVar()
        widgets['notebook-frame1-rot-optionlist'] = [x for x in range(0,92)]
        widgets['notebook-frame1-rot-text'].set(widgets['notebook-frame1-rot-optionlist'][0])
        widgets['notebook-frame1-rot'] = OptionMenu(widgets['notebook-frame1'], widgets['notebook-frame1-rot-text'], *widgets['notebook-frame1-rot-optionlist'])
        widgets['notebook-frame1-rot'].grid(row=0,column=1)
        widgets['notebook-frame1-cipherbutton'] = Button(widgets['notebook-frame1'], text="Cipher", command=self.caesarcipher)
        widgets['notebook-frame1-cipherbutton'].grid(row=1,column=0, columnspan=2, sticky=W+E)

        self.gui = widgets

x = Interface()
x.root.mainloop()
