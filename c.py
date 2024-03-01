codigint = int(input("codigo"))
nombreStr = input("nombre")
existenciasint = 0 
controlBln =  True 
import os 
while controlBln  ==True:
    os.system("cls")
    print ("codigo: ", codigint, "\nNombre.", nombreStr, "\nExistencias:",existenciasint)
    opcionStr = int(input("1. compras\n2. ventas\n3. reportes \n--->"))
    cantidadInt = int(input("cantidad: "))
    if opcionStr == "1":
        existenciasint += cantidadInt
    if opcionStr == "2":
        if cantidadInt <=  existenciasint:
          existenciasint -= cantidadInt
    else: 
        print("no hay suficientes existencias ")
    enter =input ("<ENTER>")
    if opcionStr == "3":
        print("cantidad de actual existencias:",existenciasInt)
    if opcionStr == "4":
        controlBln = False
