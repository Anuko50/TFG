from os import system, name
from platform import java_ver
import phi_cell_generator
import phi_move_generator

# poner color en el texto para imprimir por pantalla
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# borrar la pantalla
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def mostrarComandosPosibles():
    print(colored(102, 255, 102, 'h (o help): muestra este mensaje'))
    print(colored(102, 255, 102,'q (o quit): termina el programa. '))
    print(colored(102, 255, 102,'1 : introduciendo un número de fila i y de columna j se mostrará una ventana y se dirá si es legal o no y el por qué.'))
    print(colored(102, 255, 102,'2 : explicación de phi_start.'))
    print(colored(102, 255, 102,'3 : explicación de phi_accept.'))
    print(colored(102, 255, 102,'4 : explicación de phi_cell, introduciendo un numero i (fila) y otro j (columna) de celda.'))
    print(colored(102, 255, 102,'5 : explicación de phi_move, introduciendo un numero i (fila).'))
    print()
    input('Presiona ENTER para continuar.')
    clear()

    
def explicacionPhi_start(phi_start, entrada):
    print(colored(26, 26, 255,'La fórmula booleana phi_start quiere representar el que la primera fila del tablón contenga la configuración de inicio con w a la entrada.'))
    print(colored(0, 179, 0, 'En otras palabras, lo que refleja la fórmula es que la primera fila del tablón contenga el estado inicial junto a la palabra de entrada (seguida de tantos símbolos blancos como sea necesario) de manera correcta, y no otra cosa.'))
    print()
    print(colored(0, 179, 0, 'En la reducción después se asignará con valor de verdad (True) aquellos literales de esta fórmula que efectivamente estén en el tablón.'))
    print()
    print(colored(0, 179, 0,'La fórmula genérica es esta: '))
    print()
    print(colored(255, 255, 0, 'phi_ start = x_1_1_# AND x_1_2_q0 AND x_1_3_w1 AND x_1_4_w2 AND [· · ·] AND x_1_(n+2)_wn'))
    print(colored(255, 255, 0, 'AND x_1_(n+3)_B AND x_1_(n+4)_B AND [· · ·] AND x_1_(nk−1)_B AND x_1_(nk)_#'))
    print()
    input('pulsa ENTER para continuar')
    clear()
    print(colored(0, 179, 0,'La fórmula phi_start para esta MT con la palabra \''+entrada+'\' es: '))
    print()
    print(colored(255, 255, 0,phi_start))
    print()
    input('pulsa ENTER para volver al menú principal')
    clear()


def explicacionPhi_accept(phi_accept, estadosFinales, entrada):
    print(colored(26, 26, 255,'La fórmula booleana phi_accept quiere representar el que alguna de las filas del tablón tiene que corresponder a una configuración de aceptación.'))
    print(colored(0, 179, 0, 'En otras palabras, lo que refleja es que se encuentre al menos un estado final en cualquier celda del tablón.'))
    print()
    print(colored(0, 179, 0, 'En la reducción después se asignará con valor de verdad (True) aquellos literales de esta fórmula que efectivamente estén en el tablón.'))
    print()
    print(colored(0, 179, 0,'La fórmula genérica es esta: '))
    print()
    print(colored(255, 255, 0, 'phi_accept = OR[1 ≤ i,j ≤ nk] x_i_j_qAccept'))
    print()
    print(colored(0, 179, 0, 'La fórmula lo que quiere decir es que va a crear un literal X_i_j_qAceptación para cada celda i,j del tablón y los va a unir con OR\'s lógicos.'))
    print(colored(0, 179, 0, 'Si en la tabla hay efectivamente un estado de aceptación, hará que la fórmula tenga valor verdadero (True)'))
    print()
    input('pulsa ENTER para continuar')
    clear()
    estados = " ".join(estadosFinales)
    msj = colored(0, 179, 0, 'Los estados finales de esta MT son : ' + estados)
    print(msj)
    print()
    print(colored(0, 179, 0,'La fórmula phi_accept para esta MT con la palabra \''+entrada+'\' es: '))
    print()
    print(colored(255, 255, 0,phi_accept))
    print()
    input('pulsa ENTER para volver al menú principal')
    clear()

def explicacionPhi_Cell(tabla, estados, alfabetoCinta, i, j):
    print(colored(26, 26, 255,'La fórmula booleana phi_Cell quiere representar el que Para cada celda concreta de la fila i y la columna j del tablón, una y sólo una de sus'))
    print(colored(26, 26, 255, 'correspondientes |C| variables puede estar a 1 (True) y las demás tienen que estar a 0 (False).'))
    print()
    print(colored(0, 179, 0, 'En otras palabras, lo que refleja es que Por cada celda debe haber uno, y solo uno, de los valores posibles.'))
    print(colored(0, 179, 0, 'Recordemos que \'C \' es un conjunto que consiste en la unión de el alfabeto de la cinta, el conjunto de estados, el símbolo que representa al Blanco (\'B\' u otro) y el símbolo \'#\'.'))
    print(colored(0, 179, 0, 'O de otra manera, C contiene a todos los símbolos que puede contener el tablón.'))
    print()
    print(colored(0, 179, 0,'La fórmula genérica es esta: '))
    print()
    print(colored(255, 255, 0, 'phi_Cell = AND[1≤i,j≤nk] [ (OR[s∈C] x_i_j_s) AND ( AND[s,t∈C;s̸=t] ( NOT(x_i_j_s) OR NOT(x_i_j_t) ) ) ]'))
    print()
    input('pulsa ENTER para continuar')
    clear()
    print(colored(0, 179, 0,'La fórmula genérica es esta: '))
    print(colored(255, 255, 0, 'phi_Cell = AND[1≤i,j≤nk] [ (OR[s∈C] x_i_j_s) AND ( AND[s,t∈C;s̸=t] ( NOT(x_i_j_s) OR NOT(x_i_j_t) ) ) ]'))
    print()
    print(colored(0, 179, 0, 'La fórmula se va a explicar por partes. Lo primero que encontramos es: \'AND[1≤i,j≤nk]\', esto refela que debe cumplirse para todas las celdas de la tabla, es decir que se va a unir la fórmula con un \'AND\' para que se cumplimente esta condición.'))
    print(colored(0, 179, 0, 'Ahora analizamos la fórmula en sí, lo que debe cumplirse por cada celda. La dividiremos en dos partes: '))
    print()
    print(colored(0, 179, 0, 'Primera parte: \' (OR[s∈C] x_i_j_s) \'.'))
    print(colored(0, 179, 0, 'Esta parte representa el que al menos un símbolo \'s\'∈C esté contenido dentro de la celda. Si esto no ocurriera, en la celda hubiera un símbolo que no pertenece a C (o no hubiera símbolo), esta parte daría False.'))
    print()
    print(colored(0, 179, 0, 'Segunda parte: \'( AND[s,t∈C;s̸=t] ( NOT(x_i_j_s) OR NOT(x_i_j_t) ) )\'.'))
    print(colored(0, 179, 0, 'Esta parte representa el que solo haya un símbolo contenido en esa celda, es decir, que una celda no contenga más de un valor.'))
    print(colored(0, 179, 0, 'Para ello se \'comparan\' dos símbolos \'s\' y \'t\', ambos pertenecientes a C y diferentes, y se comprueba que dentro de la celda o no esté contenido s, o no esté contenido t, pero lo que no puede ocurrir es que ambos estén dentro.'))
    print()
    input('pulsa ENTER para continuar')
    clear()
    phi_cell_min, phi_cell_min_valores, primeraParte, segundaParte = phi_cell_generator.generarPhiCell_soloUna(tabla, estados, alfabetoCinta, int(i), int(j))
    print(colored(0, 179, 0,'Ahora mostraremos, para la celda introducida, lo que correspondería a la primera y segunda parte que se acaban de explicar : '))
    print()
    print(colored(0, 179, 0, 'Primera parte: \' (OR[s∈C] x_i_j_s) \'.'))
    print()
    print(colored(255, 255, 0, primeraParte))
    print()
    print(colored(0, 179, 0, 'Segunda parte: \'( AND[s,t∈C;s̸=t] ( NOT(x_i_j_s) OR NOT(x_i_j_t) ) )\'.'))
    print()
    print(colored(255, 255, 0, segundaParte))
    print()
    input('pulsa ENTER para continuar')
    clear()
    print(colored(0, 179, 0,'Ahora mostraremos la fórmula phi_cell completa en esta celda en particular :'))
    print()
    print(colored(255, 255, 0, phi_cell_min))
    print()
    input('pulsa ENTER para volver al menú principal')
    clear()

    return None

def mainloop(phi_start, phi_accept, phi_cell, phi_move, tabla, n, estadosFinales, entrada, estados, alfabetoCinta):
    quit = False
    print(colored(0, 179, 0, "Bienvenido/a/e, introduce lo que quieres hacer."))
    print(colored(0, 179, 0, "Para ver las posibles opciones, introduce 'h' (de help): "))

    while(not quit):
        print(colored(0,0,255,'¡Bienvenido al menú principal!'))
        comando = input()
        clear()
        if(comando == 'h' or comando == 'help'):
            mostrarComandosPosibles()
        elif(comando == 'q' or comando == 'quit'):
            print(colored(0,0,255,'¡Adiós!'))
            exit(1)
        elif(comando == '1'):
            print(colored(255, 255, 0, 'EXPLICACIÓN VENTANAS'))
        elif(comando == '2'):
            print(colored(255, 255, 0, 'EXPLICACIÓN PHI_START'))
            explicacionPhi_start(phi_start, entrada)
        elif(comando == '3'):
            print(colored(255, 255, 0, 'EXPLICACIÓN PHI_ACCEPT'))
            explicacionPhi_accept(phi_accept, estadosFinales, entrada)
        elif(comando == '4'):
            print(colored(255, 255, 0, 'EXPLICACIÓN PHI_CELL'))
            correct = False

            while(not correct):
                i = input('introduce el número de fila de la celda a analizar: ')
                j = input('introduce el número de columna de la celda a analizar: ')
                if((i == '0' or j== '0') or ( int(i) > n or int(j) > n)):
                    print(colored(255,0,0, 'Has introducido un valor de celda incorrecto, debe ser de 1 hasta n (siendo n el tamaño del tablón).'))
                    print(colored(255,0,0, 'El tamaño del tablón actual es de '+ str(n) + " X "+ str(n)))
                    print(colored(255,0,0, 'Intentalo de nuevo.'))
                else: 
                    correct = True

            clear()
            explicacionPhi_Cell(tabla, estados, alfabetoCinta, i, j)
        elif(comando == '5'):
            print(colored(255, 255, 0, 'EXPLICACIÓN PHI_MOVE'))
        else:
            print(colored(255,0,0,'Has introducido un comando invalido, si necesitas ayuda introduce h (help)'))