from os import system 
import os 
import getpass
system("clear")

def menu_principal():
    print("==============================")
    print("============LOGIN=============")
    print(" ")
    print("1.    ADMINISTRATIVOS         ")
    print("2.    LIDER DESARROLLADOR     ")
    print("==============================")
    print("")
    while True:
        try:
            opcion=int(input("Por favor inicia sesion con tu rol asignado: "))
            os.system("clear")
        except:
            print("No se permiten letras")
            continue
        else:
            break
    if (opcion>3):
        print("Rango no permitido dentro del menu: ")
    if  (opcion== 1):
        print("=====================")
        print("        LOGIN        ")
        print("                     ")
        print("1.   PRESIDENTE      ")
        print("2.   VICEPRESIDENTE  ")
        print("                     ")
        print("=====================")
        opcion=int(input("Por favor identificate: "))
        if (opcion>2):
            print("su seleccion no se encuentra dentro del rango permitido")
            print(" ")
        if (opcion == 1):
            presidente = ["juan","1234"]
            if print ("") or input("ingrese su usuario: ").lower() != presidente[0] or  getpass.getpass("ingrese su contraseña: ") != presidente[1] or print("sesion iniciada correctamente"):
                print("error datos incorrectos") or quit()
        if (opcion == 2):
            vicepresidente = ["didier","1435"]
            if print ("") or input("ingrese su usuario: ").lower() != vicepresidente[0] or getpass.getpass("ingrese su contraseña: ") != vicepresidente[1] or print("sesion iniciada correctamente"):
                print("error datos incorrectos") or quit()
    elif (opcion==2):
        lideres= ["kevin", "3322","jhon","1540"]
        if input("ingrese su usarios asignado: ").lower() != lideres[0 and 2]  or input("ingrese su contraseña asignada: ").lower() != lideres[1 and 3] or print("sesion iniciada correctamente"):
            print("error datos incorrectos") or quit()