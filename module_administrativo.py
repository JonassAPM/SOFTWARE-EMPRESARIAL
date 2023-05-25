from os import system 
import os 
import getpass
import limpiar_consola


def menu_principal():
    print("==============================")
    print("============LOGIN=============")
    print("                              ")
    print("1.    ADMINISTRATIVO          ")
    print("2.    LIDER DESARROLLADOR     ")
    print("==============================")
    print("")
    while True:
        try:
            opcion=int(input("Por favor inicia sesion con tu rol asignado: "))
            limpiar_consola.system_clear_function()
        except:
            print("No se permiten letras")
            continue
        else:
            break
    if (opcion>3):
        print("Rango no permitido dentro del menu: ")
    if  (opcion== 1):
            presidente = ["juan","1234"]
            if print ("") or input("ingrese su usuario: ").lower() != presidente[0] or  getpass.getpass("ingrese su contraseña: ") != presidente[1] or print("sesion iniciada correctamente")or limpiar_consola.system_clear_function() or menu_administrativo():
                print("error datos incorrectos") or quit()




def menu_administrativo():
     #en este menu estara convexas todos los items de presidente
     while(True):
          print("=======================================")
          print("|**Bienvenido al menu administrativo**|")
          print("=======================================")
          print("                                       ")
          print("1. Reportes generales                  ")
          print("2. Ingreso de vacantes                 ")
          print("3. Informacion trabajadores            ")
          print("4. Cerrar sesion                       ")
          print("                                       ")
          print("=======================================")
          print("\n")
          opcion=int(input("Ingresa la opcion la cual desea realizar:"))
          limpiar_consola.system_clear_function()
          if(opcion>4):
               print("Ocurrio un error")
               limpiar_consola.system_clear_function()
               return menu_administrativo()
          if (opcion==1):
               pass
          elif (opcion==2):
               pass
          elif (opcion==3):
               pass
          elif (opcion==4):
               return menu_administrativo()
          else:
               print("Ocurrio un error")
               exit()