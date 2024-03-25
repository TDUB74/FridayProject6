import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Pack Calculator")

entry = tk.Entry(root, state='disabled', font=("Arial", 18), justify='right')
entry.pack(side="top", fill="x")

buttons_frame = tk.Frame(root)
buttons_frame.pack(side="top", expand=True, fill="both")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    btn = tk.Button(buttons_frame, text=text, font=("Arial", 18), padx=20, pady=10)
    btn.grid(row=row, column=col, sticky="nsew")
    btn.bind("<Button-1>", button_click)

root.mainloop()

