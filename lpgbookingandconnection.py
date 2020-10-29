# -*- coding: utf-8 -*-



from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox as ms
import sqlite3


Item4 = 0


# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()

#main Class
class user:
    def __init__(self,master):
    	# Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = "Welcome to NEW LPG Connection and Booking System, " + self.username.get()
            self.head.configure(fg="green", bg="black")
            self.head.pack(fill=X)
            application = travel(root)
            
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Already Taken!')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10,bg="light yellow")
        self.head.pack(fill=X)
        self.logf = Frame(self.master,padx =10,pady = 10,bg="light yellow")
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5,bg="light yellow").grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5,bg="light yellow").grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,bg="dark green",command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,bg="sky blue",command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10,bg="light yellow")
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5,bg="light yellow").grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5,bg="light yellow").grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,bg="light green",command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,bg="dark green",command=self.log).grid(row=2,column=1)

class travel:

    def __init__(self,root):
        self.root = root
        self.root.title("New LPG Connection and Booking System")
        self.root.geometry(geometry) 
        self.root.configure(bg='black')

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime(" %d / %m / %Y "))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        timeType=IntVar()
        cynType=IntVar()
        
        varl1=StringVar()
        varl2=StringVar()
        varl3=StringVar()
        reset_counter=0


        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Pincode=StringVar()
        Mobile=StringVar()
        Telephone=StringVar()
        Email=StringVar()

        MainCost=StringVar()
        Km=StringVar()
        Seq_Money=StringVar()
        Luggage=StringVar()
        Receipt=StringVar()


        Domestic=StringVar()
        Commertial=StringVar()
        Pipeline=StringVar()


        MainCost.set("0")
        Km.set("0")
        Seq_Money.set("0")
        Luggage.set("0")


        Domestic.set("0")
        Commertial.set("0")
        Pipeline.set("0")

       
        

    
    #==========================================Define Functiom==================================================

        def iExit():
            iExit= ms.askyesno("Prompt!","Do you want to exit?")
            if iExit > 0:
                root.destroy()
                return
        
        def iBook():
            x=random.randint(100001,500005)
            randomRef = str(x)
            Receipt_Ref.set(randomRef)
            iExit= ms.askyesno("Book Your LPG","Your LPG has been booked! Please pay at the delivery venue with unique refrence no: "+ Receipt_Ref.get()+". Click 'Yes' to submit response!")
            if iExit > 0:
                root.destroy()
                return
        
        
        def Reset():
            MainCost.set("0")
            Km.set("0")
            Seq_Money.set("0")
            Luggage.set("0")

            Domestic.set("0")
            Commertial.set("0")
            Pipeline.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            Pincode.set("")
            Mobile.set("")
            Telephone.set("")
            Email.set("")

            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt1.delete("1.0",END)
            self.txtReceipt2.delete("1.0",END)
            
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            timeType.set(0)
            cynType.set(0)
            varl1.set("0")
            varl2.set("0")
            varl3.set("0")


            self.cboDelPlace.current(0)
            self.cboType.current(0)
            self.cboNoCyn.current(0)
            self.cboDis.current(0)

            self.txtMainCost.configure(state=DISABLED)
            self.txtKm.configure(state=DISABLED)
            self.txtSeq_Money.configure(state=DISABLED)
            self.txtLuggage.configure(state=DISABLED)
        
            self.txtDomestic.configure(state=DISABLED)
            self.txtCommertial.configure(state=DISABLED)
            self.txtPipeline.configure(state=DISABLED)
            self.reset_counter=1

        def Receiptt():
            if reset_counter is 0 and Firstname.get()!="" and Surname.get()!="" and Address.get()!="" and Pincode.get()!="" and Mobile.get()!="" and Telephone.get()!="" and Email.get()!="":
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                x=random.randint(10001,50001)
                randomRef = str(x)
                Receipt_Ref.set(randomRef)

                self.txtReceipt1.insert(END,"Receipt Ref:\n")
                self.txtReceipt2.insert(END, Receipt_Ref.get() + "\n")
                self.txtReceipt1.insert(END,'Date:\n')
                self.txtReceipt2.insert(END, DateofOrder.get() + "\n")
                self.txtReceipt1.insert(END,'Booking No:\n')
                self.txtReceipt2.insert(END, 'TR ' + Receipt_Ref.get() + " BW\n")
                self.txtReceipt1.insert(END,'Firstname:\n')
                self.txtReceipt2.insert(END, Firstname.get() + "\n")
                self.txtReceipt1.insert(END,'Surname:\n')
                self.txtReceipt2.insert(END, Surname.get() + "\n")
                self.txtReceipt1.insert(END,'Address:\n')
                self.txtReceipt2.insert(END, Address.get() + "\n")
                self.txtReceipt1.insert(END,'Pin Code:\n')
                self.txtReceipt2.insert(END, Pincode.get() + "\n")
                self.txtReceipt1.insert(END,'Telephone:\n')
                self.txtReceipt2.insert(END, Telephone.get() + "\n")
                self.txtReceipt1.insert(END,'Mobile:\n')
                self.txtReceipt2.insert(END, Mobile.get() + "\n")
                self.txtReceipt1.insert(END,'Email:\n')
                self.txtReceipt2.insert(END, Email.get() + "\n")
                self.txtReceipt1.insert(END,'From:\n')
                self.txtReceipt2.insert(END, varl1.get() + "\n")
                self.txtReceipt1.insert(END,'To:\n')
                self.txtReceipt2.insert(END, varl2.get() + "\n")
                self.txtReceipt1.insert(END,'No of cylinders:\n')
                self.txtReceipt2.insert(END, varl3.get() + "\n")
                self.txtReceipt1.insert(END,'Domestic:\n')
                self.txtReceipt2.insert(END, Domestic.get() + "\n")
                self.txtReceipt1.insert(END,'Commertial:\n')
                self.txtReceipt2.insert(END, Commertial.get() + "\n")
                self.txtReceipt1.insert(END,'Pipeline:\n')
                self.txtReceipt2.insert(END, Pipeline.get() + "\n")
                self.txtReceipt1.insert(END,'Paid:\n')
                self.txtReceipt2.insert(END, PaidTax.get() + "\n")
                self.txtReceipt1.insert(END,'SubTotal:\n')
                self.txtReceipt2.insert(END, str(SubTotal.get()) + "\n")
                self.txtReceipt1.insert(END,'Total Cost:\n')
                self.txtReceipt2.insert(END, str(TotalCost.get()))
                
            else:
                self.txtReceipt1.delete("1.0",END)
                self.txtReceipt2.delete("1.0",END)
                self.txtReceipt1.insert(END,"\nNo Input")
                

        def Main_Cost():
            global Item1
            if var1.get() == 1:
                self.txtMainCost.configure(state = NORMAL)
                Item1=float(500)
                MainCost.set("Rs " + str(Item1))
            elif var1.get() == 0:
                self.txtMainCost.configure(state=DISABLED)
                MainCost.set("0")
                Item1=0

        
        def Kilo():
            if var2.get() == 0:
                self.txtKm.configure(state=DISABLED)
                Km.set("0")
            elif var2.get() == 1 and varl1.get() != "" and varl2.get() != "":
                self.txtKm.configure(state=NORMAL)
                if varl1.get() == "Add_New":
                    switch ={"Nearest_LPG_GAS_STATION": 10,"Home_Address": 8,"Updated_Address":6,"Add_new": 0}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Nearest_LPG_GAS_STATION":
                    switch ={"Nearest_LPG_GAS_STATION": 0,"Home_Address": 2,"Updated_Address":5,"Add_new": 10}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Home_Address":
                    switch ={"Nearest_LPG_GAS_STATION": 2,"Home_Address": 0,"Updated_Address":3,"Add_new": 8}
                    Km.set(switch[varl2.get()])
                elif varl1.get() == "Updated_Address":
                    switch ={"Nearest_LPG_GAS_STATION": 5,"Home_Address": 3,"Updated_Address":0,"Add_new": 6}
                    Km.set(switch[varl2.get()])        

        
        def SeqMoney():
            global Item3
            if var3.get() == 1:
                self.txtSeq_Money.configure(state = NORMAL)
                Item3=float(1000)
                Seq_Money.set("Rs " + str(Item3))
            elif var3.get() == 0:
                self.txtSeq_Money.configure(state = DISABLED)
                Seq_Money.set("0")
                Item3=0
                

        
        def Lug():
            global Item4
            if (var4.get()==1):
                self.txtLuggage.configure(state = NORMAL)
                Item4=float(30)
                Luggage.set("Rs "+ str(Item4))
            elif var4.get()== 0:
                self.txtLuggage.configure(state = DISABLED)
                Luggage.set("0")
                Item4=0

        
        def selectCyn():
            global Item5
            if cynType.get() == 1:
                self.txtCommertial.configure(state = DISABLED)
                Commertial.set("0") 
                self.txtPipeline.configure(state = DISABLED)
                Pipeline.set("0")
                self.txtDomestic.configure(state = NORMAL)
                Item5 = float(800)
                Domestic.set("Rs "+ str(Item5))
            elif cynType.get() == 2:
                self.txtDomestic.configure(state =DISABLED)
                Domestic.set("0")
                self.txtPipeline.configure(state = DISABLED)
                Pipeline.set("0")
                self.txtCommertial.configure(state = NORMAL)
                Item5 = float(1500)
                Commertial.set("Rs "+ str(Item5))
            else:
                self.txtDomestic.configure(state =DISABLED)
                Domestic.set("0")
                self.txtCommertial.configure(state = DISABLED)
                Commertial.set("0")
                self.txtPipeline.configure(state = NORMAL)
                Item5 = float(1700)
                Pipeline.set("Rs/mth "+ str(Item5))
                
                       
        def Total_Paid():
            if ((var1.get() == 1 and var2.get() == 1 and var3.get() == 1 or var4.get() == 1) and cynType.get() != 0 and timeType.get() != 0 and (varl1.get() != "" and varl2.get() !="")):
                if timeType.get()==1:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))
                elif timeType.get()==2:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)*1.5+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))
                else:
                    Item2=Km.get()
                    Cost_of_fare = (Item1+(float(Item2)*Item5)*2+Item3+Item4)

                    Tax = "Rs " + str('%.2f'%((Cost_of_fare) *0.09))
                    ST = "Rs " + str('%.2f'%((Cost_of_fare)))
                    TT = "Rs " + str('%.2f'%(Cost_of_fare+((Cost_of_fare)*0.9)))

                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            else:
                w = ms.showwarning("Error !","Invalid Input\nPlease try again !!!")
                
                
                
        def profile():
            roo = Tk()
            roo.geometry("1700x550+0+0")
            roo.title("Profile")
            roo.configure(bg='pink')
            lblinfo = Label(roo, font=('forte', 15, 'bold'), text="Status:", bg="pink",fg="black", bd=5)
            lblinfo.grid(row=0, column=0)
            lblinfo = Label(roo, font=('aria', 15,'bold'), text="         ",bg="pink", fg="white", anchor=W)
            lblinfo.grid(row=0, column=2)
            lblinfo = Label(roo, font=('forte', 15, 'bold'), text="Details:",bg="pink", fg="black", anchor=W)
            lblinfo.grid(row=0, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Name",bg="pink", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Customer's Name",bg="pink", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="17-Digit LPG ID",bg="pink", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1-4682-2742-2732-8631",bg="pink", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="State", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=3, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Customer's location", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=3, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pincode", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=4, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="16xxx21", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=4, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Account Since:", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=5, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="2016", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=5, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Address:", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=6, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="H.no 24, DS colony, xyz street",bg="pink", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Contact No.:", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=7, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="1235227184", fg="steel blue",bg="pink", anchor=W)
            lblinfo.grid(row=7, column=3)
            
            x=random.randint(1001,5001)
            randomRef = str(x)
            Receipt_Ref.set(randomRef)
            
            lblinfo = Label(roo, font=('verdana', 15, 'bold'),bg="pink", text="Please Visit Your Nearest LPG Gas Station For Verification with Token ID:" + Receipt_Ref.get() , fg="red", anchor=W)
            lblinfo.grid(row=8, column=2)


            roo.mainloop()


            

   #================================================mainframe========================================================================

        MainFrame=Frame(self.root)
        MainFrame.pack(fill=BOTH,expand=True)
        
        Tops = Frame(MainFrame, bd=20, width=1350,relief=SUNKEN, bg="light yellow")
        Tops.pack(side=TOP,fill=BOTH)
      
        self.lblTitle=Label(Tops,font=('arial',50,'bold'),text="Book your LPG:", fg="red",bg="light yellow")
        self.lblTitle.grid()

    #================================================customerframedetail=============================================================
        CustomerDetailsFrame=LabelFrame(MainFrame, width=1350,height=500,bd=20, pady=5, relief=RIDGE,bg="light yellow")
        CustomerDetailsFrame.pack(side=BOTTOM,fill=BOTH,expand=True)

        FrameDetails=Frame(CustomerDetailsFrame, width=880,height=400,bd=10, relief=RIDGE,bg="light yellow")
        FrameDetails.pack(side=LEFT,fill=BOTH,expand=True)

        CustomerName=LabelFrame(FrameDetails, width=150,height=250,bd=10, font=('arial',12,'bold'),text="Customer's Details:", relief=RIDGE,bg="light yellow")
        CustomerName.grid(row=0,column=0)

        TravelFrame = LabelFrame(FrameDetails,bd=10, width=300,height=250, font=('arial',12,'bold'),text="Booking Details:", relief=RIDGE,bg="light yellow")
        TravelFrame.grid(row=0,column=1)

        Book_Frame=LabelFrame(FrameDetails,width=300,height=150,relief=FLAT,bg="light yellow")
        Book_Frame.grid(row=1,column=0)

        CostFrame = LabelFrame(FrameDetails,width=150,height=150,bd=5,relief=FLAT,bg="light yellow")
        CostFrame.grid(row=1,column=1)


    #===============================================recipt======================================================================
        Receipt_BottonFrame=LabelFrame(CustomerDetailsFrame,bd=10, width=450,height=400, relief=RIDGE,bg="black")
        Receipt_BottonFrame.pack(side=RIGHT,fill=BOTH,expand=True)

        ReceiptFrame=LabelFrame(Receipt_BottonFrame, width=350,height=300, font=('verdana',12,'bold'),text="Final Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_BottonFrame, width=350,height=100, relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)
        
        Button1Frame=LabelFrame(Receipt_BottonFrame, width=350, height=100, relief=RIDGE)
        Button1Frame.grid(rowspan= 5)
    #=========================================================CustomerName====================================================

        self.lblFirstname=Label(CustomerName,font=('arial',14,'bold'),text="First Name",bd=7,bg="light yellow")
        self.lblFirstname.grid(row=0,column=0,sticky=W)
        self.txtFirstname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Firstname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtFirstname.grid(row=0,column=1)


        self.lblSurname=Label(CustomerName,font=('arial',14,'bold'),text="Sirname",bd=7,bg="light yellow")
        self.lblSurname.grid(row=1,column=0,sticky=W)
        self.txtSurname=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Surname,bd=7,insertwidth=2,justify=RIGHT)
        self.txtSurname.grid(row=1,column=1,sticky=W)


        self.lblAddress=Label(CustomerName,font=('arial',14,'bold'),text="Address",bd=7,bg="light yellow")
        self.lblAddress.grid(row=2,column=0,sticky=W)
        self.txtAddress=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Address,bd=7,insertwidth=2,justify=RIGHT)
        self.txtAddress.grid(row=2,column=1)


        self.lblPincode=Label(CustomerName,font=('arial',14,'bold'),text="Pin Code",bd=7,bg="light yellow")
        self.lblPincode.grid(row=3,column=0,sticky=W)
        self.txtPintcode=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Pincode,bd=7,insertwidth=2,justify=RIGHT)
        self.txtPintcode.grid(row=3,column=1)


        self.lblTelephone=Label(CustomerName,font=('arial',14,'bold'),text="Telephone No.",bd=7,bg="light yellow")
        self.lblTelephone.grid(row=4,column=0,sticky=W)
        self.txtTelephone=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Telephone,bd=7,insertwidth=2,justify=RIGHT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(CustomerName,font=('arial',14,'bold'),text="Mobile No.",bd=7,bg="light yellow")
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Mobile,bd=7,insertwidth=2,justify=RIGHT)
        self.txtMobile.grid(row=5,column=1)
        
        self.lblEmail=Label(CustomerName,font=('arial',14,'bold'),text="Email ID:",bd=7,bg="light yellow")
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(CustomerName,font=('arial',14,'bold'),textvariable=Email,bd=7,insertwidth=2,justify=RIGHT)
        self.txtEmail.grid(row=6,column=1)

 
    #===============================================LPG Information==============================================================
        self.lblDelPlace=Label(TravelFrame,font=('arial',14,'bold'),text="Delivery Place",bd=7,bg="light yellow")
        self.lblDelPlace.grid(row=0,column=0,sticky=W)

        self.cboDelPlace =ttk.Combobox(TravelFrame, textvariable = varl1 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboDelPlace['value']=('','Nearest_LPG_Gas_Station','Home_Address','Updated_Address','Add_New')
        self.cboDelPlace.current(0)
        self.cboDelPlace.grid(row=0,column=1)


        self.lblType=Label(TravelFrame,font=('arial',14,'bold'),text="LPG Cylinder type",bd=7,bg="light yellow")
        self.lblType.grid(row=1,column=0,sticky=W)

        self.cboType =ttk.Combobox(TravelFrame, textvariable = varl2 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboType['value']=('','Domestic','Commercial', 'Pipeline')
        self.cboType.current(0)
        self.cboType.grid(row=1,column=1)
        

        self.lblNoCyn=Label(TravelFrame,font=('arial',14,'bold'),text="No. of Cylinder",bd=7,bg="light yellow")
        self.lblNoCyn.grid(row=2,column=0,sticky=W)

        self.cboNoCyn =ttk.Combobox(TravelFrame, textvariable = varl3 , state='readonly', font=('arial',20,'bold'), width=14)
        self.cboNoCyn['value']=('','1','2','5','10')
        self.cboNoCyn.current(1)
        self.cboNoCyn.grid(row=2,column=1)
        
    #===============================================Charging Information==============================================================

        self.chkMainCost=Checkbutton(TravelFrame,text=" Main Cost*",bg="light yellow",variable = var1, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Main_Cost).grid(row=4, column=0, sticky=W)
        self.txtMainCost=Label(TravelFrame,font=('arial',14,'bold'),textvariable=MainCost,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtMainCost.grid(row=4,column=1)


        self.chkKm=Checkbutton(TravelFrame,text="Delivery Charges (KMs)*",bg="light yellow",variable = var2, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Kilo).grid(row=5, column=0, sticky=W)
        self.txtKm=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Km,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN,highlightthickness=0)
        self.txtKm.grid(row=5,column=1)

        self.chkSeq_Money=Checkbutton(TravelFrame,text="Security Money *",bg="light yellow",variable = var3, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=SeqMoney).grid(row=6, column=0, sticky=W)
        self.txtSeq_Money=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Seq_Money,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtSeq_Money.grid(row=6,column=1)

      
        self.chkLuggage=Checkbutton(TravelFrame,text="Redeem Discount/ Luggage Amount",bg="light yellow",variable = var4, onvalue=1, offvalue=0,font=('arial',16,'bold'),command=Lug).grid(row=7, column=0, sticky=W)
        self.txtLuggage=Label(TravelFrame,font=('arial',14,'bold'),textvariable=Luggage,bd=6,width=18,bg="white",state= DISABLED,justify=RIGHT,relief=SUNKEN)
        self.txtLuggage.grid(row=7,column=1)
    
    #=================================payment information ===========================================================================
         
        self.lblPaidTax=Label(CostFrame,font=('arial',14,'bold'),text="Paid Tax\t\t",bd=7,bg="light yellow")
        self.lblPaidTax.grid(row=0,column=2,sticky=W)
        self.txtPaidTax = Label(CostFrame,font=('arial',14,'bold'),textvariable=PaidTax,bd=7, width=26, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtPaidTax.grid(row=0,column=3)
            

        
        self.lblSubTotal=Label(CostFrame,font=('arial',14,'bold'),text="Sub Total",bd=7,bg="light yellow")
        self.lblSubTotal.grid(row=1,column=2,sticky=W)
        self.txtSubTotal = Label(CostFrame,font=('arial',14,'bold'),textvariable=SubTotal,bd=7, width=26, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtSubTotal.grid(row=1,column=3)



        self.lblTotalCost=Label(CostFrame,font=('arial',14,'bold'),text="Total Cost",bd=7,bg="light yellow")
        self.lblTotalCost.grid(row=2,column=2,sticky=W)
        self.txtTotalCost = Label(CostFrame,font=('arial',14,'bold'),textvariable=TotalCost,bd=7, width=26, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtTotalCost.grid(row=2,column=3)

    #==========================================================Cylinder Select=======================================================================

        self.chkDomestic=Radiobutton(Book_Frame,text="Domestic  ",value=1,variable = cynType,font=('arial',14,'bold'),bg="light yellow",command=selectCyn).grid(row=0, column=0, sticky=W)
        self.txtDomestic = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=Domestic,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtDomestic.grid(row=0,column=1)
        

        self.chkCommertial=Radiobutton(Book_Frame,text="Commertial",value=2,variable = cynType,font=('arial',14,'bold'),bg="light yellow",command=selectCyn).grid(row=1, column=0, sticky=W)
        self.txtCommertial= Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable=Commertial,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtCommertial.grid(row=1,column=1)
             
       
        self.chkPipeline = Radiobutton(Book_Frame,text="Pipeline     ",value=3,variable = cynType,font=('arial',14,'bold'),bg="light yellow",command=selectCyn).grid(row=2, column=0)
        self.txtPipeline = Label(Book_Frame,font=('arial',14,'bold'),width =7,textvariable= Pipeline,bd=5, state= DISABLED, justify=RIGHT,bg="white",relief=SUNKEN)
        self.txtPipeline.grid(row=2,column=1)

        self.chkTDays =Radiobutton(Book_Frame,text="Time Period: 20 Days",bg="light yellow",value=1,variable = timeType,font=('arial',14,'bold')).grid(row=0, column=2, sticky=W)
        self.chkOMth =Radiobutton(Book_Frame,text="Time Period: 1 Month",bg="light yellow",value=2,variable = timeType,font=('arial',14,'bold')).grid(row=1, column=2, sticky=W)
        self.chkOFMths =Radiobutton(Book_Frame,text="Time Period: 1.5 Months",bg="light yellow",value=3,variable = timeType,font=('arial',14,'bold')).grid(row=2, column=2, sticky=W)
    
   
    #=======================================Recipt====================================================================================

        self.txtReceipt1 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt1.grid(row=0,column=0,columnspan=2)
        self.txtReceipt2 = Text(ReceiptFrame,width = 22, height = 21,font=('arial',10,'bold'),borderwidth=0)
        self.txtReceipt2.grid(row=0,column=2,columnspan=2)


    #======================================Button========================================================================================
        
        self.btnTotal = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 2,text='Total',command=Total_Paid).grid(row=0,column=0)
        self.btnReceipt = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 3,text='Receipt',command=Receiptt).grid(row=0,column=1)
        self.btnReset = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 2,text='Reset',command=Reset).grid(row=0,column=2)
        self.btnExit = Button(ButtonFrame,padx=18,bd=7,font=('arial',11,'bold'),width = 2,text='Exit', command=iExit).grid(row=0,column=3)
    
    #------------------------------------Button1--------------------------------------------------------------------------------------
        self.btnBook = Button(Button1Frame,padx=14,bd=5,font=('arial',12,'bold'),width = 20,bg="light yellow", fg ="red", text='BOOK YOUR LPG', command=iBook).grid()
        self.btnNew = Button(Button1Frame,padx=14,bd=5,font=('arial',12,'bold'),width = 20,bg="light yellow", fg ="red", text='NEW LPG CONNECTION', command=profile).grid()
        
    #====================================================================================================================================

        
if __name__=='__main__':
    root = Tk()

    #=========================================== Getting Screen Width ==================================================================
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry="%dx%d+%d+%d"%(w,h,0,0)
    
    root.geometry("500x300+320+200")
    root.title('Login Form')
    application = user(root)
    root.mainloop()
    
