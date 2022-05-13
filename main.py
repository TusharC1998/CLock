from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title('Clock')

# https://www.1001fonts.com/digital+clock-fonts.html
# To Download Digital CLock font refer to above site. 

lbl=Label(root,font=('Digital-7',30,'bold'), background='Black', foreground='#00FF00')

def time():
    string=strftime('%I:%M:%S %p %a %m/%d/%Y')
    lbl.config(text=string)
    lbl.after(1000,time)

lbl.pack(anchor='center')
time()

mainloop()