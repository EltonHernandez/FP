"""Imprimir los numeros pares enun rango especifico 
"""
inicio=1
fin=20
for numero in range(inicio,fin+1):
    if numero % 2==0:
        print(numero)