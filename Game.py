
#------ Para el desarrollo del juego se ocupa el archivo .csv ------#

#----- Librerías---------
import pandas as pd
import numpy as np
import os
#------------------------


#-------------------------------------CLASES--------------------------------------------

class testVerbos:
	"""
	Clase Prueba que permite crear pruebas para evaluar los conocimientos
	de vocabulario de los verbos
	"""
	def __init__(self,verbos):
		self.dfVerbos = verbos

	def test(self, aleatorio, nombreJugador):
		palabInfin = self.dfVerbos["INFINITIVO"][aleatorio]
		print(f"{nombreJugador} ingrese el pasado SIMPLE del verbo:  {palabInfin} -- ", end="")
		pastParticiple = input()
		revision = self.dfVerbos["PASADO SIMPLE"][aleatorio] == pastParticiple.capitalize()

		if(revision):
			print("Es correcto")
		else:
			print(":( :( El resultado correcto es: ", self.dfVerbos["PASADO SIMPLE"][aleatorio], "-->",self.dfVerbos["TRADUCCION"][aleatorio] )
			print(" ")
			print("El turno pasa al siguiente jugador".center(50,"="))
			continuar =  input("Presione la tecla C para continuar ")
		return revision


class Tabler: 
    """
    Aquí se crea el objeto tipo tablero

    """

    def __init__(self,x):
        self.tablero = x

    def print (self):       
        """
        Método que imprime el estado del tablero
        """
        print("     |     |     " )  
        print(f"  {self.tablero[1]}  |  {self.tablero[2]}  |  {self.tablero[3]}")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.tablero[4]}  |  {self.tablero[5]}  |  {self.tablero[6]}")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.tablero[7]}  |  {self.tablero[8]}  |  {self.tablero[9]}")



""" 
    Aquí se crea el objeto tipo tablero, que es la que permite visualizar
    el juego, marcar casillas y buscar ganador.
    Recibe como argumento una  lista de numero de 0-9 en caracteres

    """
class Tablero(Tabler):                 #--- Herencia
    def __init__(self, df ):
        super().__init__(df)
        
    def marcar_casilla(self,casilla_elegida, simbolo):
        """
        Método que marca una casilla indicada casilla, ya sea con un cero o una X
        """
        if (casilla_elegida == 1 and self.tablero[1] == "1"):
            self.tablero[1] = simbolo
            
        elif (casilla_elegida == 2 and self.tablero[2] == "2"):
            self.tablero[2] = simbolo
            
        elif (casilla_elegida == 3 and self.tablero[3] == "3"):
            self.tablero[3] = simbolo
        
        elif (casilla_elegida == 4 and self.tablero[4] == "4"):
            self.tablero[4] = simbolo
            
        elif (casilla_elegida == 5 and self.tablero[5] == "5"):
            self.tablero[5] = simbolo
            
        elif (casilla_elegida == 6 and self.tablero[6] == "6"):
            self.tablero[6] = simbolo
            
        elif (casilla_elegida == 7 and self.tablero[7] == "7"):
            self.tablero[7] = simbolo
        
        elif (casilla_elegida == 8 and self.tablero[8] == "8"):
            self.tablero[8] = simbolo
            
        elif (casilla_elegida == 9 and self.tablero[9] == "9"):
            self.tablero[9] = simbolo
        else:       
            print("Jugada invalida, el turno pasa al otro jugador ")
            #TableroPuntuacion.marcar_casilla(self, casilla_elegida,simbolo)
            a = input("Precione C para continuar: ")
            
            
    def buscar_ganador(self):
        """
        Método que refresa el estado del juego, el cual pueder ser: Hay ganador,
        empate o que puede continuar jugando"""
        tablero = self.tablero
        
        if(tablero[1] == tablero[2] and tablero[2] == tablero[3]):
                return 1                                            # hay ganador

        elif (tablero[4] == tablero[5] and tablero[5] == tablero[6]):
            return 1 

        elif(tablero[7] == tablero[8] and tablero[8] == tablero[9]):
            return 1                                               # Tercer fila igual simbolo
                                                                   # Hay ganadot
        # ------- Comprobando lo anterior pero para las columnas------------------
        elif (tablero[1] == tablero[4] and tablero[4] == tablero[7]):  # Columna 1
            return 1;

        elif (tablero[2] == tablero[5] and tablero[5] == tablero[8]):   # Columna 2
            return 1

        elif (tablero[3] == tablero[6] and tablero[6] == tablero[9]):   # Columna 3
            return 1
        #------------- Buscando ganador en las diagonales ---------------------------  
        elif (tablero[1] == tablero[5] and tablero[5] == tablero[9]):
            return 1   
        elif(tablero[3] == tablero[5] and tablero[5] == tablero[7]):
            return 1
        #Buscando empate
        elif (tablero[1] != '1' and tablero[2] != '2' and tablero[3] != '3' and tablero[4] != '4' 
              and tablero[5] != '5' and tablero[6] != '6'  and tablero[7] != '7' and tablero[8] != '8' and tablero[9] != '9'):
            return 0
        else:
            return -1 # En caso de no haber empate ni ganador entonces se puede seguir jugando



class Jugador(): 
    """
    Clase Jugador que crea los posibles jugadores
    """
    def __init__(self, nombre, num):
        self.nombre = nombre
        self.num = num
    
    def __str__(self):           #- Sobrecarga
        return(self.nombre)

#--------------------------------------FIN CLASES ---------------------------------------






#-------------------------------- ---INICIO DEL JUEGO-----------------------------------

decision = 1
while (decision == 1):

	#------------------------------ Pantalla -  Inicio ---------------------------------
	x = ["0","1","2", "3", "4", "5","6","7","8","9"]
	TableroPuntuacion = Tablero(x)

	print("\nBienvenido al lugar donde aprender ingles es un juego".upper().center(50," "))
	print("!!!Diviertase jugando y aprendiendo con X-0!!!".center(50, " "))
	print("Intrucciones".center(50, "="))
	print("En su turno usted debe escribir el pasado  SIMPLE ")
	print("Si usted falla entonces el turno pasa a su compañero")
	TableroPuntuacion.print()
	#------------------------------------------------------------------------------------


	#--------------------- Cargando variables para iniciar a jugar------------
	print("Digiten sus nombres: ")
	jugador1 = Jugador(input("Jugador 1: " ), 1)
	jugador2 = Jugador(input("Jugador 2: " ), 2)

	turno = 1
	estado = -1
	verbos = pd.read_csv("verbos.csv") 
	EvaluacionIngles = testVerbos(verbos)
	n = len(verbos["INFINITIVO"])
	#----------------------------------------------------------------------------


	#--------Inicio de Partida en el tablero y prueba de vocabulario por jugador ----------
	while(estado == -1):   
	    os.system ("clear") 
	    print("\nBienvenido al lugar donde aprender ingles es un juego".upper().center(50," "))
	    print("Diviertase jugando X-0".center(50, " "))
	    print("Intrucciones".center(50, "="))
	    print("En su turno usted debe escribir el pasado SIMPLE")
	    print("Si usted falla entonces el turno pasa a su compañero\n")

	    print(jugador1, ": X")
	    print(jugador2, ": 0")
	    TableroPuntuacion.print()
	    if (turno == 1):
	        aleatorio = np.random.choice(n,1)[0]
	        if (EvaluacionIngles.test(aleatorio, jugador1.nombre)):
	            print(f"{jugador1.nombre} por favor digite el numero de la casilla donde quiere poner la X: ")
	            TableroPuntuacion.marcar_casilla(int(input()), "X")
	            TableroPuntuacion.print()
	            estado = TableroPuntuacion.buscar_ganador()

	        turno = 2

	    else: 
	        aleatorio = np.random.choice(n,1)[0]
	        if (EvaluacionIngles.test(aleatorio, jugador2.nombre)):
	            print(f"{jugador2.nombre} por favor digite la casilla donde quiere poner la 0")
	            TableroPuntuacion.marcar_casilla(int(input()), "0")
	            TableroPuntuacion.print()
	            estado = TableroPuntuacion.buscar_ganador()

	        turno = 1

	    if(estado==1):
	        if(turno==1):
	            print(f"Felicidades {jugador2} usted ha ganado")
	        else:
	            print(f"FelICIDADES {jugador1} USTED HA GANADO".center(50, "=")) 
	    elif(estado == 0):
	        print("Empate")

	#-------------------------------- Fin de la partida ------------------------------

	print("\nOpciones")
	print("1 - Otra Partida ")
	print("2 - Salir")
	decision = int(input("Digite el numero de la opción: "))

#------------------------------------ FIN JUEGO----------------------------------------

"""
NOTA:
Se creo la clase Tabler y Tablero por separado solo para usar herencia 

"""