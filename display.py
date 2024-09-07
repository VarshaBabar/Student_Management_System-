from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview
from pyrebase import *
import re


class StudentManagementSystemd:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x700+50+50")
        
        firebaseConfig = {
            "apiKey": "YOUR_API_KEY",
            "authDomain": "student-8ec27.firebaseapp.com",
            "databaseURL": "https://student-8ec27-default-rtdb.firebaseio.com/",
            "projectId": "student-8ec27",
            "storageBucket": "student-8ec27.appspot.com",
            "messagingSenderId": "827852263219",
            "appId": "1:827852263219:web:2896d18208ed510b103846",
            "measurementId": "G-QZG2Y66DEE"
        }

        # Initialize Firebase
        self.fb = initialize_app(firebaseConfig)
        self.db = self.fb.database()

        t = ("Century", 25, "bold", "italic")
        f = ("Arial", 15, "bold", "italic")
        v = ("Arial", 10, "bold")

        labtitle = Label(root, text=" Student Management System", font=t)
        #labtitle.place(x=100, y=30)

        self.labID = Label(root, text="Enter Student ID", font=f)
        #self.labID.place(x=50, y=100)

        self.entID = Entry(root, font=f, width=20)
        #self.entID.place(x=300, y=100)

        self.labName = Label(root, text="Enter Student Name", font=f)
        #self.labName.place(x=50, y=200)

        self.entName = Entry(root, font=f, width=20)
        #self.entName.place(x=300, y=200)

        self.labSalary = Label(root, text="Enter Branch Name", font=f)
        #self.labSalary.place(x=50, y=300)

        self.entSalary = Entry(root, font=f, width=20)
        #self.entSalary.place(x=300, y=300)

        self.btnUpdate = Button(root, text="Update", font=f, width=10)
        #self.btnUpdate.place(x=400, y=400)

        self.btnSave = Button(root, text="Save", font=f, width=10)
        #self.btnSave.place(x=200, y=400)

        # Add Treeview widget to display data
        self.tree = Treeview(root, columns=('ID', 'Name', 'Branch'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Branch', text='Branch')
        self.tree.place(x=30, y=10,width=750,height=560)

        # Call method to load data into Treeview
        self.load_data()

    

    def load_data(self):
        # Clear existing data from Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch data from Firebase and populate Treeview
        student_records = self.db.child("fb").get().val()
        if student_records:
            for key, value in student_records.items():
                if isinstance(value, dict):  # Check if value is a dictionary
                    self.tree.insert('', 'end', values=(value.get('ID', ''), value.get('name', ''), value.get('b_name', '')))


if __name__ == "__main__":
    root = Tk()
    app = StudentManagementSystemd(root)
    root.mainloop()
