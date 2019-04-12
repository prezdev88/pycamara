# sudo pacman -S tk
# sudo apt-get install tk

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from Camara import *
from PIL import ImageTk, Image

def photoClick(event):
    camara = Camara()
    camara.open()

def screenPosition():
    width = root.winfo_screenwidth() 
    height = root.winfo_screenheight()
    photoWidth = 128

    x = width - photoWidth
    y = 0

    root.geometry('%dx%d+%d+%d' % (photoWidth, photoWidth, x, y)) # anchura x altura

root = Tk()

screenPosition()

root.title('AWTO')
root.overrideredirect(True)

cameraIcon = ImageTk.PhotoImage(Image.open("camara.png"))
lblCamera = Label(root, image = cameraIcon)
lblCamera.bind('<Double-Button-1>', photoClick)

# cerrar con botón de scroll
# panel.bind('<Button-2>', quit)

lblCamera.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()

