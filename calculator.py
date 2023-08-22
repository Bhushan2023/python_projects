

from tkinter import Tk,Frame,Button,Label,StringVar

from math import*

screen_val = Tk()

screen_val.title("Calculator")

screen_val.geometry('300x350+200+150')

screen_val.resizable(0,0) # This will disable the user to minimum and maximize of the screen.

val = ''
data = StringVar()

def btn1_isclicked():
    global val
    val = val+'1' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn2_isclicked():
    global val
    val = val+'2' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn3_isclicked():
    global val
    val = val+'3' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn4_isclicked():
    global val
    val = val+'4' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn5_isclicked():
    global val
    val = val+'5' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn6_isclicked():
    global val
    val = val+'6' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn7_isclicked():
    global val
    val = val+'7' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn8_isclicked():
    global val
    val = val+'8' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn9_isclicked():
    global val
    val = val+'9' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btn0_isclicked():
    global val
    val = val+'0' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btnplus_isclicked():
    global val
    val = val+'+' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btnminus_isclicked():
    global val
    val = val+'-' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btnmul_isclicked():
    global val
    val = val+'*' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btndiv_isclicked():
    global val
    val = val+'/' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btnC_isclicked():
    global val
    val = ''
    data.set(val)

def btnequal_isclicked():
    global val
    val = eval(val)
    val = str(val)
    data.set(val)

def btndel_isclicked():
    global val
    val = val[:-1] # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btnpow_isclicked():
    global val
    val = val+'**' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btndot_isclicked():
    global val
    val = val+'.' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

def btnper_isclicked():
    global val
    val = val/'100' # ''+'1' -> '1'
    # val += '1'
    data.set(val)

lbl_data = Label(screen_val,text="This is Label",anchor='se',font=('Verdana',20),textvariable=data)
lbl_data.pack(fill='both',expand=True)

frame1 = Frame(screen_val,bg='red')
frame1.pack(expand=True,fill='both')

frame2 = Frame(screen_val,bg='blue')
frame2.pack(expand=True,fill='both')

frame3 = Frame(screen_val,bg='green')
frame3.pack(expand=True,fill='both')

frame4 = Frame(screen_val,bg='yellow')
frame4.pack(expand=True,fill='both')

frame5 = Frame(screen_val,bg='orange')
frame5.pack(expand=True,fill='both')


btnC = Button(frame1,text='C',font=('Verdana',20),border=0,command=btnC_isclicked)
btnC.pack(expand=True,fill='both',side='left')

btnpow = Button(frame1,text='^',font=('Verdana',20),border=0,command=btnpow_isclicked)
btnpow.pack(expand=True,fill='both',side='left')

btndel = Button(frame1,text='<',font=('Verdana',20),border=0,command=btndel_isclicked)
btndel.pack(expand=True,fill='both',side='left')

btnplus = Button(frame1,text='+',font=('Verdana',20),border=0,command=btnplus_isclicked)
btnplus.pack(expand=True,fill='both',side='left')

btn7 = Button(frame2,text='7',font=('Verdana',20),border=0,command=btn7_isclicked)
btn7.pack(expand=True,fill='both',side='left')

btn8 = Button(frame2,text='8',font=('Verdana',20),border=0,command=btn8_isclicked)
btn8.pack(expand=True,fill='both',side='left')

btn9 = Button(frame2,text='9',font=('Verdana',20),border=0,command=btn9_isclicked)
btn9.pack(expand=True,fill='both',side='left')

btnminus = Button(frame2,text='-',font=('Verdana',20),border=0,command=btnminus_isclicked)
btnminus.pack(expand=True,fill='both',side='left')

btn4 = Button(frame3,text='4',font=('Verdana',20),border=0,command=btn4_isclicked)
btn4.pack(expand=True,fill='both',side='left')

btn5 = Button(frame3,text='5',font=('Verdana',20),border=0,command=btn5_isclicked)
btn5.pack(expand=True,fill='both',side='left')

btn6 = Button(frame3,text='6',font=('Verdana',20),border=0,command=btn6_isclicked)
btn6.pack(expand=True,fill='both',side='left')

btnmul = Button(frame3,text='*',font=('Verdana',20),border=0,command=btnmul_isclicked)
btnmul.pack(expand=True,fill='both',side='left')

btn1 = Button(frame4,text='1',font=('Verdana',20),border=0,command=btn1_isclicked)
btn1.pack(expand=True,fill='both',side='left')

btn2 = Button(frame4,text='2',font=('Verdana',20),border=0,command=btn2_isclicked)
btn2.pack(expand=True,fill='both',side='left')

btn3 = Button(frame4,text='3',font=('Verdana',20),border=0,command=btn3_isclicked)
btn3.pack(expand=True,fill='both',side='left')

btndiv = Button(frame4,text='/',font=('Verdana',20),border=0,command=btndiv_isclicked)
btndiv.pack(expand=True,fill='both',side='left')

btnper = Button(frame5,text='%',font=('Verdana',20),border=0,command=btnper_isclicked)
btnper.pack(expand=True,fill='both',side='left')

btn0 = Button(frame5,text='0',font=('Verdana',20),border=0,command=btn0_isclicked)
btn0.pack(expand=True,fill='both',side='left')

btndot = Button(frame5,text='.',font=('Verdana',20),border=0,command=btndot_isclicked)
btndot.pack(expand=True,fill='both',side='left')

btnequal = Button(frame5,text='=',font=('Verdana',20),border=0,command=btnequal_isclicked)
btnequal.pack(expand=True,fill='both',side='left')

screen_val.mainloop()
