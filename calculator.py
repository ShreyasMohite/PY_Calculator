from tkinter import  Label,Frame,Button,Text,StringVar,Tk,Entry,LabelFrame
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
F1.pack(side="top")
F2=Frame(root)
F2.pack(side="top")
F3=Frame(root)
F3.pack(side="top")
F4=Frame(root)
F4.pack(side="top")
#======================entry widget
E=Entry(F1,bd=10,text=num1,insertwidth=3,font=50,width=28,state="readonly").pack( )
#=======================button
txtbut1=Button(F1,text=1,fg="black",bd=10,bg="red",width=6,command=lambda:btnclick(1)).pack(side="left")
txtbut2=Button(F1,text=2,fg="black",bd=10,width=6,bg="yellow",command=lambda:btnclick(2)).pack(side="left")
txtbut3=Button(F1,text=3,fg="black",bd=10,width=6,bg="red",command=lambda:btnclick(3)).pack(side="left")
txtbutw=Button(F1,text='+',fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick('+')).pack(side="left")
#==============================================
txtbut4=Button(F2,text=4,fg="black",bd=10,width=6,bg="yellow",command=lambda:btnclick(4)).pack(side="left")
txtbut5=Button(F2,text=5,fg="black",bd=10,width=6,bg="red",command=lambda:btnclick(5)).pack(side="left")
txtbut6=Button(F2,text=6,fg="black",bd=10,width=6,bg="yellow",command=lambda:btnclick(6)).pack(side="left")
txtbutx=Button(F2,text='-',fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick('-')).pack(side="left")
#==================================================
txtbut7=Button(F3,text=7,fg="black",bd=10,width=6,bg="red",command=lambda:btnclick(7)).pack(side="left")
txtbut8=Button(F3,text=8,fg="black",bd=10,width=6,bg="yellow",command=lambda:btnclick(8)).pack(side="left")
txtbut9=Button(F3,text=9,fg="black",bd=10,width=6,bg="red",command=lambda:btnclick(9)).pack(side="left")
txtbuty=Button(F3,text='/',fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick('/')).pack(side="left")
#================================================
txtbutz=Button(F4,text='*',fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick('*')).pack(side="left")
txtbute=Button(F4,text='C',fg="black",bg="powder blue",bd=10,width=6,command=clrdisplay).pack(side="left")
txtbutr=Button(F4,text=0,fg="black",bg="powder blue",bd=10,width=6,command=lambda:btnclick(0)).pack(side="left")
txtbutt=Button(F4,text='=',fg="black",bg="powder blue",bd=10,width=6,command=eqals).pack(side="left")



root.mainloop()
