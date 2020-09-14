
class Tablero: 
    """
    Aquí se crea el objeto tipo tablero, que es la que permite visualizar
    el juego, marcar casillas y buscar jugador.
    Recibe como argumento una  lista de numero de 0-9 en caracteres

    """

    def __init__(self,x):
        self.tablero = x

    def print (self):       
        """
        Función que imprime el self.tablero
        """
        print("     |     |     " )  
        print(f"  {self.tablero[1]}  |  {self.tablero[2]}  |  {self.tablero[3]}")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.tablero[4]}  |  {self.tablero[5]}  |  {self.tablero[6]}")
        print("_____|_____|_____")
        print("     |     |     ")
        print(f"  {self.tablero[7]}  |  {self.tablero[8]}  |  {self.tablero[9]}")
        
    def marcar_casilla(self,casilla_elegida, simbolo):
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
            
            
    def buscar_ganador(self):
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
    def __init__(self, nombre, num):
        self.nombre = nombre
        self.num = num
    
    def __str__(self):
        return(self.nombre)



x = ["0","1","2", "3", "4", "5","6","7","8","9"]
TableroPuntuacion = Tablero(x)

print("\nBienvenido al lugar donde aprender ingles es un juego".upper().center(50," "))
print("Diviertase jugando X-0".center(50, " "))
print("Intrucciones".center(50, "="))
print("En su turno usted debe escribir el pasado paricipio o")
print("pasado simple del verbo, si usted falla entonces el turno pasa a su compañero\n\n")

TableroPuntuacion.print()


print("Digiten sus nombres: ")
jugador1 = Jugador(input("Jugador 1: " ), 1)
jugador2 = Jugador(input("Jugador 2: " ), 2)


turno = 1
estado = -1


while(estado == -1):
    
    if (turno == 1):
        print(f"{jugador1.nombre} por favor digite la casilla donde quiere poner la X")
        TableroPuntuacion.marcar_casilla(int(input()), "X")
        turno = 2

    else: 
        print(f"{jugador2.nombre} por favor digite la casilla donde quiere poner la 0")
        TableroPuntuacion.marcar_casilla(int(input()), "0")
        turno = 1

    TableroPuntuacion.print()
    estado = TableroPuntuacion.buscar_ganador()



if(estado==1):
    if(turno==1):
        print(f"Felicidades {jugador2} usted ha ganado")
    else:
        print(f"Felicidades {jugador1} usted ha ganado") 
else:
    print("Empate")



    

