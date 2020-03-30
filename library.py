from tkinter import*
from tkinter import ttk
import random 
from datetime import datetime
import tkinter.messagebox

class Library:


    def__init__(self,root):
        self.root = root
        self.root.title("Rutto's Library Mangaement System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='Purple')





    if __name__ =='__main__':
        root = Tk()
        application = Library(root)
        root.mainloop()