""" importaciones de la libreria pygame , y sys que me permite cerrar la ventana """
import pygame,sys 
from pygame.locals import *
from random import randint
 

""" metodo init que me permite arrancar la ventana ."""
pygame.init()

""" amboos implementan colores RGB (0 a 255 #enteros), uno con la libreria pygame"""
color =(200,80,100) 
colorpoly =(0,150,175) 
colorlinea = pygame.Color(0,150,175)
colorFondo = pygame.Color(255,255,255)

fuente = pygame.font.SysFont("Arial",40)

"""se crea un objeto tipo pygame y se envia una titulo de la ventana """ 
ventana = pygame.display.set_mode((800,475))
pygame.display.set_caption("space wars")
#pygame.draw.circle(ventana, color, (200,200),20)
#pygame.draw.rect(ventana, color,(200,100,25,25))

#tuplaPoly=((140,100),(200,100),(200,50),(140,50),(250,75),(230,85),(220,80))
#pygame.draw.polygon(ventana, colorpoly,tuplaPoly)

     
#cargar imagen 
nave = pygame.image.load("img/navenegraversion1.0.png")
navedos = pygame.image.load("img/mship1version2.0.png")

posX,posY=150,100
posx2, posy2=200,225

#variables de movimiento 
vel =0.02
derecha=True
vel2 = 10
rigth=True
auxTime=1
""" bucle infinito que mantiene abierta la ventana y actualizada"""
while True: 

    #color dr fondo     
    ventana.fill(colorFondo)
    pygame.draw.line(ventana, colorlinea, (10,210),(790,210),8)

    #dibuja las naves en la ventana 
    ventana.blit(nave,(posX,posY))
    ventana.blit(navedos,(posx2,posy2))
    
    tiempo = pygame.time.get_ticks()/1000 
    if auxTime == tiempo :
        auxTime +=1
        print(tiempo)
        
    contador = fuente.render("Tiempo es : "+str(tiempo), 0, color)
    ventana.blit(contador,(250,0))
    

    #primera nave  que se mueve sola      
    if rigth == True:
        if posy2 < 430  :
            posy2 += vel
        else: 
            rigth=False
    else :
        if posy2 > 1  :
            posy2 -=vel
        else :
            rigth =True
             
             
    for eventoX in pygame.event.get():
        if eventoX.type == QUIT:
            pygame.quit()
            sys.exit()  
        # segunda nave con las teclas A y D ..     
        elif eventoX.type == pygame.KEYDOWN :
            if eventoX.key == K_a :
                posx2 -= vel2
            elif eventoX.key == K_d :
                posx2 +=vel2
            
    #print( pygame.mouse.get_pos() ) 
    #posX , posY = pygame.mouse.get_pos()
    posX=posX-50    
    posY=posY-50     
    
                        
    pygame.display.update()
