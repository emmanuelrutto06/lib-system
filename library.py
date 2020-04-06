from tkinter import*
from tkinter import ttk
import random 
from datetime import datetime
import tkinter.messagebox

class Library:


    def __init__(self,root):
        self.root = root
        self.root.title("Rutto's Library Mangaement System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='Purple')

        #================================================FRAME==============================================================================================================

        MainFrame = Frame(self.root)
        MainFrame.grid()


       	TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame, width=39,font=('arial', 40,'bold'),text="\tLibrary Management System\t",padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd= 20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=('arial', 12, 'bold'), text="Library Membership Info:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE, font=('arial', 12,'bold'), text="Book Details:",)
        DataFrameRIGHT.pack(side=RIGHT)
        #===================================================WIDGET===========================================================================================================
        self.lblMemberType=Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Member Type:', padx=2, pady=2)
        self.lblMemberType .grid(row=0, column=0, sticky=W)

        self.cboMemberType=ttk.Combobox(DataFrameLEFT, font=('arial', 12, 'bold'),state='readonly', width=23)
        self.cboMemberType['value']=('', 'Student','Lecturer','Admin staff')
        self.cboMemberType.current(0)
        self.cboMemberType .grid(row=0, column=1)

        self.lblBookID=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Book ID:', padx=2, pady=2)
        self.lblBookID .grid(row=0, column=2, sticky=W)
        self.txtBookID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtBookID .grid(row=0, column=3)


        self.lblBookTitle=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Book ID:', padx=2, pady=2)
        self.lblBookTitle .grid(row=1, column=2, sticky=W)
        self.lblBookTitle = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.lblBookTitle.grid(row=1, column=3)


        self.lblRef=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Book ID:', padx=2, pady=2)
        self.lblRef .grid(row=1, column=0, sticky=W)
        self.txtRef= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtRef .grid(row=1, column=1)


       	self.lblTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2)
       	self.lblTitle .grid(row=2, column=0, sticky=W)

       	self.cboTitle=ttk.Combobox(DataFrameLEFT, state='readonly', font=('arial', 12, 'bold'), width=23)
       	self.cboTitle['value']=('', 'Miss.', 'Mr.', 'Mrs.', 'Dr.', 'Capt.', 'Ms.')
       	self.cboTitle.current(0)
       	self.cboTitle.grid(row=2, column=1)

        self.lblAuthor=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Book ID:', padx=2, pady=2)
        self.lblAuthor .grid(row=2, column=2, sticky=W)
        self.txtAuthor= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtAuthor .grid(row=2, column=3)

        self.lblFirstname=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Book ID:', padx=2, pady=2)
        self.lblFirstname .grid(row=3, column=0, sticky=W)
        self.txtFirstname= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtFirstname .grid(row=3, column=1)

        self.lblDateBorrowed=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Book ID:', padx=2, pady=2)
        self.lblDateBorrowed .grid(row=3, column=2, sticky=W)
        self.txtDateBorrowed= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtDateBorrowed .grid(row=3, column=3)


if __name__ =='__main__':
	root = Tk()
	application = Library(root)
	root.mainloop()