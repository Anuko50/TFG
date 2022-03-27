#def isNonDeterministic(config, tape, transitions):
from distutils.command.config import config
import execute_MT
import execute_MTND
import execute_MTND_VIEJO

def calcularTamanyoTabla(filas_tabla):
    tamFinal = len(filas_tabla)
    for fila in filas_tabla:
        #Split me separa los elementos de un string en diferentes elementos en una lista, delimitados por espacio
        tamNuevo = len(fila.split())
        if  tamNuevo > tamFinal : 
            #print('tamaño fila: '+ str(tamNuevo))
            #print('tamaño que estba: '+ str(tamFinal))
            tamFinal = tamNuevo
    
    return tamFinal +2  # el +2 contempla los "#"

def crearTabla(filas_tabla, blanco):
    n = calcularTamanyoTabla(filas_tabla) 
    tabla = [[0] * n for i in range(n)] #inicializo la tabla
    fila=0
    for cinta in filas_tabla:
        #Estoy dentro una configuracion dentro de la tabla
        meter = cinta.split()
        contMeter=0
        #print(meter)
        for i in range(0, n ,1):
            if (i==0 or i==n-1):
                tabla[fila][i] = '#'
            else:
                if(contMeter < len(meter)):
                    tabla[fila][i] = meter[contMeter]
                    contMeter += 1
                else:
                    tabla[fila][i] = blanco
        fila+=1
    
    return tabla


#Crear una fila de la tabla para el algoritmo desde la cinta actual y el setting
def crearFilaTabla(tape, setting):
    filaTabla=""
    cont = 0
    #print(tape)
    for j in tape:
        if(setting.get("head_tape") == cont):
            filaTabla += 'q' +setting.get("current_state")+' '
        filaTabla +=  j+ ' '
        cont = cont + 1
    return filaTabla

def isNonDeterministic(transitions, config):
    #Las transiciones son un diccionario cuya key es el orden de la transicion empezando en uno
    # lo cual me es cómodo porque puedo iterar, pero quiero ver si se repite algo...
    """ En el diccionario (transitions) vamos a tener en value: 
    ['estado_actual', 'estado_nuevo', 'simbolo_Actual', 'Nuevo_Simbolo', 'direccion'] 
    Querremos ver de la key i el valor [0] (estado actual) y el [2] (simbolo actual);
    Si dentro de las transiciones se repite alguno, es una MTND"""
    estado_actual= -1
    simbolo_actual = -1
    blanco = config[3][0]
    
    for i in range(1, len(transitions) + 1, 1):
        estado_actual = transitions[i][0] 
        simbolo_actual = transitions[i][2] 
        
        for j in range(i+1, len(transitions) + 1, 1): #lo comparo con los demas
            if(transitions[j][0] == estado_actual):
                if(transitions[j][2] == simbolo_actual):   
                    #print('Estado actual = '+ estado_actual + ' ; Lo comparo con estado = ' + transitions[j][0] )
                    #print('Simbolo actual = '+ simbolo_actual + ' ; Lo comparo con simbolo = ' + transitions[j][2] ) 
                    return True
    return False

""" Esta funcion sirve como controlador para ejecutar la MT segun sea no determinista o sí. 
Una vez se ejecute se llamara a la creación de la tabla. """
def controller(config, tape, transitions):

    filas_tabla = [] #lista donde vamos a guardar las filas de la tabla
    reglas_utilizadas_en_orden = [] #Lista donde se van a guardar las reglas de transicion aplicadas en orden de fila

    
    if(isNonDeterministic(transitions, config)):
        #print('es no determinista, aun no he hecho esa parte')
        #execute_MTND_VIEJO.execute(config, tape, transitions, filas_tabla, reglas_utilizadas_en_orden)
        execute_MTND.execute(config, tape, transitions, filas_tabla, reglas_utilizadas_en_orden)
    else:
        execute_MT.machine(config, tape, transitions, filas_tabla, reglas_utilizadas_en_orden) 
        #print(filas_tabla)
        #print(reglas_utilizadas_en_orden)

    blanco = config[3][0]   # simbolo blanco que se va a utilizar
    tabla = crearTabla(filas_tabla, blanco)
    
    print("TABLA: ")
    print(" ")
    for fila in tabla:
        print(fila)
    print(" ")
    print("REGLAS: ")
    print(" ")
    print(reglas_utilizadas_en_orden)