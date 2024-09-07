from tkinter import *
from tkinter.messagebox import *
from pyrebase import *


class student10:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        root.geometry("400x180+400+200")
        
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

        
        root.geometry("400x180")

        def register():
            email = entry_email.get()
            password = entry_password.get()

            try:
                auth.create_user_with_email_and_password(email, password)
                showinfo("Success", "User Registered Successfully!")
            except Exception as e:
                showerror("Error", "Registration Failed!\n" + str(e))




            # You can place your main application window code here

        label_email = Label(root, text="Email:")
        label_email.pack()

        entry_email = Entry(root)
        entry_email.pack()

        label_password = Label(root, text="Password:")
        label_password.pack()

        entry_password = Entry(root, show="*")
        entry_password.pack()



        button_login = Button(root, text="Register", command=register)
        button_login.pack()

if __name__ == "__main__":
    root=Tk()
    obj =student10(root)
    root.mainloop()
