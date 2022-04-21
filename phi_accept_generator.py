
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

