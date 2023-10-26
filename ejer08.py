
inicio = 1

nombre_articulo = input("Nombre del artículo que se vende: ")
if nombre_articulo in nombres:
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad_vendida = 0.0
    nombres.append(teclado)
    precios.append(50)
    cantidades_vendidas.append(cantidad_vendida)
    cantidad = float(input("Cantidad vendida: "))
    indice = nombres.index(nombre_articulo)
    precio = precios[indice]
    cantidades_vendidas[indice] += cantidad
    print(
        f"Se vende(n) {cantidad} {nombre_articulo}. Total: {cantidad * precio}")
else:
    print("El artículo no existe")
    