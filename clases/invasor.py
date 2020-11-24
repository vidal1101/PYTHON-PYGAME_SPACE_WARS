import pygame
from random import randint
from clases.proyectil import proyectiles
"""
clase de los invasores , llamada desde el metodo cargarEnemigos() , donde recibe las posiciones X,Y ..
distancia en lateral de cada nave . y 2 imagenes que cambio a traves de un contador  
"""

class invasor(pygame.sprite.Sprite):
    
    def __init__(self,posX, posY,distancia,imagen1, imagen2):
        pygame.sprite.Sprite.__init__(self)        

        self.invasorA = pygame.image.load(imagen1)
        self.invasorB = pygame.image.load(imagen2)
        
        self.listaImagenes =[self.invasorA , self.invasorB]
        self.posImagen =0
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()
        
        self.listaDisparos =[]
        self.velocidad =2
        self.rect.top = posY
        self.rect.left =posX
        
        # cantidad de disparos con el randint . entre mas alto sea el numero mas disparos seran 
        self.rangoDisparo =2
        
        self.tiempoCambio =1
        
        self.derecha=True
        self.contador=0
        self.maximodescenso = self.rect.top + 20
        
        self.limiteDerecha = posX + distancia
        self.limiteIzquierda = posX - distancia
        
        self.conquista=None
      
      
    def dibujar(self,superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)
      
    # ciclo padre de las naves espaciales    
    def comportamiento(self,tiempo,conquistado):
        
        if conquistado==True :
            
            self.__movivmiento()
            
            self.__ataque()
            if self.tiempoCambio == tiempo:
                self.posImagen +=1
                self.tiempoCambio+=1
                
                if self.posImagen > len(self.listaImagenes)-1:
                    self.posImagen=0
        else :   
            print('conquista es false ')         
    
    
    def __movivmiento(self):
        if self.contador<2:
            self.__movivmientoLateral()
        else : 
            self.__descenso()     
            
    def __descenso(self): 
        if self.maximodescenso == self.rect.top :
            self.contador=0
            self.maximodescenso = self.rect.top + 40
        else : 
            self.rect.top +=1   
           
    
    def __movivmientoLateral(self):
        if self.derecha ==True:
            self.rect.left = self.rect.left + self.velocidad
            if self.rect.left > self.limiteDerecha:
                self.derecha =False
                
                self.contador +=1
        else : 
            self.rect.left = self.rect.left -self.velocidad
            if self.rect.left < self.limiteIzquierda :
                self.derecha=True       
        
        
    def __ataque(self):
        #limito los tiempos aleatorios de cada disparo 
        if (randint(0,1000)<self.rangoDisparo):
            self.__disparo()
        
    def __disparo(self):
        x,y = self.rect.center
        x=x+5
        miProyectil = proyectiles(x,y,"img/DisparoEnemigo.png",False)
        self.listaDisparos.append(miProyectil)
    
