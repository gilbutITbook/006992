import tkinter

window = tkinter.Tk()
window.geometry("200x800")
window.title("주소록")

phonebook = {}

def add():
    name = txt_name.get()
    phone = txt_phone.get()
    email = txt_email.get()
    phonebook[name] = [phone, email]
    lbl.configure(text = "연락처를 추가했습니다!")

def show():
    s = ""
    for name, details in phonebook.items():
        s += name+"\n"+details[0]+"\n"+details[1]+"\n\n"
    lbl.configure(text=s)

txt_name = tkinter.Entry()
txt_phone = tkinter.Entry()
txt_email = tkinter.Entry()

btn_add = tkinter.Button(text="연락처 추가", command=add)
btn_show = tkinter.Button(text="모두 보기", command=show)

lbl = tkinter.Label()

txt_name.pack()
txt_phone.pack()
txt_email.pack()
btn_add.pack()
btn_show.pack()
lbl.pack()

window.mainloop()
