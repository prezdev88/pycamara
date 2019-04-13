# sudo pip3 install pygame
# https://tpec05.blogspot.com/2016/11/dibujo-de-figuras-geometricas-en-pygame.html

import pygame.camera
import pygame.image
import sys
import os

from Rules import Colors
from Rules import Fonts
from Rules import K
from Rules import Buttons

class Camara:

    def exit(self):
        self.close()
        sys.exit()

    def close(self):
        self.webcam.stop()

    def __init__(self):
        self.is_conteo = False
        self.comenzar_conteo = False
        self.texto_cuenta_atras = None

        # Centrado
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.camera.init()

        self.cameras = pygame.camera.list_cameras()
        self.webcam = pygame.camera.Camera(self.cameras[0])

        self.i = 0

    def takePhoto(self):
        self.comenzar_conteo = False
        self.is_conteo = False
        self.texto_cuenta_atras = None

        paso = K.pasos[self.i]
        self.i += 1

        try:
            pygame.image.save(self.img, K.PHOTOS_PATH+str(self.i)+"_"+paso+".png")
        except Exception:
            pygame.image.save(self.img, str(self.i)+"_"+paso+".png")
        
        if self.i == 5:
            self.exit()

    def open(self):
        self.webcam.start()
        
        # grab first frame
        self.img = self.webcam.get_image()

        self.WIDTH = self.img.get_width()
        self.HEIGHT = self.img.get_height()

        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        
        pygame.display.set_caption("Awto Camera")

        try:
            while True :
                if self.comenzar_conteo:
                    start_ticks = pygame.time.get_ticks() #starter tick
                    self.comenzar_conteo = False

                if self.is_conteo:
                    seconds = (pygame.time.get_ticks() - start_ticks) / 1000

                    if (seconds > K.SEGUNDOS_CUENTA_ATRAS):
                        self.takePhoto()

                    else:
                        indice = int(seconds)
                        cuenta = K.lista_cuenta_atras[indice]

                        self.texto_cuenta_atras = Fonts.CUENTA_ATRAS.render(
                            cuenta,
                            False,
                            Colors.CUENTA_ATRAS
                        )

                        # print(seconds)

                for e in pygame.event.get() :
                    if e.type == pygame.QUIT :
                        self.exit()

                    if e.type == pygame.KEYDOWN:
                        # si es enter o espacio
                        if e.key == Buttons.ENTER or e.key == Buttons.SPACE:
                            self.comenzar_conteo = True
                            self.is_conteo = True

                    if e.type == pygame.MOUSEBUTTONUP and e.button == Buttons.MOUSE_BUTTON_1:
                        self.comenzar_conteo = True
                        self.is_conteo = True

                # draw frame
                self.screen.blit(self.img, (0,0))

                # Fondo para las letras
                pygame.draw.rect(self.screen, Colors.FONDO_TITULO, [0, 0, self.WIDTH, 30], 0)

                # Texto
                texto = Fonts.TITULO.render(K.pasos[self.i].replace("_", " "), False, Colors.TITULO)

                self.screen.blit(texto,(5,5))

                if self.texto_cuenta_atras is not None:
                    self.screen.blit(self.texto_cuenta_atras, (self.WIDTH / 2, (self.HEIGHT / 2) - 30))
                
                pygame.display.flip()
                # grab next frame    
                self.img = self.webcam.get_image()
        except SystemExit:
            pygame.quit()

#cam = Camara()
#cam.open()