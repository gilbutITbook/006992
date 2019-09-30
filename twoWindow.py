import tkinter
window1 = tkinter.Tk()
window1.geometry("100x100")
window1.configure(background="white")

window2 = tkinter.Tk()
window2.geometry("100x100")
window2.configure(background="black")

def changecolor():
   print("button1")

def changecolor2():
   print("button2")

btn = tkinter.Button(window1, text="Random color!", command=changecolor)
btn.pack()

btn2 = tkinter.Button(window2, text="Random color!", command=changecolor2)
btn2.pack()

window2.mainloop()
