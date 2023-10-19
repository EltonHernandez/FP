import os
os.system("cls")

codigo = int( input("codigo : "))
unidades = int( input("unidades : "))

if codigo == 101 : precio = 17
elif codigo == 102 : precio = 25
elif codigo == 103 : precio = 16
elif codigo == 104 : precio = 27
else : precio = 0 

if precio > 0 :
    compra = unidades * precio
    if 1 <= unidades <= 10 : descuento = 0.05
    elif 11 <= unidades <= 20 : descuento = 0.08
    elif unidades >= 31 : descuento = 0.13
    descuento *= compra # descuento = descuento 

    print( f"Precio    = {precio:.2f}" )
    print( f"Compra    = {compra:.2f}" )
    print( f"Descuento = {descuento:.2f}" )
    print( f"Total     = {(compra - descuento):.2f}")