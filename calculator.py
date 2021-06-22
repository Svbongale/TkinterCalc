from tkinter import *


root = Tk()
root.title = "Calculator"

e = Entry(root, width=50, borderwidth=2)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(number):
    e.delete(0, END)
    e.insert(0, number)
    return


Button_1 = Button(root, text="1", pady=20, padx=40,
                  command=lambda: button_add(1))
Button_2 = Button(root, text="2", pady=20, padx=40,
                  command=lambda: button_add(2))
Button_3 = Button(root, text="3", pady=20, padx=40,
                  command=lambda: button_add(3))
Button_4 = Button(root, text="4", pady=20, padx=40,
                  command=lambda: button_add(4))
Button_5 = Button(root, text="5", pady=20, padx=40,
                  command=lambda: button_add(5))
Button_6 = Button(root, text="6", pady=20, padx=40,
                  command=lambda: button_add(6))
Button_7 = Button(root, text="7", pady=20, padx=40,
                  command=lambda: button_add(7))
Button_8 = Button(root, text="8", pady=20, padx=40,
                  command=lambda: button_add(8))
Button_9 = Button(root, text="9", pady=20, padx=40,
                  command=lambda: button_add(9))
Button_0 = Button(root, text="0", pady=20, padx=40,
                  command=lambda: button_add(0))

Button_add = Button(root, text="+", pady=20, padx=40, command=button_add)
Button_sub = Button(root, text="-", pady=20, padx=40, command=button_add)
Button_div = Button(root, text="/", pady=20, padx=40, command=button_add)
Button_mul = Button(root, text="*", pady=20, padx=40, command=button_add)

Button_clr = Button(root, text="Clear", pady=20, padx=40, command=button_add)
Button_cancel = Button(root, text="C", pady=20, padx=40, command=button_add)


Button_1.grid(row=1, column=0)
Button_2.grid(row=1, column=1)
Button_3.grid(row=1, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=3, column=0)
Button_8.grid(row=3, column=1)
Button_9.grid(row=3, column=2)
Button_0.grid(row=4, column=0)

Button_add.grid(row=4, column=0)
Button_sub.grid(row=4, column=1)
Button_div.grid(row=4, column=2)
Button_mul.grid(row=5, column=0)

Button_clr.grid(row=5, column=1)
Button_cancel.grid(row=5, column=2)

root.mainloop()
