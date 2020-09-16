import tkinter
from tkinter import *
import PIL
#======================declaretion=======================

    
def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    num1.set(operator)
    
def clrdisplay():
    global operator
    operator=""
    num1.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    num1.set(sumup)
    #operator = ""

#===========================================================
root=Tk( )
root.iconbitmap('calc.ico')
root.title("calculator")
root.resizable(0,0)

num1=StringVar( )
operator=""

#======================##frame 1============================================
F1=Frame(root)
F1.pack(side=TOP)
F2=Frame(root)
F2.pack(side=TOP)
F3=Frame(root)
F3.pack(side=TOP)
F4=Frame(root)
F4.pack(side=TOP)
#======================entry widget
E=Entry(F1,bd=10,text=num1,insertwidth=3,font=50,width=28,state="readonly").pack( )
#=======================button
txtbut1=Button(F1,text=1,fg="black",bd=10,bg="red",width=6,command=lambda:btnclick(1)).pack(side=LEFT)
txtbut2=Button(F1,text=2,fg="black",bd=10,width=6,bg="yellow",command=lambda:btnclick(2)).pack(side=LEFT)
txtbut3=Button(F1,text=3,fg="black",bd=10,width=6,bg="red",command=lambda:btnclick(3)).pack(side=LEFT)
txtbutw=Button(F1,text='+',fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick('+')).pack(side=LEFT)
#==============================================
txtbut4=Button(F2,text=4,fg="black",bd=10,width=6,bg="yellow",command=lambda:btnclick(4)).pack(side=LEFT)
txtbut5=Button(F2,text=5,fg="black",bd=10,width=6,bg="red",command=lambda:btnclick(5)).pack(side=LEFT)
txtbut6=Button(F2,text=6,fg="black",bd=10,width=6,bg="yellow",command=lambda:btnclick(6)).pack(side=LEFT)
txtbutx=Button(F2,text='-',fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick('-')).pack(side=LEFT)
#==================================================
txtbut7=Button(F3,text=7,fg="black",bd=10,width=6,bg="red",command=lambda:btnclick(7)).pack(side=LEFT)
txtbut8=Button(F3,text=8,fg="black",bd=10,width=6,bg="yellow",command=lambda:btnclick(8)).pack(side=LEFT)
txtbut9=Button(F3,text=9,fg="black",bd=10,width=6,bg="red",command=lambda:btnclick(9)).pack(side=LEFT)
txtbuty=Button(F3,text='/',fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick('/')).pack(side=LEFT)
#================================================
txtbutz=Button(F4,text='*',fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick('*')).pack(side=LEFT)
txtbute=Button(F4,text='C',fg="black",bg="powder blue",bd=10,width=6,command=clrdisplay).pack(side=LEFT)
txtbutr=Button(F4,text=0,fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick(0)).pack(side=LEFT)
txtbutt=Button(F4,text='=',fg="black",bg="powder blue",bd=10,width=6,command=eqals).pack(side=LEFT)



root.mainloop()
