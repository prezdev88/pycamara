# sudo pacman -S tk
# sudo apt-get install tk

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from Camara import *
from PIL import ImageTk, Image

class Main:

    def __init__(self):
        self.root = Tk()

        # Undecorated
        self.root.overrideredirect(True)
        self.init_screen_position()

    def camera_click_event(self, event):
        camara = Camara()
        camara.open()

    def init_screen_position(self):
        self.width = self.root.winfo_screenwidth() 
        self.height = self.root.winfo_screenheight()
        self.photoWidth = 128

        x = self.width - self.photoWidth
        y = 0

        self.root.geometry('%dx%d+%d+%d' % (self.photoWidth, self.photoWidth, x, y)) # anchura x altura

    def main(self):
        # -------------------- init components --------------------
        cameraIcon = ImageTk.PhotoImage(Image.open("camara.png"))

        self.lbl_camera = Label(self.root, image = cameraIcon)
        self.lbl_camera.bind('<Double-Button-1>', self.camera_click_event)

        # cerrar con botón de scroll
        # panel.bind('<Button-2>', quit)

        self.lbl_camera.pack(side = "bottom", fill = "both", expand = "yes")
        # -------------------- init components --------------------
        self.root.mainloop()

app = Main()
app.main()