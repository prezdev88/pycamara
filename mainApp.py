# sudo pacman -S tk
# sudo apt-get install tk

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from PIL import ImageTk, Image
from Camara import *

def photoClick(event):
    camara = Camara()
    camara.open()


root = Tk()

root.geometry('128x128') # anchura x altura

root.title('AWTO')
root.overrideredirect(True)

img = ImageTk.PhotoImage(Image.open("camara.png"))
panel = Label(root, image = img)
panel.bind('<Button-1>', photoClick)
panel.bind('<Button-2>', quit)

panel.pack(side = "bottom", fill = "both", expand = "yes")

# ttk.Button(root, text='Salir', command=quit).pack(side=BOTTOM)

root.mainloop()

