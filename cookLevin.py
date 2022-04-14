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

from distutils.command.config import config
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

####################################################################################################
####################################     PHI_START    ##############################################
####################################################################################################

def generarPhiStart(n, tabla, proposicionesPotenciales, configuracionInicial):
    phiStart=""
    phiStart_valores=""

    for j in range(0,n,1):
        if(j < n-1):
            phiStart += "X_1_"+ str(j+1)+"_"+configuracionInicial[j]+" AND "
        else:
            phiStart += "X_1_"+ str(j+1)+"_"+configuracionInicial[j]
    
    for j in range(0,n,1):
        if(j < n-1):
            if(configuracionInicial[j] == tabla[0][j]):
                phiStart_valores += "TRUE AND "
            else:
                phiStart_valores += "FALSE AND "
        else:
            if(configuracionInicial[j] == tabla[0][j]):
                phiStart_valores += "TRUE "
            else:
                phiStart_valores += "FALSE "

    return phiStart, phiStart_valores


####################################################################################################
####################################     PHI_ACCEPT   ##############################################
####################################################################################################

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

def crearLiteralesFinales(estadosFinales, n):
    literalesFinales = []
    for i in range(1,n-1,1):
        for j in range(1,n-1,1):
            for q in estadosFinales:
                literal = 'X'+str(i)+'_'+str(j)+'_'+q
                literalesFinales.append(literal)
    return literalesFinales

def generarPhiAccept(tabla, estadosFinales, n):
    #asegura que qaccept aparezca
    #en alguna celda. (QUE HAYA ESTADO FINAL EN ALGUNA CELDA, LA QUE SEA)
    literalesFinales = crearLiteralesFinales(estadosFinales, n) 
    tam = len(literalesFinales)
    loCumple=False
    fi_Accept=""
    fi_Accept_valores=""

    for i in range(0,tam,1):
        if(i< tam-1):
            fi_Accept += literalesFinales[i] + ' OR '
        else:
             fi_Accept += literalesFinales[i]
    
    for i in range(0,n,1):
        for j in range(0,n,1):
            celda = tabla[i][j]
            if((j == i) and (j == n-1)):
                if(loContiene(estadosFinales, celda)):
                    fi_Accept_valores += 'TRUE '
                    loCumple = True
                else:
                    fi_Accept_valores += 'FALSE '
            else:
                if(loContiene(estadosFinales, celda)):
                    fi_Accept_valores += 'TRUE OR '
                    loCumple = True
                else:
                    fi_Accept_valores += 'FALSE OR '
    return fi_Accept, fi_Accept_valores, loCumple


    """ for fila in tabla:
        for celda in fila:
            if(loContiene(estadosFinales, celda)):
                fi_Accept_valores += 'TRUE OR '
            else:
                fi_Accept_valores += 'FALSE OR ' """
    
    return fi_Accept, fi_Accept_valores

def generarPhiCell():
    return " "

def generarPhiMove():
    return " "


def apply(n, tabla, estados, alfabetoCinta, configuracionInicial, estadosFinales):
    
    print(configuracionInicial)
    proposicionesPotenciales = generarProposicionesPotenciales(tabla, estados, alfabetoCinta)
    #print(proposicionesPotenciales)
    phi_start, phi_start_valores = generarPhiStart(n, tabla, proposicionesPotenciales, configuracionInicial)
    print()
    print("PHI_START:")
    print(phi_start)
    print(phi_start_valores)
    
    phi_accept, phi_accept_valores, loCumpleAccept = generarPhiAccept(tabla, estadosFinalesEnBonito(estadosFinales), n)
    print()
    print("PHI_ACCEPT:")
    print(phi_accept)
    print(phi_accept_valores)
    if(loCumpleAccept):
        print('SI tiene un estado final')
    else:
        print('NO tiene un estado final')
    
    print(estadosFinales)

    #de las proposiciones de arriba se genera un AND que contiene sólo algunas 
    #de las variables generadas por la fila 1
    #phi_start = generarPhiStart(tabla, proposicionesPotenciales, configuracionInicial)   
    """ phi_accept = generarPhiAccept()
    phi_cell = generarPhiCell()
    phi_move = generarPhiMove()

    phi = phi_start + " AND " + phi_accept + " AND " + phi_cell + " AND " + phi_move

    return phi """

