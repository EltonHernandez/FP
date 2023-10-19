import os
os.system("cls")

n1 = int( input("Número 1 : ") )
n2 = int( input("Número 2 : ") )
n3 = int( input("Número 3 : ") )
n4 = int( input("Número 4 : ") )
n5 = int( input("Número 5 : ") )

     
lista = list((n1,n2,n3,n4,n5))
lista.sort()
promedio = (n1 + n2 + n3 + n4 + n5 - lista[0] - lista[1] ) / 3

print( f"Promedio : {promedio:.2f}" )
print( f"Número Máximo : {lista[4]}" ) # max(n1,n2,n3,n4,n5)
print( f"Número Mínimo : {lista[0]}" ) # min(n1,n2,n3,n4,n5)
print()