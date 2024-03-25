import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    print("Username:", username)
    print("Password:", password)
    
root = tk.Tk()
root.title("Login Page")

username_label = tk.Label(root, text="Username:")
username_label.place(x=50, y=50)

password_label = tk.Label(root, text="Password:")
password_label.place(x=50, y=100)

username_entry = tk.Entry(root)
username_entry.place(x=150, y=50)

password_entry = tk.Entry(root, show="*")
password_entry.place(x=150, y=100)

login_button = tk.Button(root, text="Login", command=login)
login_button.place(x=150, y=150)

root.mainloop()
