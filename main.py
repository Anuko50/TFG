import sys
from os import system, name
import re
import execute_controller
import cookLevin
import turing2utf
import time
import informationToTxt
import explicaciones


####################################################################################################
####################################     FUNCIONES :  ##############################################
####################################################################################################

#FUNCION PARA LEER LA MT EN TXT
def read_file(file_name):
    config = {}
    transition = {}
    aux = 0
    """ file_name = sys.argv[1]
    file_name = str(file_name) """

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print('El archivo introducido en la entrada no existe')
        exit()
    
    for i in range(1, 8):
        content = file.readline().strip('\n').split(' ')
        config[i] = content
    for i in file:
        aux = aux + 1
        transition[aux] = i.strip('\n').split(' ')
    return config, transition

# LEE LA ENTRADA
def read_tapes():
    tape = sys.argv[2]
    return tape

# poner color en el texto para imprimir por pantalla
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# borrar la pantalla
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


####################################################################################################
####################################     MAIN :    #################################################
####################################################################################################

# main MT.jff tape o 
# main MT.txt tape
def main(): 
    # veo si la entrada es correcta
    if (len(sys.argv) != 3):
        print("Parámetros insuficientes. USO: [MT en .txt o .jff] [entrada de la MT]")
        sys.exit(1)
        
    #ver que tipo de entrada se trata:
    #si debo, pasar de MT en jflap a texto 
    print(str(sys.argv[1]))
    c=str(sys.argv[1])
    esMT = re.compile("(.*)(\.jff)")
    validez = re.compile("(.*)(\.jff|\.txt)")
    esValido = re.fullmatch(validez, c)
    match = re.fullmatch(esMT, c)
    nombreMT = ""

    if(esValido):
        nombreMT = esValido.group(1)
    else:
        print("El archivo introducido no tiene una extension válida debe ser un .txt o un .jff")
        sys.exit(1)

    # en la variable "name" va a estar la máquina de Turing en texto
    if(match):
       name = match.group(1) + ".txt"
       converter = turing2utf.Jflap2Utfpr()
       converter.convert(sys.argv[1], name)
    else: 
        name = str(sys.argv[1])



    # 2º ejecutarla para sacar la tabla
    """ valores de config:
    # linea 1: alfabeto de entrada
    # linea 2: alfabeto de la cinta
    # linea 3: simbolo que representa un espacio en blanco en la cinta
    # linea 4: conjunto de estados totales
    # linea 5: estado inicial
    # linea 6: conjunto de estados finales
    # linea 7: cantidad de fitas """

    """ valores de transitions:
    ['estado_actual', 'estado_nuevo', 'simbolo_Actual', 'Nuevo_Simbolo', 'direccion']  """

    config = {}
    transitions = {}
    tape = []
    config, transitions = read_file(name)
    tape = read_tapes()
    # 3º volcar cada configuración intermedia desde la inicial hasta la final en el tablón.


    #CARACTERISTICAS DE LA MT: 
    # nombre, determinista o no, stay o no, estadoInicial, Blanco, estadosTot, estadosFinales y la entrada
    noDeterminista = execute_controller.isNonDeterministic(transitions, config)
    esStay = execute_controller.esStay(transitions)
    estadoInicial = 'q' + str(config[5][0]) 
    blanco = config[3][0]
    estadosTotales = execute_controller.estadosEnBonito(config[4])
    estadosFinales = execute_controller.estadosEnBonito(config[6])
    entrada = sys.argv[2]

    #Lo escribo en un fichero de salida:
    informationToTxt.caracteristicasToTxt(nombreMT, noDeterminista, esStay, estadoInicial, blanco, estadosTotales, estadosFinales, entrada)
    # ejecutar la maquina
    n, tabla, reglas_en_orden = execute_controller.controller(config, tape, transitions, noDeterminista)

    if (tabla is not None):
        informationToTxt.tablonToTxt(nombreMT, execute_controller.transicionesEnBonito(reglas_en_orden) , entrada, tabla, n)
    else: 
        print(colored(255,0,0, 'No se ha podido crear la tabla debido a que se ha excedido el número máximo de pasos de cálculo.'))
        print(colored(255,0,0, 'Se procede a cerrar el programa.'))
        sys.exit(1)


    inicio = time.time()
    # 4º aplicar algoritmo de Cook-Levin
    configuracionInicial = execute_controller.crearConfiguracionInicial(sys.argv[2], config[5][0], n, config[3][0])
    alfabetoCinta = config[2]
    #print(configuracionInicial)
    #print("\n APLICACION DE COOK-LEVIN:")
    #Aplicamos Cook-Levin
    phi, phi_start, phi_accept, phi_cell, phi_move = cookLevin.apply(n, tabla, estadosTotales, alfabetoCinta, configuracionInicial, estadosFinales, reglas_en_orden, transitions)
    
    informationToTxt.phi_startToTxt(nombreMT, phi_start, entrada)
    informationToTxt.phi_acceptToTxt(nombreMT, phi_accept, entrada)
    informationToTxt.phi_cellToTxt(nombreMT, phi_cell, entrada)
    informationToTxt.phi_moveToTxt(nombreMT, phi_move, entrada)
    informationToTxt.phiToTxt(nombreMT, phi_start, phi_accept, phi_cell, phi_move, entrada)

    #TODO: TABLON, PHIS (+ SU VALOR), CARACTERISTICAS DE LA MT A .TXT
    # 5º contabilizar si el tiempo de estas máquinas es polinomial
    fin = time.time()
    print("\nTIEMPO DE EJECUCIÓN TOTAL: ")
    print(fin - inicio)
    
    explicaciones.mainloop(phi_start, phi_accept, phi_cell, phi_move, tabla, n, estadosFinales, entrada, estadosTotales, alfabetoCinta, transitions)
   
main()