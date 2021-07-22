from tkinter import *

root = Tk()
root.title('Simple Calculator')

inp = Entry(root, width=42, bd=8)
inp.grid(row=0, column=0, columnspan=3, pady=5, ipady=10)


def click(number):
    try:
        num = int(inp.get() + str(number))
    except:
        num = float(inp.get() + str(number))
    inp.delete(0, END)
    inp.insert(0, num)


def dot():
    current = inp.get()
    inp.delete(0, END)
    inp.insert(0, current + '.')


def clear():
    inp.delete(0, END)
    global first_num
    first_num = 0
    inp.delete(0, END)


def add():
    global first_num
    global math
    math = "addition"
    try:
        first_num = int(inp.get())
    except:
        first_num = float(inp.get())
    inp.delete(0, END)


def subtract():
    global first_num
    global math
    math = "subtraction"
    try:
        first_num = int(inp.get())
    except:
        first_num = float(inp.get())
    inp.delete(0, END)


def multiply():
    global first_num
    global math
    math = "multiplication"
    try:
        first_num = int(inp.get())
    except:
        first_num = float(inp.get())
    inp.delete(0, END)


def divide():
    global first_num
    global math
    math = "division"
    try:
        first_num = int(inp.get())
    except:
        first_num = float(inp.get())
    inp.delete(0, END)


def equal():
    sec_num = int(inp.get())
    inp.delete(0, END)

    if math == "addition":
        inp.insert(0, first_num + sec_num)

    if math == "subtraction":
        inp.insert(0, first_num - sec_num)

    if math == "multiplication":
        inp.insert(0, first_num * sec_num)

    if math == "division":
        if sec_num == 0:
            inp.insert(0, "inf")
        else:
            inp.insert(0, first_num / sec_num)


b1 = Button(root, text="1", width=12, pady=15, command=lambda: click(1))
b2 = Button(root, text="2", width=12, pady=15, command=lambda: click(2))
b3 = Button(root, text="3", width=12, pady=15, command=lambda: click(3))
b4 = Button(root, text="4", width=12, pady=15, command=lambda: click(4))
b5 = Button(root, text="5", width=12, pady=15, command=lambda: click(5))
b6 = Button(root, text="6", width=12, pady=15, command=lambda: click(6))
b7 = Button(root, text="7", width=12, pady=15, command=lambda: click(7))
b8 = Button(root, text="8", width=12, pady=15, command=lambda: click(8))
b9 = Button(root, text="9", width=12, pady=15, command=lambda: click(9))

b0 = Button(root, text="0", width=12, pady=15, command=lambda: click(0))
b_dot = Button(root, text=".", width=12, pady=15, command=dot)
b_clr = Button(root, text="Clear", width=12, pady=15, command=clear)

b_add = Button(root, text="+", width=12, pady=15, command=add)
b_eql = Button(root, text="=", width=26, pady=15, command=equal)

b_sub = Button(root, text="-", width=12, pady=15, command=subtract)
b_mul = Button(root, text="*", width=12, pady=15, command=multiply)
b_div = Button(root, text="/", width=12, pady=15, command=divide)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
b_dot.grid(row=4, column=1)
b_clr.grid(row=4, column=2)

b_add.grid(row=5, column=0)
b_eql.grid(row=5, column=1, columnspan=2)

b_sub.grid(row=6, column=0)
b_mul.grid(row=6, column=1)
b_div.grid(row=6, column=2)

root.mainloop()
