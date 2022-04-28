from os import system, name

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
    print(colored(102, 255, 102,'4: explicación de phi_cell, introduciendo un numero i (fila) y otro j (columna) de celda.'))
    print(colored(102, 255, 102,'5: explicación de phi_move, introduciendo un numero i (fila).'))
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



def mainloop(phi_start, phi_accept, phi_cell, phi_move, tabla, n, estadosFinales, entrada):
    quit = False
    print("Bienvenido/a/e, introduce lo que quieres hacer.")
    print("Para ver las posibles opciones, introduce 'h' (de help): ")

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
        elif(comando == '5'):
            print(colored(255, 255, 0, 'EXPLICACIÓN PHI_MOVE'))
        else:
            print(colored(255,0,0,'Has introducido un comando invalido, si necesitas ayuda introduce h (help)'))