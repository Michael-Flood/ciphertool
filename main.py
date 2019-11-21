import tkinter
from tkinter import filedialog
from tkinter import ttk
import os
import monoalphabetic
import polyalphabetic

class Interface:
    def __init__(self):
        self.gui = {}
        self.root = tkinter.Tk()
        self.root.title("Krypton Cipher Tool")
        self.mainframe = tkinter.Frame(self.root)
        self.mainframe.grid(row=0,column=0)
        # program variables
        self.infilepath = None # location for the imported .txt file
        self.infiletext = None
        self.infilepreview = None
        self.outfile = None # location for the output .txt file

        self.makeStartGUI()

    def loadFile(self):
        """
        Open the file loading dialog. After the user selects a .txt file, the file is opened in self.infile and the window widgets
        are replaced by the main GUI.
        """
        currentpath = os.getcwd()
        self.infilepath = filedialog.askopenfilename(initialdir = currentpath,title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        temptext = None
        with open(self.infilepath, encoding='utf-8') as f:
            self.infiletext = f.readlines()
        for line in range(0,len(self.infiletext)):
            self.infiletext[line] = self.infiletext[line].replace('\n','')
        if len(self.infiletext[0]) > 50:
            self.infilepreview = self.infiletext[0][0:50]
        else:
            self.infilepreview = self.infiletext[0]

        self.makeMainGUI()

    def quit(self):
        """
        Function to terminate the application
        """
        self.root.destroy()

    def displayMonoPreview(self):
        """
        Performs cipher/decipher on file line of text from infile, displays to Preview window
        """
        rotation_num = int(self.gui['notebook-frame1-rotation-var'].get())
        if (rotation_num > 95) or (rotation_num < 0):
            print("Rotation values must be between 0 and 95")
            return 0
        radio_value = self.gui['radio-variable'].get()
        if radio_value == 'cipher':
            pass
        elif radio_value == 'decipher': # if the 'decipher' option is selected, negate the rotation number (work backwards)
            rotation_num = -(rotation_num)
        text_to_cipher = self.infilepreview
        text_ciphered = monoalphabetic.caesar(text_to_cipher, rotation_num)
        self.gui['notebook-frame1-preview-entry'].delete('1.0', tkinter.END)
        self.gui['notebook-frame1-preview-entry'].insert('1.0', text_ciphered)

    def generateMonoOutfile(self):
        """
        Outputs full cipher/decipher to .txt file and closes the program.
        Loops through each entry in the self.infiletext list, returning it appended with a '\n' newline character
        """
        text = self.infiletext # temporary variable for the list in self.infiletext
        ciphertext = [] # empty dictionary to hold ciphered lines (with newline characters added)
        rotation_num = int(self.gui['notebook-frame1-rotation-var'].get())
        if self.gui['radio-variable'].get() == 'cipher':
            pass
        elif self.gui['radio-variable'].get() == 'decipher':
            rotation_num = -(rotation_num)
        for line in self.infiletext:
            ciphered = monoalphabetic.caesar(line, rotation_num)
            ciphertext.append(ciphered + '\n')

        outfile_name = self.gui['notebook-frame1-outfile-name-var'].get() + ".txt"
        self.outfile = open(outfile_name, 'w')
        for line in ciphertext:
            self.outfile.write(line)
        self.outfile.close()
        self.quit()

    def displayPolyPreview(self):
        key = self.gui['notebook-frame2-key-var'].get()
        radio_value = self.gui['radio-variable'].get()
        text_to_cipher = self.infilepreview
        text_ciphered = polyalphabetic.polycipher(text_to_cipher, key, radio_value)
        self.gui['notebook-frame2-preview-entry'].delete('1.0', tkinter.END)
        self.gui['notebook-frame2-preview-entry'].insert('1.0', text_ciphered)

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
        startGUI['credit'] = tkinter.Label(self.mainframe, text="Copyright (C) 2019 by \nMichael Flood Technical Services")
        startGUI['credit'].grid(row=3, column=0)
        self.gui = startGUI

    def makeMainGUI(self):
        """
        Function to clear self.gui, and replace it with new widgets
        """
        # remove StartGUI widgets
        self.gui['cancel-button'].grid_forget()
        self.gui['load-file-button'].grid_forget()
        self.gui['canvas'].grid_forget()
        self.gui['credit'].grid_forget()
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
        self.gui['infile-preview'].grid(row=1, column=1)
        self.gui['infile-preview'].insert(tkinter.END,self.infilepreview)

        self.gui['radio-frame-label'] = tkinter.Label(self.gui['frame'], text="Option: ")
        self.gui['radio-frame-label'].grid(row=2,column=0)
        self.gui['radio-frame'] = tkinter.Frame(self.gui['frame'])
        self.gui['radio-frame'].grid(row=2, column=1)
        self.gui['radio-variable'] = tkinter.StringVar()
        self.gui['radio-variable'].set('cipher')
        self.gui['radio-cipher'] = tkinter.Radiobutton(self.gui['radio-frame'], text='Cipher', variable=self.gui['radio-variable'], value='cipher')
        self.gui['radio-cipher'].grid(row=0, column=0, sticky=tkinter.W)
        self.gui['radio-decipher'] = tkinter.Radiobutton(self.gui['radio-frame'], text="Decipher", variable=self.gui['radio-variable'], value='decipher')
        self.gui['radio-decipher'].grid(row=0, column=1, sticky=tkinter.W)

        # make the cipher tool Frames

        self.gui['cipherframe'] = ttk.LabelFrame(self.root, text="Cipher Select")
        self.gui['cipherframe'].grid(row=3, column=0)
        self.gui['notebook'] = ttk.Notebook(self.gui['cipherframe'])
        self.gui['notebook'].grid(row=0,column=1)
        self.gui['notebook-frame1'] = ttk.Frame(self.gui['notebook'])
        self.gui['notebook-frame2'] = ttk.Frame(self.gui['notebook'])
        self.gui['notebook'].add(self.gui['notebook-frame1'], text="Monalphabetic")
        self.gui['notebook'].add(self.gui['notebook-frame2'], text="Polyalphabetic")
        # build the monoalphbaetic encipherment widgets in frame 1
        self.gui['notebook-frame1-rotation-label'] = tkinter.Label(self.gui['notebook-frame1'], text="Rotation (0-95)")
        self.gui['notebook-frame1-rotation-label'].grid(row=0, column=0)
        self.gui['notebook-frame1-rotation-var'] = tkinter.StringVar()
        self.gui['notebook-frame1-rotation-var'].set('0')
        self.gui['notebook-frame1-rotation-entry'] = tkinter.Entry(self.gui['notebook-frame1'], width=3, textvariable=self.gui['notebook-frame1-rotation-var'])
        self.gui['notebook-frame1-rotation-entry'].grid(row=0, column=1, sticky=tkinter.W)
        self.gui['notebook-frame1-preview-entry'] = tkinter.Text(self.gui['notebook-frame1'], width=30, height=3)
        self.gui['notebook-frame1-preview-entry'].grid(row=1,column=1)
        self.gui['notebook-frame1-preview-label'] = tkinter.Label(self.gui['notebook-frame1'], text="Preview")
        self.gui['notebook-frame1-preview-label'].grid(row=1, column=0)
        self.gui['notebook-frame1-preview-button'] = tkinter.Button(self.gui['notebook-frame1'], text='Display', width=30, command=self.displayMonoPreview)
        self.gui['notebook-frame1-preview-button'].grid(row=2, column=1)
        self.gui['notebook-frame1-name-outfile-label'] = tkinter.Label(self.gui['notebook-frame1'], text="Name Output .txt File")
        self.gui['notebook-frame1-name-outfile-label'].grid(row=3,column=0)
        self.gui['notebook-frame1-outfile-name-var'] = tkinter.StringVar()
        self.gui['notebook-frame1-outfile-name-var'].set('output')
        self.gui['notebook-frame1-name-outfile-entry'] = tkinter.Entry(self.gui['notebook-frame1'], width=30, textvariable=self.gui['notebook-frame1-outfile-name-var'])
        self.gui['notebook-frame1-name-outfile-entry'].grid(row=3, column=1)
        self.gui['notebook-frame1-outfile-button'] = tkinter.Button(self.gui['notebook-frame1'], text="Generate Outfile", width=30, command=self.generateMonoOutfile)
        self.gui['notebook-frame1-outfile-button'].grid(row=4, column=1)
        # build the polyalphabetic encipherment widgets in frame 2
        self.gui['notebook-frame2-key-label'] = tkinter.Label(self.gui['notebook-frame2'], text="Key:")
        self.gui['notebook-frame2-key-label'].grid(row=0, column=0)
        self.gui['notebook-frame2-key-var'] = tkinter.StringVar()
        self.gui['notebook-frame2-key-entry'] = tkinter.Entry(self.gui['notebook-frame2'], width=30, textvariable=self.gui['notebook-frame2-key-var'])
        self.gui['notebook-frame2-key-entry'].grid(row=0, column=1)
        self.gui['notebook-frame2-preview-label'] = tkinter.Label(self.gui['notebook-frame2'], text="Preview")
        self.gui['notebook-frame2-preview-label'].grid(row=1, column=0)
        self.gui['notebook-frame2-preview-entry'] = tkinter.Text(self.gui['notebook-frame2'], width=30, height=3)
        self.gui['notebook-frame2-preview-entry'].grid(row=1, column=1)
        self.gui['notebook-frame2-preview-button'] = tkinter.Button(self.gui['notebook-frame2'], text="Display", width=30, command=self.displayPolyPreview)
        self.gui['notebook-frame2-preview-button'].grid(row=2, column=1)
        self.gui['notebook-frame2-outfile-name-var'] = tkinter.StringVar()
        self.gui['notebook-frame2-outfile-name-var'].set('output')
        self.gui['notebook-frame2-name-outfile-entry'] = tkinter.Entry(self.gui['notebook-frame2'], width=30, textvariable=self.gui['notebook-frame2-outfile-name-var'])
        self.gui['notebook-frame2-name-outfile-entry'].grid(row=3, column=1)
        self.gui['notebook-frame2-outfile-button'] = tkinter.Button(self.gui['notebook-frame2'], text="Generate Outfile", width=30, command=self.generateMonoOutfile)


if __name__ == '__main__':
    app = Interface()
    app.root.mainloop()
