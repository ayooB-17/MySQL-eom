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
        bg= Label(self.root, image= self.bg).place(x= 250, y= 0, relwidth= 1, relheight= 1)

        #=== Left Image ===#
        self.left= ImageTk.PhotoImage(file= "images/side.jpeg")
        left= Label(self.root, image= self.left).place(x= 80, y= 100, width= 400, height= 500)

        #=== Registre Frame ===#
        frame1= Frame(self.root, bg= "white")
        frame1.place(x= 480, y= 100, width= 700, height= 500)

        title= Label(frame1, text= "REGISTER HERE", font= ("times new roman",20,"bold"), bg= "#fff", fg= "#0077b6").place(x= 50, y= 30)

        Fname_lbl= Label(frame1, text= "First Name: ", font= ("times new roman",15,"bold"), bg= "white", fg= "grey").place(x= 50, y= 100)
        Fname_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 50, y= 125, width= 250)

        Sname_lbl= Label(frame1, text= "Surname: ", font= ("times new roman",15,"bold"), bg= "white", fg= "grey").place(x= 370, y= 100)
        Sname_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 370, y= 125, width= 250)

        #--- Contact Details ---#
        contctdtls_lbl= Label(frame1, text= "Contact Number: ", font= ("times new roman",15,"bold"), bg= "white", fg= "grey").place(x= 50, y= 170)
        contctdtls_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 50, y= 195, width= 250)

        email_lbl= Label(frame1, text= "E-mail Address: ", font= ("times new roman",15,"bold"), bg= "white", fg= "grey").place(x= 370, y= 170)
        email_ntr= Entry(frame1, font= ("times new roman",15),).place(x= 370, y= 195, width= 250)

        #--- Security Details ---#
        scritqustn_lbl= Label(frame1, text= "Securty Question: ", font= ("times new roman",15,"bold"), bg= "white", fg= "grey").place(x= 50, y= 240)

        scritqustn_drpdwn= ttk.Combobox(frame1, font= ("times new roman",12), state= 'readonly', justify= CENTER)
        scritqustn_drpdwn['values']= ("Select", "Your Mother's Name", "Your Home Town", "Your Best Friend")
        scritqustn_drpdwn.place(x= 50, y= 265, width= 250)
        scritqustn_drpdwn.current(0)

        ans_lbl= Label(frame1, text= "Answer To Security Question: ", font= ("times new roman",15,"bold"), bg= "white", fg= "grey").place(x= 370, y= 240)
        ans_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 370, y= 265, width= 250)

        #--- Password ---#
        paswrd_lbl= Label(frame1, text= "Password: ", font= ("times new roman",15,"bold"), bg= "white", fg= "grey").place(x= 50, y= 310)
        paswrd_ntr= Entry(frame1, font= ("times new roman",15), bg= "lightgrey").place(x= 50, y= 335, width= 250)

        confrmpaswrd_lbl= Label(frame1, text= "Confirm Password: ", font= ("times new roman",15,"bold"), bg= "white", fg= "grey").place(x= 370, y= 310)
        confrmpaswrd_ntr= Entry(frame1, font= ("times new roman",15),).place(x= 370, y= 335, width= 250)

        #--- Agree to T's & C's ---#
        check= Checkbutton(frame1, text= "I Agree To Terms & Conditions", onvalue= 1, offvalue= 0, bg= "white", font= ("times new roman", 12)).place(x= 50, y= 370)

        #--- Register Button ---#
        self.rgstrbtn_img= ImageTk.PhotoImage(file= "images/register.png")
        rgstrbtn= Button(frame1, image= self.rgstrbtn_img, bd= 0, cursor= "hand2").place(x= 50, y= 430)
        loginbtn= Button(self.root, text= "Sign In", font= ("times new roman", 20), bd= 0, cursor= "hand2").place(x= 200, y= 470, width= 160)



root= Tk()
obj= Register(root)
root.mainloop()