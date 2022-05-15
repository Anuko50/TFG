
####################################################################################################
####################################     PHI_ACCEPT   ##############################################
####################################################################################################

def loContiene(estadosFinales, celda):
    for q in estadosFinales:
        if(q == celda):
            return True
    return False

def crearLiteralesFinales(estadosFinales, n):
    literalesFinales = []
    literalesFinales_latex=[]
    for i in range(1,n-1,1):
        for j in range(1,n-1,1):
            for q in estadosFinales:
                numero = q[1]
                literal_latex = '$X_'+str(i)+',_'+str(j)+'\\_q_'+numero+'$'
                literal = 'X'+str(i)+'_'+str(j)+'_'+q
                literalesFinales.append(literal)
                literalesFinales_latex.append(literal_latex)
    return literalesFinales, literalesFinales_latex

def generarPhiAccept(tabla, estadosFinales, n):
    #asegura que qaccept aparezca
    #en alguna celda. (QUE HAYA ESTADO FINAL EN ALGUNA CELDA, LA QUE SEA)
    literalesFinales, literalesFinales_latex = crearLiteralesFinales(estadosFinales, n) 
    tam = len(literalesFinales)
    loCumple = False
    phi_accept_latex = ''
    fi_Accept=""
    fi_Accept_valores=""

    for i in range(0,tam,1):
        if(i< tam-1):
            phi_accept_latex += literalesFinales_latex[i]+'\\ OR\\ '
            fi_Accept += literalesFinales[i] + ' OR '
        else:
            phi_accept_latex += literalesFinales_latex[i]
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

    return fi_Accept, fi_Accept_valores, loCumple, phi_accept_latex

