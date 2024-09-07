from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from pyrebase import *
import re


class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("800x700+50+50")
        firebaseConfig = {
        "apiKey": "AIzaSyDdkCDL4VEFTCKdD_P24A5ichL8U-zfD2E",
        "authDomain": "student-8ec27.firebaseapp.com",
        "databaseURL": "https://student-8ec27-default-rtdb.firebaseio.com/",
        "projectId": "student-8ec27",
        "storageBucket": "student-8ec27.appspot.com",
        "messagingSenderId": "827852263219",
        "appId": "1:827852263219:web:2896d18208ed510b103846",
        "measurementId": "G-QZG2Y66DEE"
    }

    # Initialize Firebase
        fb = initialize_app(firebaseConfig)
        db = fb.database()

        
        t = ("Century", 25, "bold", "italic")
        f = ("Arial", 15, "bold", "italic")
        v = ("Arial", 10, "bold")

        labtitle = Label(root, text=" Student Management System", font=t)
        labtitle.place(x=100, y=30)



        def update_data():
            ID = entID.get()
            name = entName.get()
            b_name = entSalary.get()

            if not ID:
                showerror("Issue", "You did not enter ID")
                entID.focus()
                return

            if not ID.isdigit():
                showerror("Issue", "ID should contain only digits")
                entID.delete(0, END)
                entID.focus()
                return

            if not name:
                showerror("Issue", "You did not enter name")
                entName.focus()
                return

            if not re.match("^[a-zA-Z ]+$", name):
                showerror("Issue", "Name should contain only alphabets")
                entName.delete(0, END)
                entName.focus()
                return

            if not b_name:
                showerror("Issue", "You did not enter branch name")
                entSalary.focus()
                return

            if not re.match("^[a-zA-Z ]+$", b_name):
                showerror("Issue", "Branch name should contain only alphabets")
                entSalary.delete(0, END)
                entSalary.focus()
                return

            # Retrieve the unique key (push ID) based on the entered student ID
            student_id = int(ID)
            student_records = db.child("fb").get().val()
            record_key = None

            if student_records:
                for key, value in student_records.items():
                    if value['ID'] == student_id:
                        record_key = key
                        break

            if not record_key:
                showerror("Error", "Student ID not found")
                return

            # Update the data using the retrieved key
            updated_info = {"ID": student_id, "name": name, "b_name": b_name}
            db.child("fb").child(record_key).update(updated_info)
            showinfo("Done", "Data Updated Successfully")

            entID.delete(0, END)
            entName.delete(0, END)
            entSalary.delete(0, END)
            entID.focus()
        def add():
            ID = entID.get()
            name = entName.get()
            b_name = entSalary.get()

            if not entID.get():
                showerror("Issue" , "You did not enter ID")
                entID.focus()
                return

            if not ID.isdigit():
                showerror("Issue" , "ID contain only digit")
                entID.delete(0 , END)
                entID.focus()
                return

            if not entName.get():
                showerror("Issue" , "You did not enter name")		
                entName.focus()
                return

            if name.isdigit():
                showerror("Issue" , "name is contain only alphabets")
                entName.delete(0 , END)
                entName.focus()
                return
            
            while True:
                if name != '' and all(chr.isalpha() or chr.isspace() for chr in name):
                    break
                else:
                    showerror("Issue" , " Name is contain only alphabets")
                    entName.delete(0 , END)
                    entName.focus()
                    return

            if name.isspace():
                showerror("Issue" , "name is contain only alphabets")
                entName.delete(0 , END)
                entName.focus()
                return

            if not entSalary.get():
                showerror("Issue" , "You did not enter branch name")		
                entSalary.focus()
                return

            if b_name.isdigit():
                showerror("Issue" , " Branch name is contain only alphabets")
                entSalary.delete(0 , END)
                entSalary.focus()
                return
            
            while True:
                if b_name != '' and all(chr.isalpha() or chr.isspace() for chr in b_name):
                    break
                else:
                    showerror("Issue" , "Branch Name is contain only alphabets")
                    entSalary.delete(0 , END)
                    entSalary.focus()
                    return

            if b_name.isspace():
                showerror("Issue" , "Branch name is contain only alphabets")
                entSalary.delete(0 , END)
                entSalary.focus()
                return




            ID = int(entID.get())
            

            info = { "ID":ID , "name" : name , "b_name" : b_name}
            db.child("fb").push(info)
            showinfo("Done","added")
            entID.delete(0 , END)
            entName.delete(0 , END)
            entSalary.delete(0 , END)
            entID.focus()




        labID = Label(root, text="Enter Student ID", font=f)
        labID.place(x=50, y=100)

        entID = Entry(root, font=f, width=20)
        entID.place(x=300, y=100)

        labName = Label(root, text="Enter Student Name", font=f)
        labName.place(x=50, y=200)

        entName = Entry(root, font=f, width=20)
        entName.place(x=300, y=200)

        labSalary = Label(root, text="Enter Branch Name", font=f)
        labSalary.place(x=50, y=300)

        entSalary = Entry(root, font=f, width=20)
        entSalary.place(x=300, y=300)

        btnUpdate = Button(root, text="Update", font=f, width=10, command=update_data)
        btnUpdate.place(x=400, y=400)

        btnUpdate = Button(root, text="Save", font=f, width=10, command=add)
        btnUpdate.place(x=200, y=400)

        




if __name__ == "__main__":
    root=Tk()
    obj =student(root)
    root.mainloop()



