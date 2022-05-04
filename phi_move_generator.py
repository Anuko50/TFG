import re

####################################################################################################
####################################     PHI_MOVE     ##############################################
####################################################################################################

def generarLaMisma(fila, filaSiguiente, i):
    igual=" ( "
    igual_valores=" ( "
    tam = len(fila)
    esLaMisma = True

    for index in range(0, tam ,1):
        valor = fila[index]
        if(index < tam-1):
            #fila anterior
            igual += "X_"+str(i)+"_"+str(index+1)+"_"+valor + " AND "
            #la fila siguiente
            igual += "X_"+str(i+1)+"_"+str(index+1)+"_"+valor + " AND "
            if(fila[index] == filaSiguiente[index]):
                igual_valores += "TRUE AND TRUE AND "
            else:
                igual_valores += "TRUE AND FALSE AND "
                esLaMisma = False
        else:
            #fila anterior
            igual += "X_"+str(i)+"_"+str(index+1)+"_"+valor + " AND "
            #la fila siguiente
            igual += "X_"+str(i+1)+"_"+str(index+1)+"_"+valor + " ) "
            if(fila[index] == filaSiguiente[index]):
                igual_valores += "TRUE AND TRUE )"
            else:
                igual_valores += "TRUE AND FALSE )"
                esLaMisma = False

    return igual, igual_valores, esLaMisma

#crea la fila tras aplicarle la transicion
# #todo: falla aqui  
def crearFila(fila, estado_nuevo, nuevo_simbolo, direccion):
    tamano = len(fila)
    filaNueva= ['0'] * tamano
    esEstado = re.compile("q[0-9]*")
    for i in range(0,tamano,1):
        match = re.fullmatch(esEstado, fila[i])
        if(match):
            if(direccion ==  'R'):  #muevo el cabezal a la derecha
                filaNueva[i] = nuevo_simbolo 
                filaNueva[i+1] = estado_nuevo 
                i = i + 2
                for i in range(i,len(fila),1): 
                    filaNueva[i] = fila[i] 
                return filaNueva
            elif(direccion ==  'L'):
                muevo = filaNueva[i-1]
                filaNueva[i-1] = estado_nuevo  
                filaNueva[i] = muevo 
                filaNueva[i+1] = nuevo_simbolo 
                i = i + 2
                for i in range(i,len(fila),1): 
                    filaNueva[i] = fila[i] 
                return filaNueva
            else: # stay, me quedo igual
                filaNueva[i] = estado_nuevo 
                filaNueva[i+1] = nuevo_simbolo 
                i = i + 2
                for i in range(i,len(fila),1): 
                    filaNueva[i] = fila[i] 
                return filaNueva
        else:
            filaNueva[i] = fila[i] 

    return filaNueva


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

#valores de transitions:
#    ['estado_actual', 'estado_nuevo', 'simbolo_Actual', 'Nuevo_Simbolo', 'direccion']
def generarFilas(fila, transitions):
    filas = []
    estadoFila, headFila = queHay(fila)
    tam = len(transitions)
    for i in range(1, tam + 1, 1):
        t=transitions[i]
        estado_actual = "q" +  str(t[0]) 
        simbolo_actual = str(t[2])
        if (estado_actual == estadoFila) and (headFila == simbolo_actual):
            estado_nuevo = "q" + str(t[1])
            nuevo_simbolo = str(t[3])
            direccion = str(t[4])
            f = crearFila(fila, estado_nuevo, nuevo_simbolo, direccion)
            filas.append(f)

    return filas


def generarPosibles(fila, filaSiguiente, transitions, i, j):
    valoresFila=""
    valoresFila_valores = ""
    posibles = ""
    posibles_valores = ""
    siHayPosible = False
    #Los valores de la fila padre (siempre iguales)
    #termina en AND porque se va a unir con los valores posibles que puede tener la otra fila
    for c in range(0,len(fila),1):
        valor = fila[c]
        valoresFila += "X_"+str(i)+"_"+str(c+1)+"_"+valor+ " AND " 
        valoresFila_valores += "TRUE AND "   #siempre tienen valor verdad

    filasPosibles = generarFilas(fila, transitions)
    tam = len(filasPosibles)

    if(tam != 0):
        for x in range(0,tam,1):
            hay = True
            f = filasPosibles[x]
            posible_actual=""
            posible_actual_valores=""
            #comparo la fila siguiente con la posible segun la formula
            tamano = len(f)

            for c in range(0, tamano,1):
                valor = f[c]
                valorSiguiente = filaSiguiente[c]

                if(c < tamano -1):
                    posible_actual += "X_"+str(j)+"_"+str(c+1)+"_"+valor+ " AND " 
                    if(valor == valorSiguiente):
                        posible_actual_valores += "TRUE AND "
                    else:
                        posible_actual_valores += "FALSE AND "
                        hay = False
                else:
                    posible_actual += "X_"+str(j)+"_"+str(c+1)+"_"+valor + " "
                    if(valor == valorSiguiente):
                        posible_actual_valores += "TRUE "
                    else:
                        posible_actual_valores += "FALSE  "
                        hay = False
        
            if(x < tam-1 ):
                posibles += " ( " + valoresFila + posible_actual + " ) OR "
                posibles_valores += " ( " + valoresFila_valores + posible_actual_valores + " ) OR "
            else:
                posibles +=  " ( " + valoresFila + posible_actual + " ) )"
                posibles_valores +=  " ( " + valoresFila_valores + posible_actual_valores + " ) )" 
            
            if(hay):
                siHayPosible = True

    else:
        posibles = ""
        posibles_valores = ""
    
    return posibles, posibles_valores, siHayPosible

def valoresFila(fila, i):
    tam = len(fila)
    igual = ""
    igual_valores = ""
    for index in range(0, tam ,1):
        valor = fila[index]
        igual += "X_"+str(i)+"_"+str(index+1)+"_"+valor + " AND "
        igual_valores += "TRUE AND  "


    return igual, igual_valores


####################################################################################################
########################################     MAIN :       ##########################################
####################################################################################################

def generarPhiMove(tabla, n, transitions):
    #IDEA: ir fila por fila viendo que es legal.
    #Una fila es legal cuando: tiene un unico estado y cuando es igual que la anterior o se ha llegado a ella a través de una regla de transicion
    #Se hace así porque la MT admite el estado "STAY" y complica las cosas. De esta manera es muy facil.
    #Se ha adaptado la fórmula pero es igual, en vez de ventanas de tamaño 2x3 son de tamaño filax2
    phi_move=" ( "
    phi_move_valores=" ( "
    valorTotal = True
    for i in range(0,n-1,1):
        #comparamos la fila "i" con su siguiente
        igual, igual_valores, esLaMisma = generarLaMisma(tabla[i], tabla[i+1], i+1)  #en caso de que no se haga transicion
        posibles, posibles_valores, hayPosible = generarPosibles(tabla[i], tabla[i+1], transitions, i+1, i+2)

        if((not esLaMisma) and (not hayPosible)):
            valorTotal = False
        # el primer caso siempre va a ser el de si las dos filas son iguales
        phi_move += " ( " + igual
        phi_move_valores += " ( " +  igual_valores  
        
        #¿hay transiciones posibles?
        if(posibles == ""): # si no, solo pongo el caso de que sean iguales, lo unico que la hace legal
            if(i < n-2): # porque recorremos las filas dos a dos
                phi_move += " ) AND "
                phi_move_valores +=  " ) AND "
            else:
                phi_move +=  " ) "
                phi_move_valores +=  " ) "
        else: # si hay transiciones posibles; pongo la fila actual + la posible
            if(i < n-2):
                phi_move += " OR " + posibles + " AND "
                phi_move_valores += " OR " + posibles_valores + " AND "
            else:
                phi_move += " OR " + posibles + " "
                phi_move_valores += " OR " + posibles_valores + " "

    phi_move += " ) "
    phi_move_valores += " ) "
    return phi_move, phi_move_valores, valorTotal


###################################################
############# para la explicación: ################
###################################################

def generarPhi_move_UnaSolo(tabla, n, transitions, i):
    phi_move_min=" ( "
    phi_move_valores_min=" ( "
    
    #comparamos la fila "i" con su siguiente
    igual, igual_valores = generarLaMisma(tabla[i-1], tabla[i], i)  #en caso de que no se haga transicion
    posibles, posibles_valores = generarPosibles(tabla[i-1], tabla[i], transitions, i, i+1)
    # el primer caso siempre va a ser el de si las dos filas son iguales
    phi_move_min += " ( " + igual
    phi_move_valores_min += " ( " +  igual_valores  
    
    #¿hay transiciones posibles?
    if(posibles == ""): # si no, solo pongo el caso de que sean iguales, lo unico que la hace legal
            phi_move_min +=  " ) "
            phi_move_valores_min +=  " ) "
    else: # si hay transiciones posibles; pongo la fila actual + la posible
            phi_move_min += " OR " + posibles + " "
            phi_move_valores_min += " OR " + posibles_valores + " "

    phi_move_min += " ) "
    phi_move_valores_min += " ) "

    return phi_move_min, phi_move_valores_min, igual, posibles 


####################################################################################################
####################################     FUNCIONES VENTANAS :    ###################################
####################################################################################################

def cogerVentana(tabla, i,j):
    i = i-1
    j = j-1
    #las ventanas son 
    # a1 a2 a3
    # a4 a5 a6
    # j debe ser mayor que 1 y menor que n
    # i debe ser menor que n
    a2 = tabla[i][j]
    a1 = tabla[i][j-1]
    a3 = tabla[i][j+1]
    a5 = tabla[i+1][j]
    a4 = tabla[i+1][j-1]
    a6 = tabla[i+1][j+1]
    ventana = [[a1,a2,a3],[a4,a5,a6]]
    fila = tabla[i]

    return fila, ventana

def ventanaEsIgual(ventana):
    es = True
    fila_1= ventana[0]
    fila_2= ventana[1]
    
    for i in range(0,len(fila_1),1):
        if(fila_1[i] != fila_2[i]):
            es = False
    return es

def ventanaTieneMasDeUno(ventana):
    cont_1 = 0
    cont_2 = 0
    seCumple = False
    esEstado = re.compile("q[0-9]*")
    fila_1= ventana[0]
    fila_2= ventana[1]
    for i in range(0,len(fila_1),1):
        match = re.fullmatch(esEstado, fila_1[i])
        if(match):
            cont_1 += 1
        match = re.fullmatch(esEstado, fila_2[i])
        if(match):
            cont_2 += 1
    
    if(cont_1 > 1):
        if(cont_2 > 1):
            seCumple = True
            code = -3
            return seCumple,code
        else:
            seCumple = True
            code = -1
            return seCumple,code
    elif(cont_2 > 1):
        seCumple = True
        code = -2
        return seCumple,code
    
    seCumple = False
    code = 0
    return seCumple, code

def ventanaNoSentido(ventana):
    # tiene estado en el medio de la primera fila y en la segunda no (no esta ni a su derecha ni a su izq ni en la misma posicion)
    seCumple = True
    fila_1= ventana[0]
    fila_2= ventana[1]
    
    esEstado = re.compile("q[0-9]*")
    match = re.fullmatch(esEstado, fila_1[1])
    if(match):
        for a in fila_2:    
            match = re.fullmatch(esEstado, a)
            if(match):
                seCumple = False
    else:
        seCumple = False
        return seCumple
    
    return seCumple

def ventanaTransicion(ventana, transiciones, fila, j): 
    filasPosibles = generarFilas(fila, transiciones)
    fila_2 = ventana[1]
    code = -5 #2 o  si no tiene ninguna-5
    numPosibles=1
    for fila in filasPosibles:
        #print('caso numero = '+ str(numPosibles))
        es = True
        cont=0
        for i in range(j,j+3,1):
            #print('en ventana = '+ str(fila_2[cont]) +' en la fila = ' + str(fila[i-2]))
            if(fila_2[cont] != fila[i-2]):
                es = False
            cont += 1
        if(es):
            code = 2
            return code
        #print('valor de j = '+str(j))
        numPosibles += 1
    return code

def esLegal(tabla, transiciones, i, j):
    fila, ventana = cogerVentana(tabla, i, j)

    code = 0
    #  = 1 si es igual
    if (ventanaEsIgual(ventana)):
        code = 1
        return code
    #  = -1 tiene mas de un estado en la primera fila
    #  = -2 si es en la segunda
    #  = -3 si es en las dos
    seCumple, code = ventanaTieneMasDeUno(ventana)
    if(seCumple):
        return code
    #  = -4 tiene estado en el medio de la primera fila y en la segunda no (no esta ni a su derecha ni a su izq ni en la misma posicion)
    elif(ventanaNoSentido(ventana)):
        code = -4
    #  = 2 si por transicion es congruente
    #  = -5 es incongruente por transicion
    else:
        code = ventanaTransicion(ventana, transiciones, fila, j)
    return code


