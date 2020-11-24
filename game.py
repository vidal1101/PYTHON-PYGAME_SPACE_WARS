"""importaciones de las librerias de python
,pygame para la creacion del video juego , randon para implementar 
logica de numeros al azar en los disparos de los 
enemigos  """
import pygame,sys 
from pygame.locals import *
from random import randint
#importaciones de las clases 
from clases.nave import naveEspacial 
from clases.invasor import invasor
from clases.proyectil import proyectiles
from clases import  database

#variables globales 
ancho=900
alto=500
listaEnemigos =[]

pygame.init()
pygame.display.set_caption("Space Wars   V.1.0")
venta = pygame.display.set_mode((ancho,alto))


"""detener la acciones del jugador cuando pierda el jugador """
def detenerTodo():
    for enemigo in listaEnemigos:  
        for dispar in enemigo.listaDisparos:
            enemigo.listaDisparos.remove(dispar)
    invasor.conquista=False     
            
            
            
            

"""metodo que carga los enemigos , en lista y las recorre en los arrays """
def cargarEnemigos():
    #nave padre 
    posenemigoX=300      
    for x in range(1,2):
        #clase de invasores , se le envia las posiciones de X,Y la distancia entre cada nave 
        enemigo = invasor(posenemigoX, 60, 100, "img/otherNaveVersionGrande.png" , "img/otherNaveVersionGrande.png")
        listaEnemigos.append(enemigo)
        posenemigoX = posenemigoX + 300  
    
    #primer lista de enemigos 
    posenemigoX=80
    for x in range(1,6):
        enemigo = invasor(posenemigoX, -20, 50, "img/inva2A.png" , "img/inva2B.png")
        listaEnemigos.append(enemigo)
        posenemigoX = posenemigoX + 170
     
    #segunda lista mas arriba     
    posenemigoX=170
    for x in range(1,4):
        #clase de invasores , se le envia las posiciones de X,Y la distancia entre cada nave 
        enemigo = invasor(posenemigoX, -120, 60, "img/n1m.png" , "img/n2m.png")
        listaEnemigos.append(enemigo)
        posenemigoX = posenemigoX + 170  
    #tercera lista     
    posenemigoX=80
    for x in range(1,6):
        #clase de invasores , se le envia las posiciones de X,Y la distancia entre cada nave 
        enemigo = invasor(posenemigoX, -220, 50, "img/n3m.png" , "img/n4m.png")
        listaEnemigos.append(enemigo)
        posenemigoX = posenemigoX + 170  
    #cuarta fila       
    posenemigoX=100
    for x in range(1,5):
        #clase de invasores , se le envia las posiciones de X,Y la distancia entre cada nave 
        enemigo = invasor(posenemigoX, -320, 60, "img/inva2A.png" , "img/n5m.png")
        listaEnemigos.append(enemigo)
        posenemigoX = posenemigoX + 200  
    #Quinta fila 
    posenemigoX=150       
    for x in range(1,4):
        #clase de invasores , se le envia las posiciones de X,Y la distancia entre cada nave 
        enemigo = invasor(posenemigoX, -420, 60, "img/n4m.png" , "img/n1m.png")
        listaEnemigos.append(enemigo)
        posenemigoX = posenemigoX + 210
    #sexta fila 
    posenemigoX=200      
    for x in range(1,3):
        #clase de invasores , se le envia las posiciones de X,Y la distancia entre cada nave 
        enemigo = invasor(posenemigoX, -520, 60, "img/n1m.png" , "img/n2m.png")
        listaEnemigos.append(enemigo)
        posenemigoX = posenemigoX + 220    
    #nave padre 


     
""" menu principal del juego """
def menu():
    
    fondoMenu = pygame.image.load("img/MENUF2.png")
    
    menu=True
    color =(180,225,210) 
    colorFuente = (255,60,50)
    miFuenteSystem = pygame.font.SysFont("Arial",40)
    miFuenteSystem2 = pygame.font.SysFont("ravie",110)
    textMenu = miFuenteSystem.render("Menu" ,0,color)
    textJugar =miFuenteSystem.render("Jugar" ,0,colorFuente)
    textOpciones =miFuenteSystem.render("Datos Juego" ,0,colorFuente)
    textAyuda =miFuenteSystem.render("Ayuda" ,0,colorFuente)
    textSpace =miFuenteSystem2.render("Space" ,0,colorFuente)
    textWars =miFuenteSystem2.render("Wars" ,0,colorFuente)
    
    icon = pygame.image.load("img/cohete.png")
    pygame.display.set_icon(icon)
    
    while menu: 
        click=True
        venta.fill((0,0,0))
        venta.blit(fondoMenu,(0,0))
        venta.blit(textMenu,(100,20))
        
        
        mx , my = pygame.mouse.get_pos()
        
        button1= pygame.Rect(50,100,200,50)
        button2= pygame.Rect(50,200,200,50)
        button3= pygame.Rect(50,300,200,50)
        
        if button1.collidepoint((mx,my)):
            if click:
                Space_Wars()
        if button2.collidepoint((mx,my)):
            if click:
                datos()
        if button3.collidepoint((mx,my)):
            if click:
                ayuda()
                
        pygame.draw.rect(venta, color,button1)
        pygame.draw.rect(venta, color,button2)
        pygame.draw.rect(venta, color,button3)
        venta.blit(textJugar,(100,100))
        venta.blit(textOpciones,(60,200))
        venta.blit(textAyuda,(100,300))
        venta.blit(textSpace,(350,50))
        venta.blit(textWars,(450,175))
        
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit() 
                if event.key == K_END: 
                    Space_Wars()    
            if event.type == MOUSEBUTTONDOWN: 
                if event.Button == 1:
                    click=True     
        
        
        pygame.display.update()  
 
  
""" se muestra los datos de los jugador"""       
def datos():
    
    conexion = database
    
    values = conexion.mostrarDatos()
    
    datos=True
    color =(200,200,200) 
    color2 =(100,200,200) 
    colorFuente = (255,60,50)
    miFuenteSystem = pygame.font.SysFont("Arial",40)
    textMenu = miFuenteSystem.render("Datos de las Rondas" ,0,color)
    datosJuego = miFuenteSystem.render("#,Bajas,disparos" ,0,color2)
    textatras=miFuenteSystem.render("Atras (Esc)" ,0,color)
    
    icon = pygame.image.load("img/cohete.png")
    pygame.display.set_icon(icon)
    
    while datos: 
        
        click=True
        venta.fill((0,0,0))
        venta.blit(textMenu,(300,10))
        venta.blit(textatras,(5,458))
        venta.blit(datosJuego,(100,50))
        
        
        posY=110
        posx=100
        posicion=0
        for i in values:
            
             
            if posY==430 and posicion > 7 and posicion < 14 :
                posx=325
                posY=110
                datosjugador=miFuenteSystem.render(""+str(i)+"" ,0,color)
                venta.blit(datosjugador,(posx,posY))
                    
                datosjugador=miFuenteSystem.render(""+str(i)+"" ,0,color)
                venta.blit(datosjugador,(posx,posY))    
                posY=posY+40
                posicion += 1
            elif posY==430 and posicion > 14:
                posx=540
                posY=110
                datosjugador=miFuenteSystem.render(""+str(i)+"" ,0,color)
                venta.blit(datosjugador,(posx,posY))
                    
                datosjugador=miFuenteSystem.render(""+str(i)+"" ,0,color)
                venta.blit(datosjugador,(posx,posY))    
                posY=posY+40
                posicion += 1
                    
            else :
                datosjugador=miFuenteSystem.render(""+str(i)+"" ,0,color)
                venta.blit(datosjugador,(posx,posY))
                posY=posY+40
                posicion += 1
                  
      
       
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu()
                if event.key == K_s: 
                    pass    
                
        
        
        pygame.display.update()  
               
 


""" ayuda donde se ve los controles necesarios """ 
def ayuda():
    
    ayuda=True
    color =(200,200,200) 
    color2 =(100,200,200) 
    
    miFuenteSystem = pygame.font.SysFont("Arial",40)
    textMenu = miFuenteSystem.render("Controles" ,0,color2)
    
    textatras=miFuenteSystem.render("Atras (Esc)" ,0,color)
    
    fondoAyuda = pygame.image.load("img/Controles.png")
    fondoMenu = pygame.image.load("img/MENUF2.png")
    
    icon = pygame.image.load("img/cohete.png")
    pygame.display.set_icon(icon)
    
    while ayuda: 
       
        venta.fill((0,0,0))
        venta.blit(fondoMenu,(0,0))
        venta.blit(fondoAyuda,(220,50))
        venta.blit(textMenu,(380,10))
        venta.blit(textatras,(5,458))
        
        
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu()
                if event.key == K_s: 
                    pass    
                
        
        
        pygame.display.update()  
 
 
 
 
        
"""metodo que contendra la logica de juego"""
def Space_Wars():
    
   
    
    start_time=pygame.time.get_ticks()
    
    
    fondoJuego = pygame.image.load("img/galaxia.jpg")
    icon = pygame.image.load("img/cohete.png")
    pygame.display.set_icon(icon)
    pygame.mixer.music.load("sonidos/y2mate.com - Alunados - El poeta de la era espacial (8 bits)_blw6VUwXAMg.mp3")
    pygame.mixer.music.play(5)
    
    color =(200,200,200) 
    miFuenteSystem = pygame.font.SysFont("Arial",40)
    textofinal = miFuenteSystem.render("Gamer Over", 0, color)
    textoGanador = miFuenteSystem.render("VICTORIA" ,0,color)
    #objetos de las clases
    jugador = naveEspacial(ancho,alto)
    #enemigo = invasor(100,100)
    cargarEnemigos()
    
    #proyec = proyectiles(ancho/2, alto-30)
    
    #para saber si aun se esta jugando 
    enJuego = True
    juegoEnemigos = True
    starGame = True
    nuevaRonda=False
    
    fuenteVida = pygame.font.SysFont("Arial",40)
    menuReinicio = fuenteVida.render("Volver a Jugar (T)", 0, color)


    #para manejar los fps 
    fps = pygame.time.Clock()
    
    while starGame:
        
        #se crea el fondo de la ventana , la cantidad de fsp y tiempo de cambios de animaciones 
        venta.blit(fondoJuego,(0,0))
        fps.tick(60)
        tiempoCambio =   int((pygame.time.get_ticks()-start_time)/1000)


            
        for evento in pygame.event.get():
            if evento.type== QUIT:
                pygame.quit()
                sys.exit
                
            if enJuego ==True:
                #donde se hagna las colisiones y pierda reduzco la vida en -1
                if evento.type == pygame.KEYDOWN:
                    
                    #el jugador se mueve con varias opciones y dispara con 2 opciones 
                    if evento.key == K_LEFT or evento.key == K_a :
                        jugador.movimientoIzquierdo()
                            
                    elif evento.key == K_RIGHT or evento.key == K_d:   
                        jugador.movimientoDerecho()
                            
                    elif evento.key == K_SPACE or evento.key == K_RSHIFT: 
                        x, y = jugador.rect.center
                        jugador.disparar(x,y)
                    
                            
                else :
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == K_g:
                            enJuego=True
                            juegoEnemigos=True
                            menu()
                    
                         



        #lanza los proyectiles del jugador    
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(venta) 
                x.trayectoria()
                #borra los proyectiles del jugador 
                if x.rect.top < 10:
                    jugador.listaDisparo.remove(x)
                else : 
                    #justo aqui hago las colisiones objetos y borro el enemigo junto con el proyectil que lo tiro 
                    for enemigo in listaEnemigos:
                        if x.rect.colliderect(enemigo.rect) : 
                            listaEnemigos.remove(enemigo) 
                            jugador.listaDisparo.remove(x)
                            print("puntos por baja")
                            jugador.enemigosDerribados +=1
                           
                            #metodo adicional de la base de datos para guardar puntuacion
        
        jugador.dibujar(venta)
        
               
        #lanza los proyectiles de los enemigos
        if juegoEnemigos == True :
            
            if len(listaEnemigos)>0 :
                for enemigo in listaEnemigos :
                    enemigo.comportamiento(tiempoCambio,True)
                    enemigo.dibujar(venta)
                    
                    if enemigo.rect.colliderect(jugador.rect):
                        #print("golpeo al jugador: llamo a destruccion ")
                        datosFinales = miFuenteSystem.render("Disparos : "+str(jugador.cantidadDisparos)+", Bajas : "+str(jugador.enemigosDerribados)+"", 0, color)
                        jugador.destruccion()
                        enemigo.comportamiento(tiempoCambio,False)
                        enJuego=False
                        nuevaRonda=True
                        juegoEnemigos=False
                        detenerTodo()
                        
            
                    #lista de disparos de los enemigos 
                    if len(enemigo.listaDisparos)>0:
                        for x in enemigo.listaDisparos:
                            x.dibujar(venta) 
                            x.trayectoria()
                            #borra los proyectiles 
                            if x.rect.colliderect(jugador.rect):
                                datosFinales = miFuenteSystem.render("Disparos : "+str(jugador.cantidadDisparos)+" , Bajas : "+str(jugador.enemigosDerribados)+"", 0, color)

                                jugador.destruccion()
                                enemigo.comportamiento(tiempoCambio,False)
                                enJuego=False
                                nuevaRonda=True
                                juegoEnemigos=False
                                detenerTodo()
                                
                                
                            
                            if x.rect.top >900:
                                enemigo.listaDisparos.remove(x)
                            else :
                                for disparo in jugador.listaDisparo:
                                    if x.rect.colliderect(disparo.rect):
                                        jugador.listaDisparo.remove(disparo)
                                        enemigo.listaDisparos.remove(x)
            else :
                #print('gano el jugador')
                pygame.mixer.music.fadeout(1000)
                datosFinales = miFuenteSystem.render("Disparos : "+str(jugador.cantidadDisparos)+" , Bajas : "+str(jugador.enemigosDerribados)+"", 0, color)
                jugador.victoria()
                venta.blit(textoGanador,(373,195))
                detenerTodo()
                nuevaRonda=True
                juegoEnemigos=False
                
                
                
                
           
        # cuando pierde y se le muestra unos datos y puede volver a reiniciar o ir al menu    
        if enJuego==False :
            
            pygame.mixer.music.fadeout(3000)
            
            venta.blit(textofinal,(375,300))
            venta.blit(menuReinicio,(360,100))
            
            venta.blit(datosFinales,(300,200))
            
            for evento in pygame.event.get():
                if nuevaRonda == True:
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == K_t:
                            
                            cargarEnemigos()
                            jugador.reinicio()
                            enJuego=True
                            juegoEnemigos=True
                            pygame.mixer.music.play(5)
                        elif evento.key == K_p:
                            
                            for x in listaEnemigos:
                                listaEnemigos.remove(x)
                                for enemig in  enemigo.listaDisparos: 
                                    enemigo.listaDisparos.remove(enemig) 
                                    
                            enJuego=True
                            juegoEnemigos=True
                            detenerTodo()
                            menu() 
                            
                            
         
        #datos cuando gana y vuelve a  reiniciar el juego                 
        if len(listaEnemigos)>0 :
            pass
        else :
            
            venta.blit(textoGanador,(373,195))
            venta.blit(menuReinicio,(360,100))
            
            venta.blit(datosFinales,(300,300))
             
            for evento in pygame.event.get():
                if nuevaRonda == True:
                    
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == K_t: 
                            
                            jugador.reinicio()
                            enJuego=True
                            juegoEnemigos=True
                            pygame.mixer.music.play(5)
                            cargarEnemigos() 
                
            
        
                
            
        
            

        pygame.display.update()        






"""se llama el metodo principal  """
menu()



