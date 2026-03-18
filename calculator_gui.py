import tkinter as tk

print("program started")

# FUNCTIONS
def click(event):
    global expression
    expression = expression + str(event.widget["text"])
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# 👇 GUI CODE (OUTSIDE FUNCTIONS)
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""
equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=("Arial",20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15)

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial",18))
        button.pack(side="left", expand=True, fill="both")

        if btn == "=":
            button.bind("<Button-1>", lambda event: equal())
        else:
            button.bind("<Button-1>", click)

clear_btn = tk.Button(root, text="C", font=("Arial",18), command=clear)
clear_btn.pack(fill="both")

# 👇 VERY IMPORTANT
root.mainloop()