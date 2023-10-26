#calcular la suma de los digitos de un numero
numero=12345
suma=0
for digito in str(numero):
    suma+=int(digito)
print("La suma de los dijitos de",numero,"es", suma)