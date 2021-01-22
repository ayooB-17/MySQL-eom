from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Register:
    def __init__(self, root):
        self.root= root
        self.root.title("Registration Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="whitesmoke")
        
        #=== Background Image ===#
        self.bg= ImageTk.PhotoImage(file= "images/bg2.png")
        bg= Label(self.root, image= self.bg).place(x= 0, y= 0, relwidth= 1, relheight= 1)

        #=== Left Image ===#
        self.left= ImageTk.PhotoImage(file= "images/side.jpeg")
        left= Label(self.root, image= self.left).place(x= 80, y= 100, width= 400, height= 500)

        #=== Registre Frame ===#
        frame1= Frame(self.root, bg= "#8d99ae")
        frame1.place(x= 480, y= 100, width= 700, height= 500)

        title= Label(frame1, text= "REGISTER HERE", font= ("times new roman",20,"bold"), bg= "#8d99ae", fg= "#40916c").place(x= 50, y= 30)

        Fname_lbl= Label(frame1, text= "First Name: ", font= ("times new roman",15,"bold"), bg= "#8d99ae", fg= "#40916c").place(x= 50, y= 100)
        Fname_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 50, y= 125, width= 250)

        Sname_lbl= Label(frame1, text= "Surname: ", font= ("times new roman",15,"bold"), bg= "#8d99ae", fg= "#40916c").place(x= 370, y= 100)
        Sname_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 370, y= 125, width= 250)

        #--- Contact Details ---#
        contctdtls_lbl= Label(frame1, text= "Contact Number: ", font= ("times new roman",15,"bold"), bg= "#8d99ae", fg= "#40916c").place(x= 50, y= 170)
        contctdtls_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 50, y= 195, width= 250)

        email_lbl= Label(frame1, text= "E-mail Address: ", font= ("times new roman",15,"bold"), bg= "#8d99ae", fg= "#40916c").place(x= 370, y= 170)
        email_ntr= Entry(frame1, font= ("times new roman",15),).place(x= 370, y= 195, width= 250)

        #--- Security Details ---#
        scritqustn_lbl= Label(frame1, text= "Securty Question: ", font= ("times new roman",15,"bold"), bg= "#8d99ae", fg= "#40916c").place(x= 50, y= 240)

        scritqustn_drpdwn= ttk.Combobox(frame1, font= ("times new roman",12), state= 'readonly', justify= CENTER)
        scritqustn_drpdwn['values']= ("Select---", )
        scritqustn_drpdwn.place(x= 50, y= 265, width= 250)
        scritqustn_drpdwn.current(0)

        ans_lbl= Label(frame1, text= "Answer To Security Question: ", font= ("times new roman",15,"bold"), bg= "#8d99ae", fg= "#40916c").place(x= 370, y= 240)
        ans_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 370, y= 265, width= 250)

        #--- Password ---#
        paswrd_lbl= Label(frame1, text= "Password: ", font= ("times new roman",15,"bold"), bg= "#8d99ae", fg= "#40916c").place(x= 50, y= 310)
        paswrd_ntr= Entry(frame1, font= ("times new roman",15), bg= "#b7e4c7").place(x= 50, y= 335, width= 250)

        confrmpaswrd_lbl= Label(frame1, text= "Confirm Password: ", font= ("times new roman",15,"bold"), bg= "#8d99ae", fg= "#d8f3dc").place(x= 370, y= 310)
        confrmpaswrd_ntr= Entry(frame1, font= ("times new roman",15), bg= "#40916c").place(x= 370, y= 335, width= 250)

        #--- Agree to T's & C's ---#
        self.var_chk=IntVar()
        check= Checkbutton(frame1, text= "I Agree To Terms & Conditions", onvalue= 1, offvalue= 0, bg= "#8d99ae", fg= "#2d6a4f", font= ("times new roman", 12)).place(x= 50, y= 370)

        #--- Register Button ---#
        self.rgstrbtn_img= ImageTk.PhotoImage(file= "images/register.png")
        rgstrbtn= Button(frame1, image= self.rgstrbtn_img, bd= 0, cursor= "hand2", bg= "#8d99ae", command= self.register_data).place(x= 50, y= 430)
        loginbtn= Button(self.root, text= "Sign In", font= ("times new roman", 20), bd= 0, cursor= "hand2", bg= "#b7e4c7", command= self.login_window).place(x= 200, y= 470, width= 160)
    
    def login_window(self):
        self.root.destroy()
        import login

    def clear(self):
        self.Fname_ntr.delete(0, END)
        self.Sname_ntr.delete(0, END)
        self.contctdtls_ntr.delete(0, END)
        self.email_ntr.delete(0, END)
        self.ans_ntr.delete(0, END)
        self.paswrd_ntr.delete(0, END)
        self.confrmpaswrd_ntr.delete(0, END)
        self.scritqustn_drpdwn.delete(0)

    #def register_user():
    #    userid = Username_id.get()
    #    fname = fullname.get()
    #    sname = surname.get()
    #    datejoine = Date_joined.get()
    #    gender = Gender.get()
    #    usercat = Category.get()
    #    user_name = username.get()
    #    pass_word = Password.get()
    #    try:
    #        sql = "INSERT INTO USERS VALUES (%s,%s,%s,%s,%s,%s,%s,%s )"
    #        mycursor.execute(sql, [userid, fname, sname, datejoine, gender, usercat, user_name, pass_word])
    #        result = mycursor.fetchone()
    #        mydb.commit()
    #        messagebox.showinfo("INSERTION", "Record Inserted")
    #    except:
    #        messagebox.showinfo("INSERTION", "Record Insertion failed")

    def register_data(self):
        if self.Fname_ntr.get()=="" or self.Sname_ntr.get()=="" or self.contctdtls_ntr.get()=="" or self.email_ntr.get()=="" or self.ans_ntr.get()=="" or self.paswrd_ntr.get()=="" or self.confrmpaswrd_ntr.get()=="" or self.scritqustn_drpdwn.get()==0:
            messagebox.showerror("Error!", "All Fields Are Required.", parent= self.root)
        elif self.paswrd_ntr.get()!= self.confrmpaswrd_ntr.get():
            messagebox.showerror("Error!", "CONFIRM PASSWORD Should Match PASSWORD.", parent= self.root)
        elif self.var_chk.get()== 0:
            messagebox.showerror("Error!", "Agree To Terms & Conditions.", parent= self.root)
        else:
            cnct= pymysql.connect(host="localhost",
                                        user= "lifechoices",
                                        password= "",
                                        database= "lifechoicesonline")
            crsr=cnct.cursor()
            crsr.execute("select * from users where email=%s", self.email_ntr.get())
            row=cur.fetchone()
            # print(row)

            if row!= None:
                messagebox.showerror("Error!", "User Email Already Exists, Try Another EMAIL ADDRESS.")
            else:
                crsr.execute("insert into users (fname, sname, contctdtls, email, ans, confrmpaswrd)",
                                (self.Fname_ntr.get(),
                                 self.Sname_ntr.get(),
                                 self.contctdtls_ntr.get(),
                                 self.email.get(),
                                 self.ans_ntr.get(),
                                 self.confrmpaswrd.get()))
        

        


root= Tk()
obj= Register(root)
root.mainloop()