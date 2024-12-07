import tkinter as tk

root = tk.Tk()
root.title("Rishabh's Calculator")
root.geometry("480x720")

lable = tk.Label(root, text="Hello World!", font=("Arial",24))
lable.pack(padx=20, pady=20)

t = tk.Text(root, height= 15, width=50)
t.pack(pady=20, padx=20)

entry = tk.Entry(root)
entry.pack()

buttonframe = tk.Frame(root)
buttonframe.pack(fill='x')

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1")
btn1.grid(row=0, column=1, sticky=tk.E+tk.W)


btn2 = tk.Button(buttonframe, text="2")
btn2.grid(row=0, column=2,sticky=tk.E+tk.W)


btn3 = tk.Button(buttonframe, text="3")
btn3.grid(row=1, column=0,sticky=tk.E+tk.W)


btn4 = tk.Button(buttonframe, text="4")
btn4.grid(row=1, column=1,sticky=tk.E+tk.W)


btn5 = tk.Button(buttonframe, text="5")
btn5.grid(row=1, column=2,sticky=tk.E+tk.W)


btn6 = tk.Button(buttonframe, text="6")
btn6.grid(row=2, column=0,sticky=tk.E+tk.W)


btn7 = tk.Button(buttonframe, text="7")
btn7.grid(row=2, column=1,sticky=tk.E+tk.W)


btn8 = tk.Button(buttonframe, text="8")
btn8.grid(row=2, column=2,sticky=tk.E+tk.W)

btn9 = tk.Button(buttonframe, text="9")
btn9.grid(row=3, column=1,sticky=tk.E+tk.W)


btn0 = tk.Button(buttonframe, text="0")
btn0.grid(row=0, column=0, sticky=tk.E+tk.W)

root.mainloop()