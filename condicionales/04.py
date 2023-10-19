import os
os.system("cls")

grados = int(input("Grados : ")) 

if grados == 0:
    print("Nulo")
elif 0 < grados < 90 :
    print("Agudo")
elif grados == 90 :
    print("Recto")
elif 90 < grados < 180 :
    print("Obtuso")
elif grados == 180 :
    print("Llano")
elif 180 < grados < 360 :
    print("Cóncavo")
elif grados == 360 :
    print("Completo")
else:
    print("Error")