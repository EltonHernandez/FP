#sumar los numeros enteros positivos hasta un limite 
limite=10
suma=0 #acumulador
n=1 #contador
while n<=limite:
    suma+=n #acumulando los valores de n
    n+=1 #incrementando el contador
print("La suma de los numeros del 1 hasta ",limite,"es", suma)