import re

####################################################################################################
####################################     PHI_START    ##############################################
####################################################################################################

def generarPhiStart(n, tabla, proposicionesPotenciales, configuracionInicial):
    phi_start_latex=''
    phiStart=""
    phiStart_valores=""
    valorTotal = True

    esEstado = re.compile("q[0-9]*")
    eshastag= re.compile("#")

    for j in range(0,n,1):
        match = re.fullmatch(esEstado, configuracionInicial[j])
        match_hastag = re.fullmatch(eshastag, configuracionInicial[j])
        if(j < n-1):
            if(match):
                num_estado = configuracionInicial[j][1]
                phi_start_latex += "$X_1,_"+ str(j+1)+"\\_q_"+num_estado+"$\\ AND\\ "
            elif(match_hastag):
                phi_start_latex += "$X_1,_"+ str(j+1)+"\\_\\"+configuracionInicial[j]+"$\\ AND\\ "
            else:
                phi_start_latex += "$X_1,_"+ str(j+1)+"\\_"+configuracionInicial[j]+"$\\ AND\\ "

            phiStart += "X_1_"+ str(j+1)+"_"+configuracionInicial[j]+" AND "
        else:
            if(match):
                num_estado = configuracionInicial[j][1]
                phi_start_latex += "$X_1,_"+ str(j+1)+"\\_q_"+num_estado+"$\\ "
            elif(match_hastag):
                phi_start_latex += "$X_1,_"+ str(j+1)+"\\_\\"+configuracionInicial[j]+"$\\ "
            else:
                phi_start_latex += "$X_1,_"+ str(j+1)+"\\_"+configuracionInicial[j]+"$\\ "

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

    return phiStart, phiStart_valores, valorTotal, phi_start_latex
