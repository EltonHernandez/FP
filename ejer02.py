#calcular el factorial de un numero
n=5
factorial=1
for i in range(1,n+1):
    factorial *=i
print("El factorial de ",n,"es", factorial)