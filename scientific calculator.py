#scientific calculator

from tkinter import*
from tkinter.messagebox import *
import math as m


#some useful variables
font=("Verdana",18,'bold ')

#important function

def clear():
        ex=textfield.get()
        ex=ex[0:len(ex)-1]
        textfield.delete(0,END)
        textfield.insert(0,ex)


def all_clear():
    textfield.delete(0,END)
    textfield.insert(0, '0')


def click_btn_function(event):
    global p
    print("Button Clicked")
    b=event.widget
    text=b['text']
    print(text)
    

    if text=="x":
        textfield.insert(END,"*")
        return

    if text=="=":
        try:
            ex=textfield.get()
            answer=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,answer)
        except Exception as e:
            print("Error..",e)
            showerror("Error",e)
        return

    if textfield.get() == '0':
        textfield.delete(0, END)

    textfield.insert(END,text)

#windows
window=Tk()
window.title("🔢 My Calculator")
window.geometry("445x570")

#picture label
pic=PhotoImage(file="D:\Project\img2.png\Mini_Project")
headinglabel=Label(window,image=pic)
headinglabel.pack(side=TOP,pady=15)

#heading label
heading=Label(window,text="My calculator",font=font,underline=0)
heading.pack(side=TOP)

#textfield
textfield=Entry(window,font=font,justify=RIGHT)
textfield.pack(side=TOP,pady=10,fill=X,padx=10)
textfield.insert(0, '0')

#buttons
buttonframe=Frame(window)
buttonframe.pack(side=TOP)

#adding buttons
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn= Button(buttonframe,text=str(temp),font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
        btn.grid(row=i,column=j)
        temp=temp+1
        btn.bind("<Button-1>",click_btn_function)

zerobtn= Button(buttonframe,text="0",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
zerobtn.grid(row=3,column=0)

dotbtn= Button(buttonframe,text=".",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
dotbtn.grid(row=3,column=1)

equalbtn= Button(buttonframe,text="=",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
equalbtn.grid(row=3,column=2)

plusbtn= Button(buttonframe,text="+",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
plusbtn.grid(row=0,column=3)

minusbtn= Button(buttonframe,text="-",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
minusbtn.grid(row=1,column=3)

multbtn= Button(buttonframe,text="x",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
multbtn.grid(row=2,column=3)

divbtn= Button(buttonframe,text="/",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
divbtn.grid(row=3,column=3)

clearbtn= Button(buttonframe,text="C",font=font,width=11,relief=RIDGE,activebackground="orange",activeforeground="white",command=clear)
clearbtn.grid(row=4,column=0,columnspan=2)

allclearbtn= Button(buttonframe,text="AC",font=font,width=11,relief=RIDGE,activebackground="orange",activeforeground="white",command=all_clear)
allclearbtn.grid(row=4,column=2,columnspan=2)

#binding buttons
plusbtn.bind("<Button-1>",click_btn_function)
minusbtn.bind("<Button-1>",click_btn_function)
multbtn.bind("<Button-1>",click_btn_function)
divbtn.bind("<Button-1>",click_btn_function)
zerobtn.bind("<Button-1>",click_btn_function)
dotbtn.bind("<Button-1>",click_btn_function)
equalbtn.bind("<Button-1>",click_btn_function)


def enterClick(event):
    print("hi")
    e=Event()
    e.widget=equalbtn
    click_btn_function(e)

textfield.bind("<Return>",enterClick)

######################################################################################################################################################
#functions...
scframe=Frame(window)
#Buttons....
sqrtbtn= Button(scframe,text="√",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
sqrtbtn.grid(row=0,column=0)

powbtn= Button(scframe,text="^",font=font,width=5,relief=RIDGE,activebackground="orange",activeforeground="white")
powbtn.grid(row=0,column=1)

factbtn = Button(scframe, text='x!', font=font, width=5, relief='ridge', activebackground='orange',activeforeground='white')
factbtn.grid(row=0, column=2)

radbtn = Button(scframe, text='toRad', font=font, width=5, relief='ridge', activebackground='orange',activeforeground='white')
radbtn.grid(row=0, column=3)

degbtn = Button(scframe, text='toDeg', font=font, width=5, relief='ridge', activebackground='orange',activeforeground='white')
degbtn.grid(row=1, column=0)

sinbtn = Button(scframe, text='sinθ', font=font, width=5, relief='ridge', activebackground='orange',activeforeground='white')
sinbtn.grid(row=1, column=1)

cosbtn = Button(scframe, text='cosθ', font=font, width=5, relief='ridge', activebackground='orange',activeforeground='white')
cosbtn.grid(row=1, column=2)

tanbtn = Button(scframe, text='tanθ', font=font, width=5, relief='ridge', activebackground='orange',activeforeground='white')
tanbtn.grid(row=1, column=3)

normalcalc=TRUE

def calculate_sc(event):
    print("btn..")
    btn=event.widget
    text=btn['text']
    print(text)
    ex=textfield.get()

    answer=""
    
    if text=='toDeg':
        print("cal degree")
        answer=str(m.degrees(float(ex)))

    elif text=="toRad":
        print('radian')
        answer=str(m.radians(float(ex)))

    elif text=="x!":
        print("cal factoria")
        answer=str(m.factorial(int(ex)))

    elif text=="sinθ":
        print("cal sin")
        answer=str(m.sin(m.radians(int(ex))))

    elif text=="cosθ":
        print("cal cos")
        answer=str(m.cos(m.radians(int(ex))))

    elif text== "tanθ":  
        print("cal tag")
        answer=str(m.tan(m.radians(int(ex))))

    if text=="√":
        print("SQRT")
        answer=m.sqrt(int(ex))

    elif text=="^":
        print("pow")
        base,pow=ex.split(",")
        print(base)
        print(pow)
        answer=m.pow(int(base),int(pow))

    textfield.delete(0,END)

    textfield.insert(0,answer)

def sc_click():
    global normalcalc
    if normalcalc:
        buttonframe.pack_forget()
         #add sc frame
        scframe.pack(side=TOP,pady=20)
        buttonframe.pack(side=TOP)
        window.geometry("445x705")

         #sc
        print("show scientific")
        normalcalc=False
    else:
        print("show normal")
        scframe.pack_forget()
        window.geometry("445x570")
        normalcalc=True

#binding sc buttons
sqrtbtn.bind("<Button-1>",calculate_sc)
powbtn.bind("<Button-1>",calculate_sc)
factbtn.bind("<Button-1>",calculate_sc)
radbtn.bind("<Button-1>",calculate_sc)
degbtn.bind("<Button-1>",calculate_sc)
cosbtn.bind("<Button-1>",calculate_sc)
sinbtn.bind("<Button-1>",calculate_sc)
tanbtn.bind("<Button-1>",calculate_sc)

fontMenu=("",15)
menubar=Menu(window)

mode=Menu(menubar,font=fontMenu,tearoff=0)
mode.add_checkbutton(label="Normal calculator",command=sc_click)

menubar.add_cascade(label="mode",menu=mode)

window.config(menu=menubar)

window.mainloop()