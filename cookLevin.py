import re
import phi_star_generator
import phi_accept_generator
import phi_cell_generator
import phi_move_generator
from os import system, name


####################################################################################################
##################################      FUNCIONES :     ############################################
####################################################################################################


def generarProposicionesPotenciales(tabla, estados, alfabetoCinta):
    #se genera a partir de cada casilla del tablón
    #alfabetoCinta = alfabetoCinta
    posiblesValores = estados + alfabetoCinta
    posiblesValores.append('#')
    proposicionesPotenciales = [] 
    #A cada fila y celda le corresponden |C| valores
    i=1 #contador de filas
    j=1 #contador de columnas
    for fila in tabla:
        for celda in tabla:
            proposicionesFila = []
            for valor in posiblesValores:
                proposicion = 'X' +  "_" +str(i) + "_" + str(j) + "_" + valor
                proposicionesFila.append(proposicion)
            proposicionesPotenciales.append(proposicionesFila)
            j += 1

        i += 1
        j = 0 #reiniciamos las columnas
    
    return proposicionesPotenciales

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

####################################################################################################
####################################     APLICACION:  ##############################################
####################################################################################################

def apply(n, tabla, estados, alfabetoCinta, configuracionInicial, estadosFinales, reglas_en_orden, transitions):
    
    #print(configuracionInicial)
    #Pongo los estados en el formato adecuado:
    estados = estados 
    proposicionesPotenciales = generarProposicionesPotenciales(tabla, estados, alfabetoCinta)
    #print(proposicionesPotenciales)
    phi_start, phi_start_valores = phi_star_generator.generarPhiStart(n, tabla, proposicionesPotenciales, configuracionInicial)
    """  print()
    print("PHI_START:")
    print(phi_start)
    print()
    print("PHI_START_VALORES ASIGNADOS:")
    print(phi_start_valores)  """
    
    phi_accept, phi_accept_valores, loCumpleAccept = phi_accept_generator.generarPhiAccept(tabla, estadosFinales, n)
    """ print()
    print("PHI_ACCEPT:")
    print(phi_accept)
    print()
    print("PHI_ACCEPT_VALORES ASIGNADOS:")
    print(phi_accept_valores)  """
    #  if(loCumpleAccept):
    #       print('SI tiene un estado final')
    #   else:
    #       print('NO tiene un estado final')
    #   
    #   print(estadosFinales)

    phi_cell, phi_cell_valores = phi_cell_generator.generarPhiCell(tabla, n, estados, alfabetoCinta)
    """ print()
    print("PHI_CELL:")
    print(phi_cell)
    print()
    print("PHI_CELL_VALORES ASIGNADOS:")
    print(phi_cell_valores)   """
    
    phi_move, phi_move_valores = phi_move_generator.generarPhiMove(tabla, n, transitions)
    """ print()
    print("PHI_MOVE:")
    print(phi_move)
    print()
    print("PHI_MOVE_VALORES ASIGNADOS:")
    print(phi_move_valores)  """
    #de las proposiciones de arriba se genera un AND que contiene sólo algunas 
    #de las variables generadas por la fila 1
    #phi_start = generarPhiStart(tabla, proposicionesPotenciales, configuracionInicial)   

    phi = phi_start + " AND " + phi_accept + " AND " + phi_cell + " AND " + phi_move

    return phi, phi_start, phi_accept, phi_cell, phi_move

