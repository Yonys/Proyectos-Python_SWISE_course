
import pygame 
import sys

pygame.init()


# Pantalla
ancho = 800
altura = 600
win = pygame.display.set_mode((ancho, altura))
# Título e ícono
pygame.display.set_caption("Bienvenido a jugar X-0")
icon = pygame.image.load("Amapala.bmp") 
pygame.display.set_icon(icon)  # No funcionará dependiendo del tema que usen en su SO
x_imag = pygame.image.load("x1.bmp") 
o_imag = pygame.image.load("cero.bmp")
win.blit(icon, (0, 0))
# se muestran lo cambios en pantalla
pygame.display.flip()

# resizing images 
#initiating_window = pygame.transform.scale(initiating_window, (width, height + 100)) 
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
		#self.pregunta = pygame.draw.rect(win, (255,255,255), (self.titleHorz ,self.titleVert ,530,70))

		self.first = pygame.draw.rect(win, (255,255,255), (self.col1,self.fil1,self.cuadrado,self.cuadrado))
		self.first_sinMarcar = True
		self.second = pygame.draw.rect(win, (255,255,255), (self.col2,self.fil1,self.cuadrado,self.cuadrado))
		self.second_sinMarcar = True
		self.third = pygame.draw.rect(win, (255,255,255), (self.col3,self.fil1,self.cuadrado,self.cuadrado))
		self.third_sinMarcar = True
	

		self.fourth = pygame.draw.rect(win, (255,255,255), (self.col1,self.fil2,self.cuadrado,self.cuadrado))
		self.fourth_sinMarcar = True
		self.fifth = pygame.draw.rect(win, (255,255,255), (self.col2,self.fil2,self.cuadrado,self.cuadrado))
		self.fifth_sinMarcar = True
		self.sixth = pygame.draw.rect(win, (255,255,255), (self.col3,self.fil2,self.cuadrado,self.cuadrado))
		self.sixth_sinMarcar = True

		self.seventh = pygame.draw.rect(win, (255,255,255), (self.col1,self.fil3,self.cuadrado,self.cuadrado))
		self.seventh_sinMarcar = True
		self.eighth = pygame.draw.rect(win, (255,255,255), (self.col2,self.fil3,self.cuadrado,self.cuadrado))
		self.eighth_sinMarcar = True
		self.ninth = pygame.draw.rect(win, (255,255,255), (self.col3,self.fil3,self.cuadrado,self.cuadrado))
		self.ninth_sinMarcar = True

	def marcar_casilla(self,pos, jugador):

		#if(not self.first_sinMarcar): print("No puede marcar")

		if self.first.collidepoint(pos) and self.first_sinMarcar:
			if(jugador==1):
				win.blit(x_imag, (self.col1, self.fil1)) 
				self.tablero[1] = "X"
			else:
				win.blit(o_imag,(self.col1, self.fil1)) 
				self.tablero[1] = "0"
			self.first_sinMarcar = False 
			 

		if self.second.collidepoint(pos) and self.second_sinMarcar:
			if(jugador==1):
				win.blit(x_imag, (self.col2, self.fil1)) 
				self.tablero[2] = "X"
			else:
				win.blit(o_imag, (self.col2, self.fil1))
				self.tablero[2] = "0"
			self.second_sinMarcar = False 

		if self.third.collidepoint(pos) and self.third_sinMarcar:
			if(jugador==1):
				win.blit(x_imag, (self.col3, self.fil1)) 
				self.tablero[3] = "X"
			else:
				win.blit(o_imag, (self.col3, self.fil1)) 
				self.tablero[3] = "0"
			self.third_sinMarcar = False 

		if self.fourth.collidepoint(pos) and self.fourth_sinMarcar:
			if(jugador==1):
				win.blit(x_imag, (self.col1, self.fil2)) 
				self.tablero[4] = "X"
			else:
				win.blit(o_imag, (self.col1, self.fil2)) 
				self.tablero[4] = "0"
			self.fourth_sinMarcar = False 

		if self.fifth.collidepoint(pos) and self.fifth_sinMarcar:
			#pygame.draw.rect(win, (255, 0, 0), (325, 325, 50,50))
			if(jugador==1):
				win.blit(x_imag, (self.col2, self.fil2)) 
				self.tablero[5] = "X"
			else:
				win.blit(o_imag, (self.col2, self.fil2))
				self.tablero[5] = "0"
			self.fifth_sinMarcar = False 

		if self.sixth.collidepoint(pos) and self.sixth_sinMarcar:
			#pygame.draw.rect(win, (255, 0, 0), (525, 325, 50,50))
			if(jugador==1):
				win.blit(x_imag, (self.col3, self.fil2)) 
				self.tablero[6] = "X"
			else:
				win.blit(o_imag, (self.col3, self.fil2)) 
				self.tablero[6] = "0"
			self.sixth_sinMarcar = False 

		if self.seventh.collidepoint(pos) and self.seventh_sinMarcar:
			#pygame.draw.rect(win, (255, 0, 0), (125, 475, 50,50))
			
			if(jugador==1):
				win.blit(x_imag, (self.col1, self.fil3)) 
				self.tablero[7] = "X"
			else:
				win.blit(o_imag,  (self.col1, self.fil3)) 
				self.tablero[7] = "0"
			self.seventh_sinMarcar = False 

		if self.eighth.collidepoint(pos) and self.eighth_sinMarcar:
			#pygame.draw.rect(win, (255, 0, 0), (325, 475, 50,50))
			if(jugador==1):
				win.blit(x_imag, (self.col2, self.fil3)) 
				self.tablero[8] = "X"
			else:
				win.blit(o_imag, (self.col2, self.fil3)) 
				self.tablero[8] = "0"
			self.eighth_sinMarcar = False 

		if self.ninth.collidepoint(pos) and self.ninth_sinMarcar:
			#pygame.draw.rect(win, (255, 0, 0), (525, 475, 50,50))
			if(jugador==1):
				win.blit(x_imag, (self.col3, self.fil3)) 
				self.tablero[9] = "X"
			else:
				win.blit(o_imag, (self.col3, self.fil3))  
				self.tablero[9] = "0"
			self.ninth_sinMarcar = False 


	def buscar_ganador(self):
		"""
		Método que refresa el estado del juego, el cual pueder ser: Hay ganador,
		empate o que puede continuar jugando"""
		color = pygame.Color(200,10,12)
		if((self.tablero[1] == self.tablero[2]) and (self.tablero[2] == self.tablero[3])):
			#pygame.draw.lin
			pygame.draw.line(win, color, (self.col1 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil1+self.cuadrado/2)) 
			return 1
		elif (self.tablero[4] == self.tablero[5] and self.tablero[5] == self.tablero[6]):
			pygame.draw.line(win, color, (self.col1 +self.cuadrado/2, self.fil2 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil2+self.cuadrado/2)) 
			return 1 

		elif(self.tablero[7] == self.tablero[8] and self.tablero[8] == self.tablero[9]):
			pygame.draw.line(win, color, (self.col1 +self.cuadrado/2, self.fil3 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
			# ------- Comprobando lo anterior pero para las columnas------------------
		elif (self.tablero[1] == self.tablero[4] and self.tablero[4] == self.tablero[7]):
			pygame.draw.line(win, color, (self.col1 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col1+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1 

		elif (self.tablero[2] == self.tablero[5] and self.tablero[5] == self.tablero[8]):
			pygame.draw.line(win, color, (self.col2 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col2+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
		elif (self.tablero[3] == self.tablero[6] and self.tablero[6] == self.tablero[9]):
			pygame.draw.line(win, color, (self.col3 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
		#------------- Buscando ganador en las diagonales ---------------------------
		elif (self.tablero[1] == self.tablero[5] and self.tablero[5] == self.tablero[9]):
			pygame.draw.line(win, color, (self.col1 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col3+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
		elif(self.tablero[3] == self.tablero[5] and self.tablero[5] == self.tablero[7]):
			pygame.draw.line(win, color, (self.col3 +self.cuadrado/2, self.fil1 + self.cuadrado/2), (self.col1+self.cuadrado/2, self.fil3+self.cuadrado/2)) 
			return 1
			#Buscando empate
		else:
			return -1 # En caso de no haber empate ni ganador entonces se puede seguir jugando



	


        
tabler = Tablero()
tabler
jugador1 = True
nombre = "yonys"
miFuente = pygame.font.SysFont("comic sans serif",30)
miTexto = miFuente.render("Jugador 1: X" , 3, (5,30,100))
miTexto1 = miFuente.render("Jugador 2: 0" , 3, (5,30,100))

miFuente1 = pygame.font.SysFont("comic sans serif",50)
ganador1 = miFuente1.render(" FELICIDADES JUGADOR 1 HA GANADO " , 0, (100,0,0))
ganador2 = miFuente1.render(" FELICIDADES JUGADOR 2 HA GANADO " , 0, (100,0,0))

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
        win.blit(miTexto,(tabler.col1,tabler.titleVert + 10))
        win.blit(miTexto1,(tabler.col1,tabler.titleVert + 40))
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


        estado = tabler.buscar_ganador()

        if(estado == 0):
        	print("Empate")
        	running = True 

        if(estado==1):
	        if(jugador1):
	            #print("Felicidades  jugador2.nombre   usted ha ganado")
	            win.blit(ganador2,(50, tabler.fil3 + 170))
	            pygame.display.update()  
	        else:
	            #print("FelICIDADES jugador1.nombre  USTED HA GANADO")
	            #color = pygame.Color(60,80,150)
	            #pygame.draw.line(win, color,(100,200), (500,400))
	            win.blit(ganador1,(50, tabler.fil3 + 170))
	            #running = False
	            pygame.display.update()
	    	        	

      


    # Red, Green, Blue
    #screen.fill((160, 0, 0))
    pygame.display.update()    

   