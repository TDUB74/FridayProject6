import tkinter as tk

def sign_up():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

root = tk.Tk()
root.title("Sign Up Page")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

sign_up_button = tk.Button(root, text="Sign Up Now", command=sign_up)
sign_up_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.mainloop()
