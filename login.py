from tkinter import *
from tkinter.messagebox import *
from pyrebase import *
from student1 import student
from register import student10
from display import StudentManagementSystemd



# Firebase configuration
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
auth = fb.auth()

root = Tk()
root.title("Student Management System")
root.geometry("400x180+500+200")

def register():
    new_window=Toplevel(root)
    app=student10(new_window)

def login():
    email = entry_email.get()
    password = entry_password.get()

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        showinfo("Success", "Login Successful!")
        open_main_window()
    except Exception as e:
        showerror("Error", "Login Failed!\n" + str(e))

def open_main_window():
    new_window=Toplevel(root)
    app=student(new_window)
    # You can place your main application window code here



def login1():
    email = entry_email.get()
    password = entry_password.get()

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        showinfo("Success", "Login Successful!")
        open_main_window1()
    except Exception as e:
        showerror("Error", "Login Failed!\n" + str(e))

def open_main_window1():
    new_window=Toplevel(root)
    app=StudentManagementSystemd(new_window)

label_email = Label(root, text="Email:")
label_email.pack()

entry_email = Entry(root)
entry_email.pack()

label_password = Label(root, text="Password:")
label_password.pack()

entry_password = Entry(root, show="*")
entry_password.pack()

button_login = Button(root, text="Login", command=login)
button_login.pack()

button_login = Button(root, text="Register", command=register)
button_login.pack()
button_login = Button(root, text="Display Data", command=login1)
button_login.pack()

root.mainloop()
