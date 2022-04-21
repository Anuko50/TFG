import re
import phi_star_generator
import phi_accept_generator
import phi_cell_generator



####################################################################################################
###############################   FUNCIONES GENERICAS     ##########################################
####################################################################################################

def estadosEnBonito(estados):
    estadosBonitos = []
    for estado in estados:
        estadosBonitos.append('q'+ str(estado))
    return estadosBonitos 

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


####################################################################################################
####################################     PHI_MOVE     ##############################################
####################################################################################################
def generarPhiMoveReducido(tabla, n, reglas_en_orden):
    return " "

def generarLaMisma(fila, filaSiguiente, i):
    igual=" ( "
    igual_valores=" ( "
    cont=1
    for index in range(0,len(fila),1):
        if(index<len(fila)-1):
            igual = "X_"+str(i)+"_"+str(cont)+"_"+fila[cont] + " AND "
            if(fila[cont] == filaSiguiente[cont]):
                igual_valores = "TRUE AND "
            else:
                igual_valores = "FALSE AND "
        else:
            igual = "X_"+str(i)+"_"+str(cont)+"_"+fila[cont] 
            if(fila[cont] == filaSiguiente[cont]):
                igual_valores = "TRUE )"
            else:
                igual_valores = "FALSE )"
    return igual, igual_valores


def queHay(fila):
    estadoFila=""
    headFila=""
    esEstado = re.compile("q[0-9]*")
    for i in range(0,len(fila),1):
        match = re.fullmatch(esEstado, fila[i])
        if(match):
            estadoFila = fila[i]
            headFila = fila[i+1]
            return estadoFila, headFila
    
    return estadoFila, headFila

def crearFila(fila, estado_nuevo, nuevo_simbolo, direccion):
    fila = fila.split()
    filaNueva= ""
    esEstado = re.compile("q[0-9]*")
    for i in range(0,len(fila),1):
        match = re.fullmatch(esEstado, fila[i])
        if(match):
            if(direccion ==  'R'):  #muevo el cabezal a la derecha
                filaNueva += nuevo_simbolo  + " " + estado_nuevo + " "
                i = i + 2
                for i in range(i,len(fila),1): 
                    filaNueva+= fila[i] + " " 
                return filaNueva
            elif(direccion ==  'L'):
                muevo = filaNueva[i-1]
                filaNueva[i-1] += estado_nuevo + " " 
                filaNueva[i] += muevo + " " 
                filaNueva[i+1] += nuevo_simbolo + " " 
                i = i + 2
                for i in range(i,len(fila),1): 
                    filaNueva+= fila[i] + " " 
                return filaNueva
            else: # stay, me quedo igual
                filaNueva += estado_nuevo + " " 
                filaNueva += nuevo_simbolo  + " " 
                i = i + 2
                for i in range(i,len(fila),1): 
                    filaNueva+= fila[i] + " " 
                return filaNueva
        else:
            filaNueva+= fila[i] + " " 
    return filaNueva

""" valores de transitions:
    ['estado_actual', 'estado_nuevo', 'simbolo_Actual', 'Nuevo_Simbolo', 'direccion']  """
def generarFilas(fila, transitions):
    filas = []
    for t in transitions:
        estadoFila, headFila = queHay(fila)
        estado_actual = 'q' + t[0]       
        simbolo_actual = t[2]
        if (estado_actual == estadoFila) and (headFila == simbolo_actual):
            estado_nuevo = 'q' + t[1]
            nuevo_simbolo = t[3]
            direccion = t[4]
            fila = crearFila(fila, estado_nuevo, nuevo_simbolo, direccion)

def generarPosibles(fila, filaSiguiente, transitions, i, j):
    posibles = " ( "
    posibles_valores = " ( "
    filasPosibles = generarFilas(fila, transitions)

def generarPhiMove(tabla, n, transitions):
    #IDEA: ir fila por fila viendo que es legal.
    #Una fila es legal cuando: tiene un unico estado y cuando es igual que la anterior o se ha llegado a ella a través de una regla de transicion
    #Se hace así porque la MT admite el estado "STAY" y complica las cosas. De esta manera es muy facil.
    #Se ha adaptado la fórmula pero es igual, en vez de ventanas de tamaño 2x3 son de tamaño filax2
    phi_move="( "
    phi_move_valores="( "
    for i in range(0,n-1,1):
        j=i+1 #comparamos la fila "i" con su siguiente
        igual, igual_valores = generarLaMisma(tabla[i], tabla[j], i)
        phi_move += igual + " OR "
        phi_move_valores += igual_valores + " OR "
        generarPosibles(tabla[i], tabla[j], transitions, i, j)

        
    return " "

####################################################################################################
####################################     APLICACION:  ##############################################
####################################################################################################

def apply(n, tabla, estados, alfabetoCinta, configuracionInicial, estadosFinales, reglas_en_orden, transitions):
    
    print(configuracionInicial)
    #Pongo los estados en el formato adecuado:
    estados = estadosEnBonito(estados) 
    proposicionesPotenciales = generarProposicionesPotenciales(tabla, estados, alfabetoCinta)
    #print(proposicionesPotenciales)
    phi_start, phi_start_valores = phi_star_generator.generarPhiStart(n, tabla, proposicionesPotenciales, configuracionInicial)
    print()
    print("PHI_START:")
    print(phi_start)
    print("PHI_START_VALORES ASIGNADOS:")
    print(phi_start_valores)
    
    phi_accept, phi_accept_valores, loCumpleAccept = phi_accept_generator.generarPhiAccept(tabla, phi_accept_generator.estadosFinalesEnBonito(estadosFinales), n)
    print()
    print("PHI_ACCEPT:")
    print(phi_accept)
    print("PHI_ACCEPT_VALORES ASIGNADOS:")
    print(phi_accept_valores) 
    #  if(loCumpleAccept):
    #       print('SI tiene un estado final')
    #   else:
    #       print('NO tiene un estado final')
    #   
    #   print(estadosFinales)

    phi_cell, phi_cell_valores = phi_cell_generator.generarPhiCell(tabla, n, estados, alfabetoCinta)
    print()
    print("PHI_CELL:")
    print(phi_cell)
    print("PHI_CELL_VALORES ASIGNADOS:")
    print(phi_cell_valores) 
    
    """ phi_move, phi_move_valores = generarPhiMove(tabla, n, transitions)
    print()
    print("PHI_MOVE:")
    print(phi_move)
    print("PHI_MOVE_VALORES ASIGNADOS:")
    print(phi_move_valores)  """
    #de las proposiciones de arriba se genera un AND que contiene sólo algunas 
    #de las variables generadas por la fila 1
    #phi_start = generarPhiStart(tabla, proposicionesPotenciales, configuracionInicial)   
    """ phi_accept = generarPhiAccept()
    phi_cell = generarPhiCell()
    phi_move = generarPhiMove()

    phi = phi_start + " AND " + phi_accept + " AND " + phi_cell + " AND " + phi_move

    return phi """

