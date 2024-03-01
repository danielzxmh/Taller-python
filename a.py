cantidadint = int(input("cantidad de numeros: "))
contadorint = 1 
contadornumerosInt = 0 
while contadorint <= cantidadint: 
    numeroint = int(input("ingrese un numero "))
    if numeroint >= 10 and numeroint <= 20:
        contadornumerosInt  += 1
    contadorint += 1

print("la cantidad de numerosde 10 a 20 son:   ",contadornumerosInt)
