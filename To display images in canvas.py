#A python program to display images in canvas

from tkinter import *

#create root window
root=Tk()

#create canvas as a child to root window
c =Canvas(root, bg='white', height=700, width=1200)

#copy images into files
file1 = PhotoImage(file="dog.gif")
file2 = PhotoImage(file='puppy.gif')

#display the image in canvas in NE direction
#when mouse is placed on cat image
id =c.create_image(500, 200, anchor =NE , image =file1,  activeimage=file2)

#dispay some text below the image
id=c.create_text(500,500,text='This is aThirilling photo',font=('Jokerman',40,bold),fill='blue')

#add canvas to the root
c.pack()

#wait for any events
root.mainloop()