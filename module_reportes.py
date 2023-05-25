#importaciones
import module_administrativo
import limpiar_consola
import random
import time
#esta funcion esta para los reportes generales 

def reporte_usuarios():
    pass

def reporte_productos():
    pass

def reporte_fechas():
    pass

def reporte_desarrolladores():
    pass



def menu_reportes():
    while(True):
        print("|==============================|")
        print("|**MENU DE REPORTES GENERALES**|")
        print("|==============================|")
        print("                                ")
        print("|1. Consultas por usuarios     |")
        print("|2. Consultas por productos    |")
        print("|3. Consultas por fechas       |")
        print("|4. Consultas por lideres      |")
        print("|5. Cerrar sesion              |")
        print("|==============================|")
        print("\n")
        opcion=int(input("Ingrese la opcion a la cual se quiere dirigir: "))
        limpiar_consola.system_clear_function()
        if(opcion>5):
            print("Ocurrio un error")
            limpiar_consola.system_clear_function()
            return menu_reportes()
        if (opcion==1):
               pass
        elif (opcion==2):
               pass
        elif (opcion==3):
               pass
        elif (opcion==4):
               pass
        elif(opcion==5):
            for i in reversed(range(1,2)):
                print(f"redirigiendo al sistema de votación...{i}")
                time.sleep(1)
            print(f"Saliendo del sistema...{i}")
            limpiar_consola.system_clear_function()
            return module_administrativo.menu_administrativo()
        else:
               print("Ocurrio un error")
               exit()
