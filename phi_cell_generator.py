####################################################################################################
####################################     PHI_CELL     ##############################################
####################################################################################################

def generarPrimeraParte(i,j,valor,valoresPosibles):
    #como minimo cada celda debe tener un valor.
    primeraParte = "[ ("
    primeraParteValor = "[ ("
    estaBien = False
    tam = len(valoresPosibles)
    for e in range(0,tam,1):
        if(e < tam-1):
            primeraParte += "X_" + str(i) +"_" + str(j) + "_" + valoresPosibles[e] + " OR " 
            if(valoresPosibles[e] == valor):
                estaBien = True
                primeraParteValor += "TRUE OR "
            else:
                primeraParteValor += "FALSE OR "
        else:
            primeraParte += "X_" + str(i) +"_" + str(j) + "_" + valoresPosibles[e] + " ) "
            if(valoresPosibles[e] == valor):
                estaBien = True
                primeraParteValor += "TRUE ) "
            else:
                primeraParteValor += "FALSE ) "

    return primeraParte, primeraParteValor, estaBien

def generarSegundaParte(i,j,valor,valoresPosibles):
    segundaParte = "( " 
    segundaParteValor = "( " 
    estaBien = True
    
    #no pueden haber dos valores simultaneamente
    tam = len(valoresPosibles)
    for index in range(0, tam-1, 1):
        numNext = index + 1
        s = valoresPosibles[index]
        for numNext in range(numNext, tam, 1):
            t = valoresPosibles[numNext]
            #print("s = " +s+ " t =" + t + " index = "+ str(index) + " numNext = "+ str(numNext))
            if(t != s):
                valorS = (s == valor)
                valorT = (t == valor)

                if(valorS == valorT == True):
                    #print("Segunda parte: falla con valores i="+str(i)+" j="+str(j)+" valor en la tabla="+valor)
                    #print("valor de s = "+ s + "valor de t = "+ t)
                    estaBien = False

                if index < tam-2:
                    segundaParte += " NOT ("+ "X_"+ str(i)+"_"+str(j)+"_"+s + ") OR  NOT ( " + "X_"+ str(i)+"_"+str(j)+"_"+ t +")  ) AND ( "
                    segundaParteValor += " NOT ("+ str(valorS) + ") OR  NOT ( " + str(valorT) +")  ) AND ( "
                else:
                    segundaParte += " NOT ("+ "X_"+ str(i)+"_"+str(j)+"_"+s + ") OR  NOT ( " + "X_"+ str(i)+"_"+str(j)+"_"+ t +")  ) ]"
                    segundaParteValor += " NOT ("+ str(valorS) + ") OR  NOT ( " + str(valorT) +")  ) ]"
    
    return segundaParte, segundaParteValor, estaBien

def generarPhiCell(tabla, n, estados, alfabetoCinta):
    phi_cell=""
    phi_cell_valores = ""
    valoresPosibles = estados + alfabetoCinta + ["#"]    #conjunto de valores posibles (en la nomenclatura de la asignatura se llama "C")
    valorTotal = True

    for i in range(0,n,1):
        for j in range(0,n,1):
            primeraParte, primeraParteValor, estaBien = generarPrimeraParte(i+1,j+1,tabla[i][j],valoresPosibles)
            valorTotal = estaBien
            #print("PRIMERA PARTE DE LA FORMULA, ESTABIEN = " + str(estaBien))
            phi_cell += primeraParte + " AND "
            phi_cell_valores += primeraParteValor + " AND "
            segundaParte, segundaParteValor, estaBien = generarSegundaParte(i+1,j+1,tabla[i][j],valoresPosibles)
            valorTotal = estaBien
            #print("SEGUNDA PARTE DE LA FORMULA, ESTABIEN = " + str(estaBien))
            if( j == n-1 and i == n-1): #Estoy en el ultimo caso
                phi_cell += segundaParte 
                phi_cell_valores += segundaParteValor 
                
            else:
                phi_cell += segundaParte + " AND "
                phi_cell_valores += segundaParteValor + " AND "

    return  phi_cell, phi_cell_valores, valorTotal

#funcion para la explicacion de phi_cell
def generarPhiCell_soloUna(tabla, estados, alfabetoCinta, i, j):
    #por como pido los datos al usuario:
    i = i-1
    j = j-1
    phi_cell_min="[ "
    phi_cell_min_valores = "[ "
    valoresPosibles = estados + alfabetoCinta + ["#"]    #conjunto de valores posibles (en la nomenclatura de la asignatura se llama "C")
    
    primeraParte, primeraParteValor, estaBien = generarPrimeraParte(i+1,j+1,tabla[i][j],valoresPosibles)
    #print("PRIMERA PARTE DE LA FORMULA, ESTABIEN = " + str(estaBien))
    phi_cell_min += primeraParte + " AND "
    phi_cell_min_valores += primeraParteValor + " AND "

    segundaParte, segundaParteValor, estaBien = generarSegundaParte(i+1,j+1,tabla[i][j],valoresPosibles)
    #print("SEGUNDA PARTE DE LA FORMULA, ESTABIEN = " + str(estaBien))

    phi_cell_min += segundaParte  + " ]"
    phi_cell_min_valores += segundaParteValor + " ]"


    return  phi_cell_min, phi_cell_min_valores, primeraParte, segundaParte