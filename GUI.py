from tkinter import *
Y=Tk()
Y.geometry('500x500+650-100') 
Y.title("3atf")
Y.minsize(500,500)
Y.maxsize(500,500)
X=Tk()
X.title("first window")
X.geometry('500x500+150-100')
Y.resizable(False,False)
X.lift()
#X.lower() 
X.state("normal") #X.iconify() zy X.state("iconic"))
if X.state()=="normal":
    X.state("withdraw") # X.destroy() zy withdraw
X.state("normal") #X.deiconify() zy normal 
Y.configure(bg='dodgerblue')
X.configure(bg='dodgerblue')
text=Label(Y, text="what's your name?")#to write something in the window command is : (Label)
text.grid(column=0, row=0)
def button1():
    text2.configure(text="your amount is : 1k$")
def button2():
    res = "Welcome  " + ins.get() +  "!" #command (function y3ny)
    text.configure(text= res)
def withdraw():
    X.state("withdraw")
def reviveB():
    X.state("normal")
def destroy():
    Y.destroy()
button = Button(X, text="Dispaly ur amount" , bg="aqua" , fg="black",command=button1)#to add a button command is : (Button)
button.grid(column=8, row=0)
text2=Label(X, text="welcome to your account !")
text2.grid(column=0, row=0)
ins=Entry(Y,width=15 )#zy input bs fl window bta5od data mn el user  #state='disabled' (u can no longer write in the entry space)
ins.grid(column=1, row=0)
X.state("normal")
button2 = Button(Y, text="confirm" , bg="aqua" , fg="black",command=button2) #button dy 2sm el el function ely fo2 
button2.grid(column=17, row=0)
text3=Label(X, text="--->")
text3.grid(column=0, row=2)
withdrawB=Button(X, text="click to kill the window " , bg="aqua" , fg="black", command=withdraw)
withdrawB.grid(column=2, row=2)
Y.lift()
reviveB=Button(Y, text="click to revive the killed window " , bg="aqua" , fg="black", command=reviveB)
reviveB.grid(column=3, row=2)
text4=Label(Y, text="--->")
text4.grid(column=0, row=2)
from tkinter import messagebox
def info():
    messagebox.showinfo('info', 'this is an info message ')
btn = Button(X,text='info', command=info)
btn.grid(column=4,row=5)
def warning():
    messagebox.showwarning('warining', 'this is a warining message ')
btn2 = Button(X,text='warining', command=warning)
btn2.grid(column=0,row=5)
#res = messagebox.askquestion('askQ','how r ya ?') res = messagebox.askyesno('Message title','Message content') res = messagebox.askyesnocancel('Message title','Message content') res = messagebox.askokcancel('Message title','Message content') res = messagebox.askretrycancel('Message title','Message content')
ins.focus()
exitB=Button(Y,text='Exit' , bg="aqua" , fg="black", command=destroy)
exitB.grid(column=0 , row=4)
X.mainloop()
Y.mainloop()
