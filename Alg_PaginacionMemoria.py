# Algorito de Reemplazo de Paginas
# Desarrollado: Jorge Antonio Hernandez


# Algoritmo de reemplazo de páginas que emula la ejecución de este proceso 
# para decidir qué páginas pueden ser sacadas de memoria cuando se necesita 
# cargar una nueva y ya no hay marcos libres.


import os
import matplotlib.pyplot as plt
import numpy as np

# ========================================= IMPRIMIR GRAFICA =========================================

def funcion_grafica(CONTADOR_FALLOS,MATRIZ_CAMBIOS, NUMERO_DE_MARCOS):
    

    MATRIZ_CAMBIOS = np.array(MATRIZ_CAMBIOS, dtype="<U11")
    MATRIZ_CAMBIOS = MATRIZ_CAMBIOS.astype(float)

    print("-------------------------------------------------------------------")
    print("Número de fallos de página:", CONTADOR_FALLOS)
    print("--------------- TABLA CON LOS REEMPLAZOS DE PAGINA ---------------------")
    for i in range(len(MATRIZ_CAMBIOS[0])):
        for j in range(len(MATRIZ_CAMBIOS)):
            print(str(MATRIZ_CAMBIOS[j][i]) + "\t", end="")
        print("")
    print("-------------------------------------------------------------------")
    plt.imshow(MATRIZ_CAMBIOS, cmap='binary')
    plt.xticks(range(NUMERO_DE_MARCOS))
    plt.xlabel("Marcos de página")
    plt.ylabel("Solicitudes de proceso")
    plt.title("Proceso de cambio de página")
    plt.show()

# ========================================= IMPRIMIR MATRIZ DE PROCESOS =========================================

def imp_matrizProcesos(MEMORIA_RAM):
    print(">> Contenido de Memoria: ", MEMORIA_RAM)

# ========================================= SECCION DEL FIFO =========================================

def Alg_FIFO():
    while True:
        os.system ("cls")
        print("Desea usar el ejemplo preconfigurado o ingresar los valores manualmente?")
        print("1: Ingresar Valores Manuales")
        print("2: Usar Valores Preconfigurados")
        opc = int(input())
        if opc == 1:
            NUMERO_DE_MARCOS = int(input("Ingrese la cantidad de marcos en la memoria física: "))
            PAGINAS = input("Ingrese el orden de solicitud de los procesos separados por comas: (Ingrese solo numeros) ").split(',')
            break
        elif opc == 2:
            NUMERO_DE_MARCOS = 3
            PAGINAS = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
            break

    os.system ("cls")
    MEMORIA_RAM = [-1] * NUMERO_DE_MARCOS
    print("=========================================================================")
    print("Informacion de los procesos a emular:")
    print(">> Contenido de Memoria: ", MEMORIA_RAM)
    print("Numero de Marcos: ",NUMERO_DE_MARCOS)
    print("Lista y Orden de procesos a emular: ",PAGINAS)
    print("Numero de secuencias de paginas: ",len(PAGINAS))
    print("=========================================================================")
    CONTADOR_FALLOS = 0
    print("\n")

    FIFO_order = []
    MATRIZ_CAMBIOS = []

    for pag in PAGINAS:
         print("Accediendo a la pagina:", pag)
         print("-------------------------------------------------------------------")
         if pag in MEMORIA_RAM:
              print("Fallo de Pagina No. :",CONTADOR_FALLOS)
              print("La página ya se encuentra cargada en la memoria")
              print(">> Contenido de Memoria: ", MEMORIA_RAM)
              print("-------------------------------------------------------------------")
              print("\n")
              MATRIZ_CAMBIOS.append(list(MEMORIA_RAM))
         else:
              if -1 in MEMORIA_RAM:
                   CONTADOR_FALLOS += 1
                   PROCESS = MEMORIA_RAM.index(-1)
                   MEMORIA_RAM[PROCESS] = pag
                   FIFO_order.append(PROCESS)
                   print("Fallo de Pagina No. :",CONTADOR_FALLOS)
                   print("La página se carga en el marco", PROCESS)
                   print(">> Contenido de Memoria: ", MEMORIA_RAM)
                   print("-------------------------------------------------------------------")
                   print("\n")
                   MATRIZ_CAMBIOS.append(list(MEMORIA_RAM))
                   
              else:
                   CONTADOR_FALLOS += 1      
                   PROCESS = FIFO_order.pop(0)
                   PAG_REEMP = MEMORIA_RAM[PROCESS]
                   MEMORIA_RAM[PROCESS] = pag
                   FIFO_order.append(PROCESS)
                   print("Fallo de Pagina No. :",CONTADOR_FALLOS)
                   print("La página", PAG_REEMP, "fue remplazada por ", pag, "en el marco", PROCESS)
                   print(">> Contenido de Memoria: ", MEMORIA_RAM)
                   print("-------------------------------------------------------------------")
                   print("\n")
                   MATRIZ_CAMBIOS.append(list(MEMORIA_RAM))

    print("Frecuencia: ",(CONTADOR_FALLOS/len(PAGINAS)))
    print("Rendimiento:",((1-(CONTADOR_FALLOS/len(PAGINAS)))*100),"%")
    funcion_grafica(CONTADOR_FALLOS,MATRIZ_CAMBIOS,NUMERO_DE_MARCOS)

# ================================ Seccion de segunda oportunidad
def segunda_oprtunidadReloj():
    while True:
        os.system ("cls")
        print("Desea usar el ejemplo preconfigurado o ingresar los valores manualmente?")
        print("1: Ingresar Valores Manuales")
        print("2: Usar Valores Preconfigurados")
        opc = int(input())
        if opc == 1:
            NUMERO_DE_MARCOS = int(input("Ingrese la cantidad de marcos en la memoria física: "))
            PAGINAS = input("Ingrese el orden de solicitud de los procesos separados por comas: (Ingrese solo numeros)  ").split(',')
            break
        elif opc == 2:
            NUMERO_DE_MARCOS = 3
            PAGINAS = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
            break
    
    os.system ("cls")
    MEMORIA_RAM = [-1] * NUMERO_DE_MARCOS
    VECTOR_REFERENCIA = [0] * NUMERO_DE_MARCOS
    print("=========================================================================")
    print("Informacion de los procesos a emular:")
    print(">> Contenido de Memoria: ", MEMORIA_RAM)
    print("Numero de Marcos: ",NUMERO_DE_MARCOS)
    print("Lista y Orden de procesos a emular: ",PAGINAS)
    print("Numero de secuencias de paginas: ",len(PAGINAS))
    print("=========================================================================")
    CONTADOR_FALLOS = 0
    print("\n")
    #MEMORIA_RAM = [-1] * NUMERO_DE_MARCOS
    #VECTOR_REFERENCIA = [0] * NUMERO_DE_MARCOS

    MATRIZ_CAMBIOS = []
    index = 0

    for PAG in PAGINAS:
        if PAG in MEMORIA_RAM:
            VECTOR_REFERENCIA[MEMORIA_RAM.index(PAG)]=1
        else:
            while True:
                if index == NUMERO_DE_MARCOS:
                    index = 0
                if VECTOR_REFERENCIA[index] == 0:
                    MEMORIA_RAM[index] = PAG
                    MATRIZ_CAMBIOS.append(list(MEMORIA_RAM))
                    VECTOR_REFERENCIA[index] = 1
                    CONTADOR_FALLOS += 1
                    index += 1
                    break
                VECTOR_REFERENCIA[index] = 0
                index += 1

        print("-------------------------------------------------------------------")
        print("Fallo de Pagina No. :",CONTADOR_FALLOS)
        print(">> Contenido de Memoria: ", MEMORIA_RAM)
    
    print("Frecuencia: ",(CONTADOR_FALLOS/len(PAGINAS)))
    print("Rendimiento:",((1-(CONTADOR_FALLOS/len(PAGINAS)))*100),"%")
    funcion_grafica(CONTADOR_FALLOS,MATRIZ_CAMBIOS, NUMERO_DE_MARCOS)


# ========================================= SECCION DEL LRU =========================================

def Alg_LRU():
    while True:
        os.system ("cls")
        print("Desea usar el ejemplo preconfigurado o ingresar los valores manualmente?")
        print("1: Ingresar Valores Manuales")
        print("2: Usar Valores Preconfigurados")
        opc = int(input())
        if opc == 1:
            NUMERO_DE_MARCOS = int(input("Ingrese la cantidad de marcos en la memoria física: "))
            PAGINAS = input("Ingrese el orden de solicitud de los procesos separados por comas: (Ingrese solo numeros) ").split(',')
            break
        elif opc == 2:
            NUMERO_DE_MARCOS = 3
            PAGINAS = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
            break

    os.system ("cls")
    MEMORIA_RAM = [-1] * NUMERO_DE_MARCOS
    ARRG_FRECUENCIA = [0] * NUMERO_DE_MARCOS

    print("=========================================================================")
    print("Informacion de los procesos a emular:")
    print(">> Contenido de Memoria: ", MEMORIA_RAM)
    print(">> Numero de Marcos: ",NUMERO_DE_MARCOS)
    print(">> Lista y Orden de procesos a emular: ",PAGINAS)
    print(">> Numero de secuencias de paginas: ",len(PAGINAS))
    print("=========================================================================")
    CONTADOR_FALLOS = 0
    print("\n")

    LRU_order = []
    MATRIZ_CAMBIOS = []

    for PAG in PAGINAS:
        print("Accediendo a la pagina:", PAG)
        print("-------------------------------------------------------------------")
        if PAG in MEMORIA_RAM:
            print("Fallo de Pagina No. :",CONTADOR_FALLOS)
            print("La página ya se encuentra cargada en la memoria")
            print(">> Contenido de Memoria: ", MEMORIA_RAM)
            print("-------------------------------------------------------------------")
            print("\n")
            PAG_SOLICITADA = MEMORIA_RAM.index(PAG)
            ARRG_FRECUENCIA[PAG_SOLICITADA] = 0
            MATRIZ_CAMBIOS.append(list(MEMORIA_RAM))
        else:
            if -1 in MEMORIA_RAM:
                CONTADOR_FALLOS += 1
                PROCESS = MEMORIA_RAM.index(-1)
                MEMORIA_RAM[PROCESS] = PAG

                ARRG_FRECUENCIA[PROCESS] = 0

                LRU_order.append(PROCESS)
                print("Fallo de Pagina No. :",CONTADOR_FALLOS)
                print("La página se carga en el marco", PROCESS)
                print(">> Contenido de Memoria: ", MEMORIA_RAM)
                print("-------------------------------------------------------------------")
                print("\n")
                MATRIZ_CAMBIOS.append(list(MEMORIA_RAM))
            else:
                CONTADOR_FALLOS += 1
                PROCESS = ARRG_FRECUENCIA.index(max(ARRG_FRECUENCIA))
                PAG_REEMP = MEMORIA_RAM[PROCESS]
                MEMORIA_RAM[PROCESS] = PAG
                LRU_order.append(PROCESS)
                ARRG_FRECUENCIA[PROCESS] = 0
                MATRIZ_CAMBIOS.append(list(MEMORIA_RAM))
                print("Fallo de Pagina No. :",CONTADOR_FALLOS)
                print("La pagina", PAG_REEMP, "fue remplazada por ", PAG, "en el marco", PROCESS)
                print(">> Contenido de Memoria: ", MEMORIA_RAM)
                print("-------------------------------------------------------------------")

        for c in range(NUMERO_DE_MARCOS):
            ARRG_FRECUENCIA[c] += 1;
    

    print("Frecuencia: ",(CONTADOR_FALLOS/len(PAGINAS)))
    print("Rendimiento:",((1-(CONTADOR_FALLOS/len(PAGINAS)))*100),"%")
    funcion_grafica(CONTADOR_FALLOS,MATRIZ_CAMBIOS, NUMERO_DE_MARCOS)
                
# ========================================= MENU DE EJECUCION =========================================

def menu():
    while True:
        os.system ("cls")
        print("===== Algoritmo de Simulacion De Paginacion De Memoria =====")
        print("\t 1: Algoritmo FIFO")
        print("\t 2: Algoritmo LRU")
        print("\t 3: Algoritmo SEGUNDA OPORTUNIDAD (Reloj)")
        print("\t 4: Salir")
        opcion = int(input("=> "))

        if opcion == 1:
            Alg_FIFO()
            input("Please press the Enter key to proceed")
        elif opcion == 2:
            Alg_LRU()
            input("Please press the Enter key to proceed")
        elif opcion == 3:
            segunda_oprtunidadReloj()
            input("Please press the Enter key to proceed")
        elif opcion == 4:
            break

# ========================================= ORDEN DE FUNCIONES =========================================
menu()
print("Tenga un buen dia :)")