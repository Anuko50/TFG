####################################################################################################
####################################     PHI_START    ##############################################
####################################################################################################

def generarPhiStart(n, tabla, proposicionesPotenciales, configuracionInicial):
    phiStart=""
    phiStart_valores=""
    valorTotal = True

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
                valorTotal = False
        else:
            if(configuracionInicial[j] == tabla[0][j]):
                phiStart_valores += "TRUE "
            else:
                phiStart_valores += "FALSE "
                valorTotal = False

    return phiStart, phiStart_valores, valorTotal
