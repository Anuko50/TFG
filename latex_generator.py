import re
import codecs
import phi_move_generator

#solo si la lista es de strings
def listToStr(list):
    str =  " ".join(list)
    return str

def listToStr2(list):
    str = "  ".join(list)
    return str


##################################################################
################### LATEX DEL TABLON #############################
##################################################################
def  crear_eles_tabuladas(n):
    eles = '|'
    for i in range(0,n,1):
        eles+='l|'
    return eles

def tablonAlterado(nombreDeMT, tablon_alterado, n, transiciones, blanco, simbolosPosibles):
    #outputFile = nombreDeMT+ "_tablon_alterado.tex"
    outputFile = "tablon_alterado.tex"
    
    with codecs.open(outputFile, 'w', "utf-8-sig") as f:
        #Cosas que importar de manera genérica
        f.write('\\documentclass[a4paper,10pt]{article}\n')
        f.write('\\usepackage[utf8]{inputenc}\n')
        f.write('\\usepackage[spanish,es-tabla]{babel}\n')
        #márgenes del documento
        f.write('\\usepackage[top=3cm, bottom=2cm, right=1.5cm, left=3cm]{geometry}\n')
        f.write('\\usepackage[usenames,dvipsnames,svgnames,table]{xcolor}\n\n')
        # Definimos el título
        f.write('\\title{Tablón Alterado}\n')
        f.write('\\author{'+nombreDeMT+'}\n')
        f.write('\\date{}\n\n')
        #comienzo del documento:
        f.write('\\begin{document}\n')
        f.write('\\maketitle\n\n')


        #####################################################
        ######  tablon alterado, mostrar la tabla ###########
        #####################################################
        f.write('\\section{Tabla alterada}\n\n')
        f.write('Aquí mostraremos la tabla alterada de manera aleatoria. Lo que se puede encontrar es que:\n')
        f.write('\\begin{itemize}\n')
        f.write('\\item Se haya introducido un carácter que no pertenece al conjunto C.\n')
        f.write('\\item Se haya cambiado un carácter a otro perteneciente al conjunto C.\n')
        f.write('\\item Se haya cambiado la primera fila por otra aleatoria del tablón.\n')
        f.write('\\item Se haya añadido un estado de más.\n')
        f.write('\\item Eliminar estados para quitar el sentido del tablón, cambiándolos por otro signo.\n')
        f.write('\\end{itemize}')
        
        f.write('\\begin{table}[h]\n')
        f.write('\\centering\n')
        eles = crear_eles_tabuladas(n)
        f.write('\\begin{tabular}{'+eles+'}\n')
        f.write('\\hline\n')
        
        esEstado = re.compile("q[0-9]*")
        esHastag = re.compile("#")
        fila_tabla = '\t'

        for i in range(0,n,1):
            for j in range (0,n,1):
                celda = tablon_alterado[i][j]
                match = re.fullmatch(esEstado, celda)
                match_hastag = re.fullmatch(esHastag, celda)
                if(j < n-1):
                    if(match):
                        fila_tabla += celda +'  &   '
                    elif(match_hastag):
                        fila_tabla += '\\#' +'  &   '
                    else:
                        fila_tabla += celda +'   &   '
                else:
                    if(match):
                        fila_tabla += celda + '\t'
                    elif(match_hastag):
                        fila_tabla += '\\#' + '\t'
                    else:
                        fila_tabla += celda + '\t'

            f.write(fila_tabla + '\\\\ \\hline\n')
            fila_tabla = '\t'
  
        f.write('\\end{tabular}\n')
        f.write('\\end{table}\n')
        

        #####################################################
        ##########  MOSTRAR LAS VENTANAS ILEGALES ###########
        #####################################################

        f.write('\\section{Ventanas ilegales}\n')
        f.write('En este apartado se mostrarán las ventanas ilegales que nacen del tablón alterado.\\newline')
        ilegales = phi_move_generator.encontrarIlegales(tablon_alterado, n, transiciones, blanco, simbolosPosibles)
        ventanas = ilegales['ventana']
        mensajes = ilegales['mensaje']
        posiciones = ilegales['posicion']

        for i in range(0, len(ventanas), 1):
            f.write('\\begin{table}[h!]\n')
            f.write('\\centering\n')
            eles = crear_eles_tabuladas(3)
            f.write('\\begin{tabular}{'+eles+'}\n')
            f.write('\\hline\n')

            esEstado = re.compile("q[0-9]*")
            esHastag = re.compile("#")

            ventana_actual = ventanas[i]
            fila_1 = ventana_actual[0]
            fila_2 = ventana_actual[1]
            mensaje_actual = mensajes[i]
            posicion_actual = posiciones[i]
            fila_tabla_1 = '\t'
            fila_tabla_2 = '\t'

            for i in range(0, len(fila_1), 1):
                celda_1 = fila_1[i]
                celda_2 = fila_2[i]
                match_1 = re.fullmatch(esEstado, celda_1)
                match_2 = re.fullmatch(esEstado, celda_2)
                match_hastag_1 = re.fullmatch(esHastag, celda_1)
                match_hastag_2 = re.fullmatch(esHastag, celda_2)
                if(i < len(fila_1)-1):
                    if(match_1):
                        fila_tabla_1 += celda_1 +'  &   '
                    elif(match_hastag_1):
                        fila_tabla_1 += '\\#' +'  &   '
                    else:
                        fila_tabla_1 += celda_1 +'   &   '
                        
                    if(match_2):
                        fila_tabla_2 += celda_2 +'  &   '
                    elif(match_hastag_2):
                        fila_tabla_2 += '\\#' +'  &   '
                    else:
                        fila_tabla_2 += celda_2 +'   &   '
                else:
                    if(match_1):
                        fila_tabla_1 += celda_1 + '\t'
                    elif(match_hastag_1):
                        fila_tabla_1 += '\\#' + '\t'
                    else:
                        fila_tabla_1 += celda_1 + '\t'
                    
                    if(match_2):
                        fila_tabla_2 += celda_2 + '\t'
                    elif(match_hastag_2):
                        fila_tabla_2 += '\\#' + '\t'
                    else:
                        fila_tabla_2 += celda_2 + '\t'

            fila_tabla_1 += '\\\\ \\hline\n'
            fila_tabla_2 += '\\\\ \\hline\n'
        
            f.write(fila_tabla_1)
            f.write(fila_tabla_2)
            f.write('\\end{tabular}\n')
            f.write('\\end{table}\n')
            f.write('\n')
            f.write('Se trata de la ventana cuya casilla central superior es la celda de la fila '+ str(posicion_actual[0])+ ' y columna ' + str(posicion_actual[1])+'\\newline\n')
            f.write(mensaje_actual+'\\newline\n')



        #fin del documento:
        f.write('\\end{document}\n')

    f.close()

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
        f.write('Fórmula phi_move (con los valores asignados) creada con la palabra \''+palabra+'\': \n\n')
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
        f.write("[ "+phi_move +' ]\n\n\n\n')
        f.write("FÓRMULA COMPLETA (seguida)=  \n\n")
        f.write(phi +'\n\n' )
    f.close()

