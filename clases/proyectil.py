import pygame
"""clases encargada de la logica de los proyectiles del jugador  y los invasores 
a traves de los objetos que recibe en parametros.  
posiciones en X, Y  .. 
ruta de la imagen ,  True : si es el jugador , False : si es el enemigo 
"""
class proyectiles(pygame.sprite.Sprite):
    
    def __init__(self,posX, posY,ruta,personaje):
        pygame.sprite.Sprite.__init__(self)        

        self.imagenProyectil = pygame.image.load(ruta)
        
        self.rect = self.imagenProyectil.get_rect()
        
        self.velocidadDisparo =0
        
        self.rect.top = posY
        self.rect.left =posX
        
        self.disparoPersonaje = personaje
        
    def trayectoria(self):
        if self.disparoPersonaje == True :  
            #disparo del jugador 
            self.velocidadDisparo=18
            self.rect.top = self.rect.top - self.velocidadDisparo
        else :
            #disparo del enemigo
            self.velocidadDisparo=2
            self.rect.top = self.rect.top + self.velocidadDisparo

        
    def dibujar(self,superficie):
        superficie.blit(self.imagenProyectil, self.rect)
        