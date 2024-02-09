from tkinter import *

def Exit():
    window.quit()

def New():
    def Load():
        with open('Target.txt') as f:
            data = f.read()
        txt_1.insert(INSERT,data)
    def Save():
        with open('Target.txt',"w") as f:
            f.write(txt_1.get(1.0,END))

    window_2 = Toplevel()
    window_2.resizable(width=False, height=False)
    window_2.title('Steve13 - Text Editor')

    txt_1 = Text(window_2)
    txt_1.pack(fill=BOTH)

    Button(window_2, text='Save', command=Save).pack(side='bottom')
    Button(window_2, text='Load', command=Load).pack(side='bottom')

window = Tk()
window.resizable(width=False, height=False)
#window.geometry('100x100')
window.config(bg='light gray')
window.title('Steve13 - Menu Text Editor')

Label(window, text=' ', bg='light gray').pack()

Button(text='New', command=New).pack(pady=5, padx=5)
Button(text='Quit', fg='red', command=Exit).pack(padx=5, pady=5)

Label(window, text=' ', bg='light gray').pack()





window.mainloop()