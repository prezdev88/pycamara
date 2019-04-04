# sudo pip3 install pygame

import pygame.camera
import pygame.image
import sys

pygame.init()
pygame.camera.init()

cameras = pygame.camera.list_cameras()

print("Using camera %s ..." % cameras[0])

webcam = pygame.camera.Camera(cameras[0])

webcam.start()

# grab first frame
img = webcam.get_image()

WIDTH = img.get_width()
HEIGHT = img.get_height()

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption("pyGame Camera View")

pasos = list()

pasos.append("CARNET_FRONT")
pasos.append("CARNET_BACK")
pasos.append("LICENCIA_FRONT")
pasos.append("LICENCIA_BACK")
pasos.append("SELFIE")

i = 0

white = (255, 255, 255) 
# blue = (0, 0, 128) 
# green = (0, 255, 0) 

pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            sys.exit()
        
        if e.type==pygame.KEYDOWN:
            if e.key == 13:
                print("ENTER")
                paso = pasos[i]
                pygame.image.save(img, paso+".png")
                i += 1

                if i == 5:
                    sys.exit()

    # draw frame
    screen.blit(img, (0,0))
    # Texto
    textsurface = myfont.render(pasos[i], False, white)

    screen.blit(textsurface,(0,0))

    pygame.display.flip()
    # grab next frame    
    img = webcam.get_image()