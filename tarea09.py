#Calcular el precio de venta de un artículo. Utilizar precio de costo y porcentaje de ganancia.

producto = int( input("producto : "))
unidades = int( input("unidades : "))

producto  == 101 : precio = 17
elif producto == 102 : precio = 25
elif producto == 103 : precio = 16
elif producto == 104 : precio = 27
else : precio = 0 

if precio > 0 :
    compra = unidades * precio
    if 1 <= unidades <= 10 : ganancia = 0.30
    elif 11 <= unidades <= 20 : ganancia = 0.30
    elif unidades >= 31 : ganancia = 0.30
    ganancia *= compra #descuento = descuento

    print( f"Precio    = {precio:.2f}" )
    print( f"Compra    = {compra:.2f}" )
    print( f"ganancia = {ganancia:.2f}" )
    print( f"Total     = {(compra + ganancia):.2f}")