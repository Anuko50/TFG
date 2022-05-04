

#solo si la lista es de strings
def listToStr(list):
    str =  " ".join(list)
    return str

def listToStr2(list):
    str = "  ".join(list)
    return str

def caracteristicasToTxt(nombreDeMT, noDeterministic, stay, estadoInicial, blanco, estadosTot, estadosFinales, entrada):
    outputFile = nombreDeMT + "_Caracteristicas.txt"
    with open(outputFile, 'w') as f:
        f.write( 'CARACTERISTICAS DE LA MÁQUINA DE TURING '+ nombreDeMT + '\n')
        if(noDeterministic):
            f.write("Es una MT no determinista MTND." + '\n')
        else:
           f.write("Es una MT determinista." + '\n')
        if(stay):
            f.write("Es una MT con transiciones Stay. Esto quiere decir que a parte de las transiciones a la derecha o a la izquierda, esta MT puede quedarse inmovil." + '\n')
        else: 
            f.write("Es una MT sin transiciones Stay. Esto quiere decir solo dispone de las transiciones a la derecha o a la izquierda." + '\n')
        f.write("Estado Inicial = " + estadoInicial + '\n')
        f.write("Símbolo blanco = " + blanco + '\n')
        f.write("Los estados totales son = " + listToStr(estadosTot) + '\n')
        f.write("Los estados finales son = " + listToStr(estadosFinales) + '\n')
        f.write("La entrada/palabra que se ha introducido al ejecutar la MT es = \'" + entrada + '\'\n')
    
    f.close()


def tablonToTxt(nombreDeMT, reglasEnOrden, palabra, tabla, n):
    outputFile = nombreDeMT + "_Tablon_e_informacion_palabra_"+palabra+".txt"
    with open(outputFile, 'w') as f:
        f.write( 'Las reglas que han sido utilizadas en la ejecución de la MT han sido: '+'\n \n')
        for regla in reglasEnOrden:
            f.write(listToStr(regla)+'\n')
        f.write('\n')
        f.write('Tablón final con la palabra \''+palabra+'\': \n \n')
        for fila in tabla:
            f.write(listToStr2(fila)+'\n')
        f.write('\n')
        f.write('La tabla final es de tamaño '+str(n)+ 'X'+ str(n)+'\n')
    
    f.close()

def phi_startToTxt(nombreDeMT, phi_start, palabra, phi_start_valores, valorTotal_phi_start):
    outputFile = nombreDeMT + "_phi_start_palabra_\'"+palabra+"\'.txt"
    with open(outputFile, 'w') as f:
        f.write('VALOR TOTAL DE LA FÓRMULA = ' + str(valorTotal_phi_start)+'\n')
        f.write('Fórmula phi_start creada con la palabra \''+palabra+'\': \n\n')
        f.write(phi_start +'\n\n')
        f.write('Fórmula phi_start (con los valores asignados) creada con la palabra \''+palabra+'\': \n\n')
        f.write(phi_start_valores +'\n\n')
    f.close()

def phi_acceptToTxt(nombreDeMT, phi_accept, palabra, phi_accept_valores, valorTotal_phi_accept):
    outputFile = nombreDeMT + "_phi_accept_palabra_\'"+palabra+"\'.txt"
    with open(outputFile, 'w') as f:
        f.write('VALOR TOTAL DE LA FÓRMULA = ' + str(valorTotal_phi_accept)+'\n')
        f.write('Fórmula phi_accept creada con la palabra \''+palabra+'\': \n\n')
        f.write(phi_accept +'\n\n')
        f.write('Fórmula phi_accept (con los valores asignados) creada con la palabra \''+palabra+'\': \n\n')
        f.write(phi_accept_valores +'\n\n')
    f.close()

def phi_cellToTxt(nombreDeMT, phi_cell, palabra, phi_cell_valores, valorTotal_phi_cell):
    outputFile = nombreDeMT + "_phi_cell_palabra_\'"+palabra+"\'.txt"
    with open(outputFile, 'w') as f:
        f.write('VALOR TOTAL DE LA FÓRMULA = ' + str(valorTotal_phi_cell)+'\n')
        f.write('Fórmula phi_cell creada con la palabra \''+palabra+'\': \n\n')
        f.write(phi_cell +'\n\n')
        f.write('Fórmula phi_cell (con los valores asignados) creada con la palabra \''+palabra+'\': \n\n')
        f.write(phi_cell_valores +'\n\n')
    f.close()

def phi_moveToTxt(nombreDeMT, phi_move, palabra, phi_move_valores, valorTotal_phi_move):
    outputFile = nombreDeMT + "_phi_move_palabra_\'"+palabra+"\'.txt"
    with open(outputFile, 'w') as f:
        f.write('VALOR TOTAL DE LA FÓRMULA = ' + str(valorTotal_phi_move)+'\n')
        f.write('Fórmula phi_move creada con la palabra \''+palabra+'\': \n\n')
        f.write(phi_move +'\n\n')
        f.write('Fórmula phi_cell (con los valores asignados) creada con la palabra \''+palabra+'\': \n\n')
        f.write(phi_move_valores +'\n\n')
    f.close()

def phiToTxt(nombreDeMT, phi_start, phi_accept, phi_cell, phi_move , palabra, phi, valorTotal_phi):
    outputFile = nombreDeMT + "_phi_palabra_\'"+palabra+"\'.txt"
    with open(outputFile, 'w') as f:
        f.write('VALOR TOTAL DE LA FÓRMULA = ' + str(valorTotal_phi)+'\n')
        f.write('Fórmula phi creada con la palabra \''+palabra+'\': \n')
        f.write('Se expone a trozos para mayor claridad, primero phi_start, luego accept, cell y move al final. \n\n')
        f.write("[ "+phi_start +' ]\n\n')
        f.write(' AND \n\n')
        f.write("[ "+phi_accept +' ]\n\n')
        f.write(' AND \n\n')
        f.write("[ "+phi_cell +' ]\n\n')
        f.write(' AND \n\n')
        f.write("[ "+phi_move +' ]\n\n')
        f.write("FÓRMULA COMPLETA (seguida)=  \n\n")
        f.write(phi +'\n\n' )
        f.close()