from tkinter import *
from tkinter import ttk


def ekle():
    i1 = int ( s1 . get ())
    i2 = int ( s2 . get ())
    l3 ["text"] = "Result: " + str ( i1+i2 ) 
    
def cikar():
    i1 = int ( s1 . get ())
    i2 = int ( s2 . get ())
    l3 ["text"] = "Result: " + str ( i1- i2 )
def carp():
    i1 = int ( s1 . get ())
    i2 = int ( s2 . get ())
    l3 ["text"] = " Result: " + str ( i1* i2 )
def bol():
    i1 = int ( s1 . get ())
    i2 = int ( s2 . get ())
    l3 ["text"] = " Result: " + str ( i1/ i2 )


w = Tk ()
w.title ("CENG105")
#w.geometry ("300x200")
w.columnconfigure (0 , weight =1)
form = ttk.Frame (w , padding =10)
form.grid ()

s1 = StringVar ()
s2 = StringVar ()

ttk.Label ( form , text = "First Number: " ). grid ( column =0 , row =0)
ttk.Label(form, text= "Second Number: ").grid(column=2, row=0)

e1 = Entry ( form , textvariable = s1 )
e1 . grid ( column =1 , row =0)

e2 = Entry ( form , textvariable = s2 )
e2 . grid ( column =3 , row =0)

l3 = Label ( form , text = " " )

b1=Button ( form , text = "+" , command =  ekle ). grid ( column =0 , row =1,sticky = " we ")
b2=Button ( form , text = "-" , command = cikar ). grid ( column =1 , row =1,sticky = " we ")
b3=Button ( form , text = "*" , command = carp ). grid ( column =2 , row =1,sticky = " we ")
b4=Button ( form , text = "/" , command = bol ). grid ( column =3 ,row =1,sticky = " we ")


l3 . grid ( column =0 , row =3 , columnspan =2)

w.mainloop ()