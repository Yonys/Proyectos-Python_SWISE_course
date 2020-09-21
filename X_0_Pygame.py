
import pygame 
import sys

pygame.init()


# Pantalla
ancho = 800
altura = 600
pantalla = pygame.display.set_mode((ancho, altura))
# Título e ícono
pygame.display.set_caption("Bienvenido a jugar X-0")
icon = pygame.image.load("imagenes/Amapala.bmp") 
pygame.display.set_icon(icon)  # No funcionará dependiendo del tema que usen en su SO
x_imag = pygame.image.load("imagenes/x1.bmp") 
o_imag = pygame.image.load("imagenes/cero.bmp")
pantalla.blit(icon, (0, 0))
# se muestran lo cambios en pantalla
pygame.display.flip()

# resizing images 
#initiating_pantalladow = pygame.transform.scale(initiating_pantalladow, (width, height + 100)) 
x_imag = pygame.transform.scale(x_imag, (80, 80))
o_imag = pygame.transform.scale(o_imag, (80, 80))


#---------
class Tablero:
	def __init__(self):

		self.fil1 = 100
		self.fil2 = 200
		self.fil3 = 300
		self.cuadrado = 80
		self.col1 = 180
		self.col2 = 330
		self.col3 = 480

		self.titleHorz = 100
		self.titleVert = 10


		self.tablero = ["0","1","2","3","4","5","6","7","8","9"]
		#self.pregunta = pygame.draw.rect(pantalla, (255,255,255), (self.titleHorz ,self.titleVert ,530,70))

		self.cuadro1 = pygame.draw.rect(pantalla, (255,255,255), (self.col1,self.fil1,self.cuadrado,self.cuadrado))
		self.cuadro1_sinMarcar = True
		self.cuadro2 = pygame.draw.rect(pantalla, (255,255,255), (self.col2,self.fil1,self.cuadrado,self.cuadrado))
		self.cuadro2_sinMarcar = True
		self.cuadro3 = pygame.draw.rect(pantalla, (255,255,255), (self.col3,self.fil1,self.cuadrado,self.cuadrado))
		self.cuadro3_sinMarcar = True
	

		self.cuadro4 = pygame.draw.rect(pantalla, (255,255,255), (self.col1,self.fil2,self.cuadrado,self.cuadrado))
		self.cuadro4_sinMarcar = True
		self.cuadro5 = pygame.draw.rect(pantalla, (255,255,255), (self.col2,self.fil2,self.cuadrado,self.cuadrado))
		self.cuadro5_sinMarcar = True
		self.cuadro6 = pygame.draw.rect(pantalla, (255,255,255), (self.col3,self.fil2,self.cuadrado,self.cuadrado))
		self.cuadro6_sinMarcar = True

		self.cuadro7 = pygame.draw.rect(pantalla, (255,255,255), (self.col1,self.fil3,self.cuadrado,self.cuadrado))
		self.cuadro7_sinMarcar = True
		self.cuadro8 = pygame.draw.rect(pantalla, (255,255,255), (self.col2,self.fil3,self.cuadrado,self.cuadrado))
		self.cuadro8_sinMarcar = True
		self.cuadro9 = pygame.draw.rect(pantalla, (255,255,255), (self.col3,self.fil3,self.cuadrado,self.cuadrado))
		self.cuadro9_sinMarcar = True

	def marcar_casilla(self,pos, jugador):

		#if(not self.cuadro1_sinMarcar): print("No puede marcar")

		if self.cuadro1.collidepoint(pos) and self.cuadro1_sinMarcar:
			if(jugador==1):
				pantalla.blit(x_imag, (self.col1, self.fil1)) 
				self.tablero[1] = "X"
			else:
				pantalla.blit(o_imag,(self.col1, self.fil1)) 
				self.tablero[1] = "0"
			self.cuadro1_sinMarcar = False 
			 

		if self.cuadro2.collidepoint(pos) and self.cuadro2_sinMarcar:
			if(jugador==1):
				pantalla.blit(x_imag, (self.col2, self.fil1)) 
				self.tablero[2] = "X"
			else:
				pantalla.blit(o_imag, (self.col2, self.fil1))
				self.tablero[2] = "0"
			self.cuadro2_sinMarcar = False 

		if self.cuadro3.collidepoint(pos) and self.cuadro3_sinMarcar:
			if(jugador==1):
				pantalla.blit(x_imag, (self.col3, self.fil1)) 
				self.tablero[3] = "X"
			else:
				pantalla.blit(o_imag, (self.col3, self.fil1)) 
				self.tablero[3] = "0"
			self.cuadro3_sinMarcar = False 

		if self.cuadro4.collidepoint(pos) and self.cuadro4_sinMarcar:
			if(jugador==1):
				pantalla.blit(x_imag, (self.col1, self.fil2)) 
				self.tablero[4] = "X"
			else:
				pantalla.blit(o_imag, (self.col1, self.fil2)) 
				self.tablero[4] = "0"
			self.cuadro4_sinMarcar = False 

		if self.cuadro5.collidepoint(pos) and self.cuadro5_sinMarcar:
			#pygame.draw.rect(pantalla, (255, 0, 0), (325, 325, 50,50))
			if(jugador==1):
				pantalla.blit(x_imag, (self.col2, self.fil2)) 
				self.tablero[5] = "X"
			else:
				pantalla.blit(o_imag, (self.col2, self.fil2))
				self.tablero[5] = "0"
			self.cuadro5_sinMarcar = False 

		if self.cuadro6.collidepoint(pos) and self.cuadro6_sinMarcar:
			#pygame.draw.rect(pantalla, (255, 0, 0), (525, 325, 50,50))
			if(jugador==1):
				pantalla.blit(x_imag, (self.col3, self.fil2)) 
				self.tablero[6] = "X"
			else:
				pantalla.blit(o_imag, (self.col3, self.fil2)) 
				self.tablero[6] = "0"
			self.cuadro6_sinMarcar = False 

		if self.cuadro7.collidepoint(pos) and self.cuadro7_sinMarcar:
			#pygame.draw.rect(pantalla, (255, 0, 0), (125, 475, 50,50))
			
			if(jugador==1):
				pantalla.blit(x_imag, (self.col1, self.fil3)) 
				self.tablero[7] = "X"
			else:
				pantalla.blit(o_imag,  (self.col1, self.fil3)) 
				self.tablero[7] = "0"
			self.cuadro7_sinMarcar = False 

		if self.cuadro8.collidepoint(pos) and self.cuadro8_sinMarcar:
			#pygame.draw.rect(pantalla, (255, 0, 0), (325, 475, 50,50))
			if(jugador==1):
				pantalla.blit(x_imag, (self.col2, self.fil3)) 
				self.tablero[8] = "X"
			else:
				pantalla.blit(o_imag, (self.col2, self.fil3)) 
				self.tablero[8] = "0"
			self.cuadro8_sinMarcar = False 

		if self.cuadro9.collidepoint(pos) and self.cuadro9_sinMarcar:
			#pygame.draw.rect(pantalla, (255, 0, 0), (525, 475, 50,50))
			if(jugador==1):
				pantalla.blit(x_imag, (self.col3, self.fil3)) 
				self.tablero[9] = "X"
			else:
				pantalla.blit(o_imag, (self.col3, self.fil3))  
				self.tablero[9] = "0"
			self.cuadro9_sinMarcar = False 


	def buscar_ganador(self):
		"""
		Método que refresa el estado del juego, el cual pueder ser: Hay ganador,
		empate o que puede continuar jugando"""
		color = pygame.Color(200,10,12)
		if((self.tablero[1] == self.tablero[2]) and (self.tablero[2] == self.tablero[3])):
			#pygame.draw.lin
			pygame.draw.line(pantalla, color, (self.col1 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil1+self.cuadrado/2)) 
			return 1
		elif (self.tablero[4] == self.tablero[5] and self.tablero[5] == self.tablero[6]):
			pygame.draw.line(pantalla, color, (self.col1 +self.cuadrado/2, self.fil2 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil2+self.cuadrado/2)) 
			return 1 

		elif(self.tablero[7] == self.tablero[8] and self.tablero[8] == self.tablero[9]):
			pygame.draw.line(pantalla, color, (self.col1 +self.cuadrado/2, self.fil3 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
			# ------- Comprobando lo anterior pero para las columnas------------------
		elif (self.tablero[1] == self.tablero[4] and self.tablero[4] == self.tablero[7]):
			pygame.draw.line(pantalla, color, (self.col1 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col1+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1 

		elif (self.tablero[2] == self.tablero[5] and self.tablero[5] == self.tablero[8]):
			pygame.draw.line(pantalla, color, (self.col2 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col2+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
		elif (self.tablero[3] == self.tablero[6] and self.tablero[6] == self.tablero[9]):
			pygame.draw.line(pantalla, color, (self.col3 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
		#------------- Buscando ganador en las diagonales ---------------------------
		elif (self.tablero[1] == self.tablero[5] and self.tablero[5] == self.tablero[9]):
			pygame.draw.line(pantalla, color, (self.col1 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
		elif(self.tablero[3] == self.tablero[5] and self.tablero[5] == self.tablero[7]):
			pygame.draw.line(pantalla, color, (self.col3 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col1+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
			#Buscando empate
		elif (self.tablero[1] != '1' and self.tablero[2] != '2' and self.tablero[3] != '3' and self.tablero[4] != '4' and self.tablero[5] != '5' and self.tablero[6] != '6'  and self.tablero[7] != '7' and self.tablero[8] != '8' and self.tablero[9] != '9'):
			return 0

		else:
			return -1 # En caso de no haber empate ni ganador entonces se puede seguir jugando




class Partida:
	def __init__(self, fil3, cuadrado):
		fil3 = fil3 + cuadrado
		self.volverJugar = pygame.draw.rect(pantalla, (255,255,255), (240,fil3 + 30,120,30))
		self.salir = pygame.draw.rect(pantalla, (255,255,255), (380,fil3 +30,120,30))
		
		miFuente1 = pygame.font.SysFont("Arial",18)
		self.textJugar = miFuente1.render("Reiniciar" , 12, (2,2,120))
		self.textSalir = miFuente1.render("Salir" , 12, (2,2,120))

		pantalla.blit(self.textJugar,(263, fil3 + 35))
		pantalla.blit(self.textSalir,(422, fil3 + 35))




        
tabler = Tablero()
#tabler
jugador1 = True
nombre = "yonys"
miFuente = pygame.font.SysFont("comic sans serif",30)
miTexto = miFuente.render("Jugador 1: X" , 3, (5,30,100))
miTexto1 = miFuente.render("Jugador 2: 0" , 3, (5,30,100))

miFuente1 = pygame.font.SysFont("comic sans serif",50)
ganador = miFuente1.render("== FELICIDADES  HA GANADO ==" , 0, (100,0,0))
#ganador2 = miFuente1.render(" FELICIDADES JUGADOR 2 HA GANADO " , 0, (100,0,0))
empate = miFuente1.render(" ===== EMPATE ===== " , 0, (100,0,0))
#(100,50,530,50)

# Controlador del while para apertura y cerradura de la ventana
running = True
estado = -1
# Ciclo de repetición del juego
while running:
    for event in pygame.event.get():  # <-- Recolector de eventos que suceden en CADA 
                                      #     iteración del while
        

        # # Cerrar el juego cuando el evento recibido sea el de salir de la ventana
        # if event.type == pygame.QUIT: 
        #     running = False
        # Cerrar el juego cuando el evento recibido sea el de salir de la ventana
        pantalla.blit(miTexto,(tabler.col1,tabler.titleVert + 10))
        pantalla.blit(miTexto1,(tabler.col1,tabler.titleVert + 40))
        if event.type == pygame.QUIT: 
            running = False

        if(jugador1):
        	if event.type == pygame.MOUSEBUTTONUP:
         		pos = pygame.mouse.get_pos()
         		tabler.marcar_casilla(pos,1)
         		jugador1 = False
        else:
        	if event.type == pygame.MOUSEBUTTONUP:
         		pos = pygame.mouse.get_pos()
         		tabler.marcar_casilla(pos,2)
         		jugador1 = True


    
        partida = Partida(tabler.fil3 , tabler.cuadrado)
        if event.type == pygame.MOUSEBUTTONUP:
        	pos = pygame.mouse.get_pos()
         		#tabler.marcar_casilla(pos,1)
	        if partida.salir.collidepoint(pos):
	        	running = False
	        if partida.volverJugar.collidepoint(pos):
	        	pantalla.blit(icon, (0, 0))
	        	tabler = Tablero()
	        	pygame.display.update()
	        	running = True
        
        estado = tabler.buscar_ganador()
        if(estado!=-1):
	        if(estado == 0):
	        	pantalla.blit(empate,(tabler.col1, tabler.fil3 + 170))

	        else:
		            pantalla.blit(ganador,(tabler.col1-90, tabler.fil3 + 170))

		      




	        





		    	        	

      


    # Red, Green, Blue
    #screen.fill((160, 0, 0))
    pygame.display.update()    

   