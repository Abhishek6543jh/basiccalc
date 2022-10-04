from tkinter import *

#for shoeing typed equation in the label 
def eqshow(val):
    global eqtext
    eqtext = eqtext + str(val)
    eqlabel.set(eqtext)

#for equating the expression
def equal():
    try:
        finaleq = lable['text']
        res = eval(finaleq)
        eqlabel.set(str(res))
    except ArithmeticError:
        eqlabel.set("ARTHEMATIC ERROR")
    except:
        eqlabel.set("INVALID EXPRESSION")

#for clearing the euqtion in label
def clear():
    global eqtext
    eqlabel.set('')
    eqtext = ""


window = Tk()
frame1 = Frame(window,padx=10,pady=20)
frame1.pack()
frame2 = Frame(window,padx=1,pady=1,bg="blue")
frame2.pack()
frame3 = Frame(window,padx=1,pady=1,bg="green")
frame3.pack()
#creating a label 
eqtext = "     "
eqlabel=StringVar()
lable = Label(frame1,textvariable=eqlabel,bg="white",padx=115,pady=30)
lable.grid(row=0,column=0)
#
#creating buttons 
bt0 = Button(frame2,text="0",padx=19,pady=24,command=lambda :eqshow(0))
bt0.grid(row=0,column=0)
button1 = Button(frame2,text="1",padx=19,pady=24,command=lambda :eqshow(1))
button1.grid(row=0,column=1)
button2 = Button(frame2,text="2",padx=19,pady=24,command=lambda :eqshow(2))
button2.grid(row=0,column=2)
button3 = Button(frame2,text="3",padx=19,pady=24,command=lambda :eqshow(3))
button3.grid(row=1,column=0)
button4 = Button(frame2,text="4",padx=19,pady=24,command=lambda :eqshow(4))
button4.grid(row=1,column=1)
button5 = Button(frame2,text="5",padx=19,pady=24,command=lambda :eqshow(5))
button5.grid(row=1,column=2)
button6 = Button(frame2,text="6",padx=19,pady=24,command=lambda :eqshow(6))
button6.grid(row=2,column=0)
button7 = Button(frame2,text="7",padx=19,pady=24,command=lambda :eqshow(7))
button7.grid(row=2,column=1)
button8 = Button(frame2,text="8",padx=19,pady=24,command=lambda :eqshow(8))
button8.grid(row=2,column=2)
button9 = Button(frame2,text="9",padx=20,pady=24,command=lambda :eqshow(9))
button9.grid(row=0,column=3)
buttoneq = Button(frame2,text="=",padx=19,pady=24,command=equal)
buttoneq.grid(row=2,column=3)
buttonpls = Button(frame2,text="+",padx=19,pady=24,command=lambda :eqshow('+'))
buttonpls.grid(row=1,column=3)
buttonminus = Button(frame2,text="-",padx=19,pady=24,command=lambda :eqshow('-'))
buttonminus.grid(row=0,column=4)
buttonmultply = Button(frame2,text="*",padx=19,pady=24,command=lambda :eqshow('*'))
buttonmultply.grid(row=1,column=4)
buttondiv = Button(frame2,text="/",padx=19,pady=24,command=lambda :eqshow('/'))
buttondiv.grid(row=2,column=4)
buttonclear = Button(frame3,text="clear",padx=20,pady=25,command=clear)
buttonclear.grid(row=3,column=2)
###

window.title("basic calc")
window.geometry("450x450")
window.mainloop()
