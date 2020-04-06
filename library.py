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
        self.root.configure(background='Blue')

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


        self.lblBookTitle=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Book Title:', padx=2, pady=2)
        self.lblBookTitle .grid(row=1, column=2, sticky=W)
        self.txtBookTitle = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtBookTitle.grid(row=1, column=3)


        self.lblRef=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Reference NO:', padx=2, pady=2)
        self.lblRef .grid(row=1, column=0, sticky=W)
        self.txtRef= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtRef .grid(row=1, column=1)


       	self.lblTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Title:", padx=2, pady=2)
       	self.lblTitle .grid(row=2, column=0, sticky=W)

       	self.cboTitle=ttk.Combobox(DataFrameLEFT, state='readonly', font=('arial', 12, 'bold'), width=23)
       	self.cboTitle['value']=('', 'Miss.', 'Mr.', 'Mrs.', 'Dr.', 'Capt.', 'Ms.')
       	self.cboTitle.current(0)
       	self.cboTitle.grid(row=2, column=1)

        self.lblAuthor=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Author:', padx=2, pady=2)
        self.lblAuthor .grid(row=2, column=2, sticky=W)
        self.txtAuthor= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtAuthor .grid(row=2, column=3)

        self.lblFirstname=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='First Name:', padx=2, pady=2)
        self.lblFirstname .grid(row=3, column=0, sticky=W)
        self.txtFirstname= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtFirstname .grid(row=3, column=1)

        self.lblDateBorrowed=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Date Borrowed:', padx=2, pady=2)
        self.lblDateBorrowed .grid(row=3, column=2, sticky=W)
        self.txtDateBorrowed= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtDateBorrowed .grid(row=3, column=3)

        self.lblSurname=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Surname:', padx=2, pady=2)
        self.lblSurname .grid(row=4, column=0, sticky=W)
        self.txtSurname= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtSurname .grid(row=4, column=1)

        self.lblDateDue=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Date Due:', padx=2, pady=6)
        self.lblDateDue .grid(row=4, column=2, sticky=W)
        self.txtDateDue= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtDateDue .grid(row=4, column=3)

        self.lblAddress1=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Address 1:', padx=2, pady=2)
        self.lblAddress1 .grid(row=5, column=0, sticky=W)
        self.txtAddress1= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtAddress1 .grid(row=5, column=1)

        self.lblDaysOnLoan=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Days On Loan:', padx=2, pady=2)
        self.lblDaysOnLoan .grid(row=5, column=2, sticky=W)
        self.txtDaysOnLoan= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtDaysOnLoan .grid(row=5, column=3)

        self.lblAddress2=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Address 2:', padx=2, pady=2)
        self.lblAddress2 .grid(row=6, column=0, sticky=W)
        self.txtAddress2= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtAddress2 .grid(row=6, column=1)

        self.lblLateReturnFine=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text=':Date Return Fine', padx=2, pady=2)
        self.lblLateReturnFine .grid(row=6, column=2, sticky=W)
        self.txtLateReturnFine= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtLateReturnFine .grid(row=6, column=3)

        self.lblPostCode=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Post Code:', padx=2, pady=2)
        self.lblPostCode .grid(row=7, column=0, sticky=W)
        self.txtPostCode= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtPostCode .grid(row=7, column=1)

        self.lblDateOverDue=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Date Over Due:', padx=2, pady=2)
        self.lblDateOverDue .grid(row=7, column=2, sticky=W)
        self.txtDateOverDue= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtDateOverDue .grid(row=7, column=3)

        self.lblMobileNo=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Mobile NO:', padx=2, pady=2)
        self.lblMobileNo .grid(row=8, column=0, sticky=W)
        self.txtMobileNO= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtMobileNO .grid(row=8, column=1)

        self.lblSellingPrice=Label(DataFrameLEFT, font=('arial', 12, 'bold',), text='Selling Price:', padx=2, pady=2)
        self.lblSellingPrice .grid(row=8, column=2, sticky=W)
        self.txtSellingPrice= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), width =25)
        self.txtSellingPrice .grid(row=8, column=3)
        #=============================================================Button=====================================================================
    	self.btnDisplayData=Button(ButtonFrame, text='DisplayData',font=('arial', 12, 'bold'), width=30, bd=4)
   		self.btnDisplayData.grid(row=0,column=0)





if __name__ =='__main__':
	root = Tk()
	application = Library(root)
	root.mainloop()