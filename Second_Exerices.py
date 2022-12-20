from tkinter import *
from tkinter import ttk

def Draw():
    i1 = int ( s1 . get ())
    i2 = str ( s2 . get ())
    mysy="" 

    for i in range(i1):
        for j in range(i1):
            if(i == 0 or i == i1 - 1 or j == 0 or j == i1 - 1):
                mysy=mysy+i2
            else:
                mysy=mysy+" "
        mysy=mysy+"\n"

    l3 ["text"] = mysy

    
w = Tk ()
w.title ("CENG105")
#w.geometry ("300x200")
w.columnconfigure (0 , weight =1)
form = ttk.Frame (w , padding =10)
form.grid ()

s1 = StringVar ()
s2 = StringVar ()

ttk.Label ( form , text = "Lines: " ). grid ( column =0 , row =0)
ttk.Label(form, text= "Character: ").grid(column=0, row=1)

e1 = Entry ( form , textvariable = s1 )
e1 . grid ( column =1 , row =0)

e2 = Entry ( form , textvariable = s2 )
e2 . grid ( column =1 , row =1)

l3 = Label ( form , text = "", font ="Monospace" )

b1=Button ( form , text = "Draw" , command =  Draw ). grid ( column =0 , columnspan =2 , row =2, sticky = " we " )

l3 . grid ( column =0 , row =3 , columnspan =2)

w.mainloop ()