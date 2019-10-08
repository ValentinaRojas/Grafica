import pygame,sys
import random

#constante no cambian
ANCHO=640
ALTO=480
NEGRO=[0,0,0]
BLANCO=[255,255,255]
AZUL=[0,0,255]
ROJO=[255,0,0]

#clases
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        '''Constructor'''
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,50])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.rect.x=100
        self.rect.y=150

if __name__ == '__main__':
    #Seccion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    jugadores=pygame.sprite.Group()

    #Inicializar jugador
    j=Jugador()
    jugadores.add(j)


    #ciclo principal
    while True:
        #seccion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        jugadores.update()


        #Desplegar graficos
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
