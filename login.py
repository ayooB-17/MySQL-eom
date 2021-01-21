from tkinter import *
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
        left_lbl= Label(self.root, bg="#08a3d2", bd= 0)
        left_lbl.place(x= 0, y= 0, relheight= 1, width= 600)

        right_lbl= Label(self.root, bg= "#031f3c", bd= 0)
        right_lbl.place(x= 600, y= 0, relheight= 1, relwidth= 1)

        #=== Frame ===#
        login_frame= Frame(self.root, bg= "white")
        login_frame.place(x= 250, y= 100, width= 800, height= 500)

        title= Label(login_frame, text= "SIGN IN HERE", font= ("times new roman", 30, "bold"), bg= "#edf2f4", fg= "#d90429").place(x= 250, y= 150)

        email= Label(login_frame, text= "E-Mail Address: ", font= ("times new roman", 18, "bold"), bg= "#edf2f4", fg= "#d90429").place(x= 250, y= 210)
        self.email_ntr= Entry(login_frame, font= ("times new roman", 15), bg= "#ef233c")
        self.email_ntr.place(x= 250, y= 240, width= 350, height= 35)

        paswrd_lbl= Label(login_frame, text= "Password: ", font= ("times new roman", 18, "bold"), bg= "#edf2f4", fg= "#2b2d42").place(x= 250, y= 280)
        self.paswrd_ntr= Entry(login_frame, font= ("times new roman", 15), bg= "#8d99ae")
        self.paswrd_ntr.place(x= 250, y= 310, width= 350, height= 35)

        rgstr_btn= Button(login_frame, cursor= "hand2", text= "Register A New Account?", font= ("times new roman", 12, "bold"), bg= "#edf2f4", fg= "#d90429").place(x= 250, y= 350)
        login_btn= Button(login_frame, text= "Sign In", command= self.login, font= ("times new roman",20, "bold"), bg= "#2b2d42", fg="#edf2f4").place(x= 250, y= 425)

        #=== Clock ===#
        self.clock_lbl= Label(self.root, text= "\nWebCode Clock", font= ("Book Antiqua", 25, "bold"), fg= "#edf2f4", bg= "#2b2d42")
        self.clock_lbl.place(x= 90, y= 120, height= 450, width= 350)

        self.working()

    def login(self):
        print(self.email_ntr.get(), self.paswrd_ntr.get())


    def clock_image(self,hr,min_,sec_):
        clock= Image.new("RGB", (400, 400), (8, 25, 35))
        draw= ImageDraw.Draw(clock)

        #=== Fro Clock Image ===#
        left= Image.open("images/c.png")
        left= left.resize((300, 300), Image.ANTIALIAS)
        clock.paste(left, (50, 50))

        #=== Formula To Rotate Anti-Clock ===#
        # angle_in_radians= angle_in_degrees * math.pi / 180
        # line_length= 100
        # center_x= 250
        # center_y= 250
        # end_x= center_x + line_length * math.cos(angle_in_radians)
        # end_y= center_y + line_length * mathh.sin(angle_in_radians)

        #=== Hour Line Image ===#
        origin= 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill= "red", width= 4)
        #=== Minute Line ===#
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill= "whitesmoke", width= 1)
        #=== Seconds Line Image ===#
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill= "gold", width= 3)
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


root= Tk()
obj= Login_window(root)
root.mainloop()