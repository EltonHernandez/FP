#calcular el promedio de una lista de numeros
#ingresados por consola.
total=0
contador=0
while True: #mientras sea verdad
    numero=input("ingrese un numero o fin para terminar: ")
    if numero.lower()=='fin':#lower convierte a minusculas
        break #termina el ciclo while
    total+=float(numero)
    contador+=1
if contador>0:# si contador es mayor a 0 se obtiene el promedio
    promedio=total/contador 
    print("El promedio es:", promedio)
else:
    print("No se ingresaron numeros,")