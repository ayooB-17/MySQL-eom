from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
import pymysql

class Login_window:
    def __init__(self, root):
        self.root= root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg= "#08a3d2")

        #=== Background Color ===#
        left_lbl= Label(self.root, bg="#52b788", bd= 0)
        left_lbl.place(x= 0, y= 0, relheight= 1, width= 600)

        right_lbl= Label(self.root, bg= "#2b2d42", bd= 0)
        right_lbl.place(x= 600, y= 0, relheight= 1, relwidth= 1)

        #=== Frame ===#
        login_frame= Frame(self.root, bg= "white")
        login_frame.place(x= 250, y= 100, width= 800, height= 500)

        title= Label(login_frame, text= "SIGN IN HERE", font= ("times new roman", 30, "bold"), bg= "#edf2f4", fg= "#2d6a4f").place(x= 250, y= 100)

        email= Label(login_frame, text= "E-Mail Address: ", font= ("times new roman", 18, "bold"), bg= "#edf2f4", fg= "#ef233c").place(x= 250, y= 160)
        self.email_ntr= Entry(login_frame, font= ("times new roman", 15), bg= "#b7e4c7")
        self.email_ntr.place(x= 250, y= 190, width= 350, height= 35)

        paswrd_lbl= Label(login_frame, text= "Password: ", font= ("times new roman", 18, "bold"), bg= "#edf2f4", fg= "#ef233c").place(x= 250, y= 230)
        self.paswrd_ntr= Entry(login_frame, font= ("times new roman", 15), bg= "#95d5b2")
        self.paswrd_ntr.place(x= 250, y= 260, width= 350, height= 35)

        rgstr_btn= Button(login_frame, cursor= "hand2", text= "Register A New Account?", command= self.register_window, font= ("times new roman", 12, "bold"), bg= "#edf2f4", fg= "#d90429").place(x= 250, y= 300)
        login_btn= Button(login_frame, text= "Sign In", command= self.login, font= ("times new roman",20, "bold"), bg= "#2b2d42", fg="#edf2f4").place(x= 250, y= 375)

        #=== Clock ===#
        self.clock_lbl= Label(self.root, text= "\nWebCode Clock", font= ("Book Antiqua", 25, "bold"), fg= "#edf2f4", bg= "#2b2d42")
        self.clock_lbl.place(x= 90, y= 125, height= 450, width= 350)

        self.working()

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.email_ntr.get()== "" or self.paswrd_ntr.get()=="":
            messagebox.showerror("You Can't Do That!", "Please fill in all fields.", parent= self.root)

        else:
            try:
                cnct= pymysql.connect(host="localhost",
                                        user= "lifechoices",
                                        password= "@Lifechoices1234",
                                        database= "lifechoicesonline")
                crsr= cnct.cursor()
                crsr.execute("select * from lifechoicesonline where email=%s and password=%s", (self.email_ntr.get(), self.paswrd_ntr.get()))
                row= crsr.fetchall()
                if row== None:
                    messagebox.showerror("You Gave Wrong Info.", "Invalid EMAIL ADDRESS &/or PASSWORD", parent= self.root)
                else:
                    messagebox.showerror("You Signed In.", "Welcome To Life Choces Academy", parent= self.root)
                    self.root.destroy()
                    import main_screen
                cnct.close()

            except Exception as es:
                messagebox.showerror("Error!", f"Error due to: {str(es)}", parent= self.root)


    def clock_image(self,hr,min_,sec_):
        clock= Image.new("RGB", (400, 400), (8, 25, 35))
        draw= ImageDraw.Draw(clock)

        #=== Fro Clock Image ===#
        left= Image.open("images/c.png")
        left= left.resize((300, 400), Image.ANTIALIAS)
        clock.paste(left, (50, 50))

        h= datetime.now().time().hour
        m= datetime.now().time().minute
        s= datetime.now().time().second

        hr= (h/12)*360
        min_= (m/60)*360
        sec_= (s/60)*360

        #=== Formula To Rotate Anti-Clock ===#
        # angle_in_radians= angle_in_degrees * math.pi / 180
        # line_length= 100
        # center_x= 250
        # center_y= 250
        # end_x= center_x + line_length * math.cos(angle_in_radians)
        # end_y= center_y + line_length * mathh.sin(angle_in_radians)

        #=== Hour Line Image ===#
        origin= 150, 150
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill= "red", width= 4)
        #=== Minute Line ===#
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill= "whitesmoke", width= 1)
        #=== Seconds Line Image ===#
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill= "lightgreen", width= 3)
        draw.ellipse((195, 195, 210, 210), fill= "#edf2f4")

    def working(self):
        h= datetime.now().time().hour
        m= datetime.now().time().minute
        s= datetime.now().time().second

        hr= (h/12)*360
        min_= (m/60)*360
        sec_= (s/60)*360

        self.clock_image(hr, min_, sec_)
        self.img= ImageTk.PhotoImage(file= "images/c.png")
        self.clock_lbl.config(image= self.img)
        self.clock_lbl.after(200, self.working)
    
    def fogot_password(self):
        if self.email_ntr.get()== "":
            messagebox.showerror("Error!", "Please Enter an EMAIL ADDRESS to Reset Password.", parent= self.root)
        else:
            try:
                cnct= pymysql.connect(host="localhost",
                                        user= "lifechoices",
                                        password= "@Lifechoices1234",
                                        database= "lifechoicesonline")
                crsr= cnct.cursor()
                crsr.execute("select * from lifechoicesonline where email=%s", self.email_ntr.get())
                row= crsr.fetchone()
                if row== None:
                    messagebox.showerror("Error!", "Please Enter The Correct EMAIL ADDRESS to Reset Password.", parent= self.root)
                else:
                    cnct.close()
                    self.root2= Toplevel()
                    self.root2.title("Forgot Your Password?")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg= "#b7e4c7")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    fgtpaswrd_lbl= Label(self.root, text= "Forgot Your Password?", font= ("times new roman", 20, "bold"), bg= "#2b2d42", fg= "#b7e4c7").place(x= 350, y= 300)

                    #=== Forgot Password Window ===#
                    qustn_lbl= Label(self.root2, text= "Security Question", font= ("times new roman", 15, "bold"))

                    self.scritqustn_drpdwn= ttk.Combobox(self.root2, font= ("times new roman", 13), state= 'readonly', justify= center)
                    self.scritqustn_drpdwn['values']= ("Select---", "Your Mother's Name", "Your Home Town", "Your Best Friend")
                    self.scritqustn_drpdwn.place(x= 50, y= 130, width= 250)
                    self.scritqustn_drpdwn.current(0)

                    ans_lbl= Label(self.root2, text= "Answer", font= ("times new roman", 15, "bold"), bg= "#b7e4c7", fg= "#2b2d42")
                    self.ans_ntr= Entry(self.root2, font= ("times new roman", 15), bg= "#d8f3dc")
                    self.ans_ntr.place(x=50, y= 210, width= 250)

                    newpaswrd_lbl= Label(self.root2, text= "Enter NEW PASSWORD", font= ("times new roman", 15, "bold"), )
                    self.newpaswrd_ntr= Entry(self.root2, font= ("times new roman", 15), bg= "#d8f3dc")
                    self.newpaswrd_ntr.place(x= 50, y= 290, width= 250)

                    chngpaswrd_btn= Button(self.root2, text= "Reset Your Password", bg= "#8d99ae", fg= "#d90429", font= ("times new roman", 18, "bold"))     

            except Exception as es:
                messagebox.showerror("Error!", f"Error due to: {str(es)}", parent= self.root)


root= Tk()
obj= Login_window(root)
root.mainloop()