""" def createFiStart(tabla, configuracionInicial):
    #Eso se refleja en esta conjunción de
    #variables correspondientes a la fila 1 que estarán a verdadero las
    #correspondientes al símbolo contenido en cada una de ellas. 
    
    fi_start = ""
    fila = tabla[0] #recorro solo la primera fila
    max = len(fila)
    cont = 0
    for simbolo in configuracionInicial.split():
        if(cont != max-1):   
            if(simbolo == fila[cont]):
                fi_start += "TRUE AND "
            else: 
                fi_start += "FALSE AND "
        else:
            if(simbolo == fila[cont]):
                fi_start += "TRUE "
            else: 
                fi_start += "FALSE "
        cont += 1
    
    return fi_start

def estadosFinalesEnBonito(estadosFinales):
    estadosFinalesBonitos = []
    for estado in estadosFinales:
        estadosFinalesBonitos.append('q'+ str(estado))
    return estadosFinalesBonitos

def loContiene(estadosFinales, celda):
    for q in estadosFinales:
        if(q == celda):
            return True
    return False

def createFiAccept(tabla, estadosFinales):
    #asegura que qaccept aparezca
    #en alguna celda. (QUE HAYA ESTADO FINAL EN ALGUNA CELDA, LA QUE SEA) 
    fi_Accept=""
    for fila in tabla:
        for celda in fila:
            if(loContiene(estadosFinales, celda)):
                fi_Accept += 'TRUE'
    
    return fi_Accept

def crearNuevaFila(fila, regla):
    nuevaFila=""
    estadoNuevo = regla[2]
    simboloNuevo = regla[4]
    muevo = regla[5]

    for simbolo in fila:
        if(simbolo == '#'):
            nuevaFila += '# '
        if(simbolo != "#" or simbolo[0] != 'q'):
    
    return nuevaFila
    


def createFiMove(tabla, reglasEnOrden):
    cont=0
    filaDeberia=""
    for fila in tabla:
        #vemos que cada ventana es legal; Es decir, que la fila siguiente es creada por una regla de transicion.
        #Me voy a limitar a comprobar que la fila siguiente a la actual es creada por la regla en concreto.
        regla = reglasEnOrden[cont]
        filaDeberia = crearNuevaFila(fila, regla)
 """

from turtle import pos


def estadosEnBonito(estados):
    estadosBonitos = []
    for estado in estados:
        estadosBonitos.append('q'+ str(estado))
    return estadosBonitos 

def generarProposicionesPotenciales(tabla, estados, alfabetoCinta):
    #se genera a partir de cada casilla del tablón
    estados = estadosEnBonito(estados)  #lo sobreescribo, qué más da
    alfabetoCinta = alfabetoCinta
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


def generarPhiStart(tabla, proposicionesPotenciales, configuracionInicial):
    """ Eso se refleja en esta conjunción de
    variables correspondientes a la fila 1 que estarán a verdadero las
    correspondientes al símbolo contenido en cada una de ellas. """

    """ Φstart = x11# ∧ x12q0 ∧ x13w1 ∧ x14w2 ∧
    · · · ∧ x1(n+2)wn ∧ x1(n+3)B ∧ x1(n+4)B ∧ 
    · · · ∧ x1(nk−1)B ∧ x1(nk)# """
    

def generarPhiAccept():
    return " "

def generarPhiCell():
    return " "

def generarPhiMove():
    return " "


def apply(tabla, estados, alfabetoCinta, configuracionInicial):
    
    proposicionesPotenciales = generarProposicionesPotenciales(tabla, estados, alfabetoCinta)
    #phi_start = generarPhiStart(tabla, proposicionesPotenciales, configuracionInicial)
    #print(phi_start)
    #de las proposiciones de arriba se genera un AND que contiene sólo algunas 
    #de las variables generadas por la fila 1
    #phi_start = generarPhiStart(tabla, proposicionesPotenciales, configuracionInicial)   
    """ phi_accept = generarPhiAccept()
    phi_cell = generarPhiCell()
    phi_move = generarPhiMove()

    phi = phi_start + " AND " + phi_accept + " AND " + phi_cell + " AND " + phi_move

    return phi """

