# sudo pip3 install pygame
# https://tpec05.blogspot.com/2016/11/dibujo-de-figuras-geometricas-en-pygame.html

import pygame.camera
import pygame.image
import sys
import os

class Camara:

    def exit(self):
        self.close()
        sys.exit()

    def close(self):
        self.webcam.stop()

    def initConstants(self):
        self.ENTER = 13
        self.SPACE = 32
        self.MOUSE_BUTTON_1 = 1

    def init_colors(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 191, 255)

        self.COLOR_LETRA = self.WHITE
        self.COLOR_FONDO_LETRA = self.BLACK

    def __init__(self):
        self.initConstants()
        self.PHOTOS_PATH = "/home/pi/"
        self.init_colors()
        self.is_conteo = False
        self.comenzar_conteo = False

        # Centrado
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.camera.init()

        self.cameras = pygame.camera.list_cameras()
        self.webcam = pygame.camera.Camera(self.cameras[0])

        self.pasos = list()

        self.pasos.append("CARNET_FRONT")
        self.pasos.append("CARNET_BACK")
        self.pasos.append("LICENCIA_FRONT")
        self.pasos.append("LICENCIA_BACK")
        self.pasos.append("SELFIE")

        self.i = 0

        self.myfont = pygame.font.SysFont(None, 30)

    def takePhoto(self):
        self.comenzar_conteo = True
        self.is_conteo = True

        paso = self.pasos[self.i]
        self.i += 1

        try:
            pygame.image.save(self.img, self.PHOTOS_PATH+str(self.i)+"_"+paso+".png")
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

        pygame.font.init()

        try:
            
            while True :

                if self.comenzar_conteo:
                    start_ticks = pygame.time.get_ticks() #starter tick
                    self.comenzar_conteo = False

                if self.is_conteo:
                    seconds = (pygame.time.get_ticks()-start_ticks) / 1000
                    print(seconds)    

                for e in pygame.event.get() :
                    if e.type == pygame.QUIT :
                        self.exit()
                    
                    if e.type == pygame.KEYDOWN:
                        # si es enter o espacio
                        if e.key == self.ENTER or e.key == self.SPACE:
                            self.takePhoto()

                    if e.type == pygame.MOUSEBUTTONUP and e.button == self.MOUSE_BUTTON_1:
                        self.takePhoto()

                # draw frame
                self.screen.blit(self.img, (0,0))

                # Fondo para las letras
                pygame.draw.rect(self.screen, self.COLOR_FONDO_LETRA, [0, 0, self.WIDTH, 30], 0)

                # Texto
                texto = self.myfont.render(self.pasos[self.i], False, self.COLOR_LETRA)

                self.screen.blit(texto,(5,5))
                
                pygame.display.flip()
                # grab next frame    
                self.img = self.webcam.get_image()
        except SystemExit:
            pygame.quit()


cam = Camara()
cam.open()