import pygame
from clases.proyectil import proyectiles
from clases import database
conexion = database
"""
clase de la nave espacial del jugador , y se mueve de derecha y izquierda . 
recibe el anho y alto de la ventana , para pos en X,Y .. en la mitad de la ventana , 

"""


class naveEspacial(pygame.sprite.Sprite):
    """clases de la nave """
    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        #cargar las imagenes
        self.ImagenNave = pygame.image.load("img/mship1version2.0.png")
        self.ImagenDestruccion = pygame.image.load("img/explosionversion2.png")
        
        self.listaImagenes=[self.ImagenNave,self.ImagenDestruccion]
        self.posImagen =0
        self.imagenJugador = self.listaImagenes[self.posImagen]
        
        self.rect = self.imagenJugador.get_rect()
        self.rect.centerx = ancho / 2
        self.rect.centery = alto-60
        
        self.listaDisparo =[]
        
        self.cantidadDisparos=0
        self.enemigosDerribados=0

        self.Vida = True
        
        self.velocidad =25
    
        self.sonidoDisparo = pygame.mixer.Sound("sonidos/008827459_prev.wav")
        self.sonidoExplosion = pygame.mixer.Sound("sonidos/001105163_prev.wav")
        self.sonidoVictoria = pygame.mixer.Sound("sonidos/victory-sonic.wav")
    
    """ nuevos cambios """
    def movimientoDerecho(self):
        self.rect.right += self.velocidad
        self.__movimiento()
        
    def movimientoIzquierdo(self):
        self.rect.left -= self.velocidad
        self.__movimiento()
        
    #metodo privado    
    def __movimiento(self): 
        if self.Vida==True:
            if self.rect.left ==0:
                self.rect.left =30
            elif self.rect.right==890:
                self.rect.right=870
                 
        
        
    def disparar(self,x,y):
        if self.Vida==True:
            x=x-18
            miProyectil = proyectiles(x,y,"img/DisparoJugador.png",True)
            self.listaDisparo.append(miProyectil)
            self.sonidoDisparo.play()
            self.cantidadDisparos = self.cantidadDisparos +1
        #print(self.cantidadDisparos)
    
    #cuando el jugaddor pierde     
    def destruccion(self):
        self.sonidoExplosion.play()
        self.Vida=False
        self.velocidad=0
        self.posImagen=1
        self.imagenJugador = self.listaImagenes[self.posImagen]
        print(self.enemigosDerribados)
        print(self.cantidadDisparos)
        msj = conexion.guardarJugadas(self.cantidadDisparos, self.enemigosDerribados)
        print(str(msj))
        self.cantidadDisparos=0
        self.enemigosDerribados=0
    
    #cuando el jugador gana 
    def victoria(self):
        self.sonidoVictoria.play()
        self.velocidad=0
        self.Vida=False        
        conexion.guardarJugadas(self.cantidadDisparos, self.enemigosDerribados)
        self.cantidadDisparos=0
        self.enemigosDerribados=0


    def reinicio(self):
        self.posImagen=0
        self.imagenJugador = self.listaImagenes[self.posImagen]
        self.Vida=True
        self.velocidad=25
        
    
    def dibujar(self,superficie):
        superficie.blit(self.imagenJugador, self.rect)  
