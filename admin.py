from tkinter import *
from tkinter import ttk

class Reception:
    def __init__(self, root):
        self.root= root
        self.root.title("Employees Management System")
        self.root.geometry("1350x700+0+0")

        title= Label(self.root, text= "Welcome to The Employees Management System", bd= 10, relief= GROOVE, font= ("times new roman", 40, "bold"), bg= "#8a817c", fg= "#e0afa0")
        title.pack(side= TOP, fill= X)

    #=== Admin Frame ===#
        admin_frame= Frame(self.root, bd= 4, relief= RIDGE, bg= "#463f3a")
        admin_frame.place(x= 20, y= 90, width= 420, height= 560)

        admn_title= Label(admin_frame, text= "Manage Recipients", bg= "#463f3a", fg= "#f4f3ee", font= ("times new roman", 30, "bold"))
        admn_title.grid(row= 0, columnspan= 2, pady= 20)

        fname_lbl= Label(admin_frame, text= "First Name: ", bg= "#463f3a", fg= "#bcb8b1", font= ("times new roman", 13, "bold"))
        fname_lbl.grid(row= 1, column= 0,pady= 10, padx= 20, sticky= "w")

        fname_ntr= Entry(admin_frame, font= ("times new roman", 13, "bold"), bd= 5, relief= RAISED)
        fname_ntr.grid(row= 1, column= 1,pady= 10, padx= 20, sticky= "w")

        sname_lbl= Label(admin_frame, text= "Surname: ", bg= "#463f3a", fg= "#bcb8b1", font= ("times new roman", 13, "bold"))
        sname_lbl.grid(row= 2, column= 0,pady= 10, padx= 20, sticky= "w")

        sname_ntr= Entry(admin_frame, font= ("times new roman", 13, "bold"), bd= 5, relief= RAISED)
        sname_ntr.grid(row= 2, column= 1,pady= 10, padx= 20, sticky= "w")

        gender_lbl= Label(admin_frame, text= "Gender: ", bg= "#463f3a", fg= "#bcb8b1", font= ("times new roman", 13, "bold"))
        gender_lbl.grid(row= 3, column= 0,pady= 10, padx= 20, sticky= "w")

        gender_drpdwn= ttk.Combobox(admin_frame, font= ("times new roman", 13, "bold"), state= 'readonly', justify= CENTER)
        gender_drpdwn['values']= ("Female", "Male", "Other (optional)")
        gender_drpdwn.grid(row= 3, column= 1, padx= 20, pady= 10)

        email_lbl= Label(admin_frame, text= "Email Address: ", bg= "#463f3a", fg= "#bcb8b1", font= ("times new roman", 13, "bold"))
        email_lbl.grid(row= 4, column= 0,pady= 10, padx= 20, sticky= "w")

        email_ntr= Entry(admin_frame, font= ("times new roman", 13, "bold"), bd= 5, relief= RAISED)
        email_ntr.grid(row= 4, column= 1,pady= 10, padx= 20, sticky= "w")

        contctnum_lbl= Label(admin_frame, text= "Contact Number: ", bg= "#463f3a", fg= "#bcb8b1", font= ("times new roman", 13, "bold"))
        contctnum_lbl.grid(row= 5, column= 0,pady= 10, padx= 20, sticky= "w")

        contctnum_ntr= Entry(admin_frame, font= ("times new roman", 13, "bold"), bd= 5, relief= RAISED)
        contctnum_ntr.grid(row= 5, column= 1,pady= 10, padx= 20, sticky= "w")

        duty_lbl= Label(admin_frame, text= "Employee's Duty: ", bg= "#463f3a", fg= "#bcb8b1", font= ("times new roman", 13, "bold"))
        duty_lbl.grid(row= 6, column= 0,pady= 10, padx= 20, sticky= "w")

        duty_ntr= Entry(admin_frame, font= ("times new roman", 13, "bold"), bd= 5, relief= RAISED)
        duty_ntr.grid(row= 6, column= 1,pady= 10, padx= 20, sticky= "w")




    #=== Details Frame ===#
        details_frame= Frame(self.root, bd= 4, relief= RIDGE, bg= "#bcb8b1")
        details_frame.place(x= 450, y= 90, width= 825, height= 560)


root= Tk()
obj= Reception(root)
root.mainloop()