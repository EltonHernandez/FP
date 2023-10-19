import math
import os
os.system("cls")

radio = int( input("Radio : ") )
altura = int( input("Altura : ") )

area = 2 * math.pi * radio * ( radio + altura )
volumen = math.pi * math.pow(radio,2) * altura

print( f"Área    : {area:.2f}" )
print( f"Volúmen : {volumen:.2f}" )
print()