# imports
from tkinter import *
import os
from PIL import ImageTk, Image 

# main screen
master = Tk()
master.title('Pesa')

# import image
img = Image.open('banx.jpg')
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

# labels
Label(master, text = 'Pesa Banking', font=('Calibri', 15)).grid(row=0, sticky=N, pady=10)
Label(master, text = "Safe and reliable banking for all your needs", font=('Times New Roman', 12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

mainloop()