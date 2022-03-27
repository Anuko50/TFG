import sys
import re
import execute_controller
import turing2utf

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
    match = re.fullmatch(esMT, c)

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
# ejecutar la maquina
    execute_controller.controller(config, tape, transitions)
# 4º aplicar algoritmo de Cook-Levin
# 5º contabilizar si el tiempo de estas máquinas es polinomial
    
 





main()