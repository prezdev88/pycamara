import pygame.image

pygame.font.init()

class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 191, 255)
    YELLOW = (255, 255, 0)

    TITULO = WHITE
    FONDO_TITULO = BLACK
    CUENTA_ATRAS = YELLOW

class Fonts:
    TITULO = pygame.font.SysFont(None, 30)
    CUENTA_ATRAS = pygame.font.SysFont(None, 100)

class K:
    SEGUNDOS_CUENTA_ATRAS = 3
    PHOTOS_PATH = "/home/pi/"
    PHOTO_ICON = "camara.png"

    lista_cuenta_atras = list()

    lista_cuenta_atras.append("3")
    lista_cuenta_atras.append("2")
    lista_cuenta_atras.append("1")

    pasos = list()

    pasos.append("FOTO_CARNET_DELANTERA")
    pasos.append("FOTO_CARNET_TRASERA")
    pasos.append("FOTO_LICENCIA_DELANTERA")
    pasos.append("FOTO_LICENCIA_TRASERA")
    pasos.append("SELFIE")

class Buttons:
    ENTER = 13
    SPACE = 32
    MOUSE_BUTTON_1 = 1