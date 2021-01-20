from tkinter import *
class MyButtons:
    def _init_(self,root):
        self.f = Frame(root,height=350,width=500)
                       
        self.f.propagate(0)
        
        self.f.pack()
        
        self.b1 = Button(self.f, text='Hi', width=15, height=2, command=self.buttonClick)
        
        self.b2 = Button(self.f, text='close', width=15, height=2, command=quit)
        
        self.b1.grid(row=0, column=1)
        self.b2.grid(row=0, column=2)
        
        def buttonClick(self):
            self.lbl = Label(self.f, text='Hello Gowthami', width=20, height=2, font=('courier', -30, 'bold underline '), fg= 'blue')
        
            self.lbl.grid(row=2,column=0)
        
root=Tk()
mb= MyButtons(root)
root.mainloop()
        
        