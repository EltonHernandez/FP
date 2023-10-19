import os
os.system("cls")

numero = int(input("Número: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3: 
    print("Miércoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("viernes")
elif numero == 6:
    print("Sábado")
elif numero == 7: 
    print("Domingo")
else:
    print("El dia no existe")

aDias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sabado","Domingo"]
if numero >= 1 and numero <= 7:
    print( aDias[numero - 1])
else : print("Error")