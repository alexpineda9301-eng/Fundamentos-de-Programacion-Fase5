# Matriz con los datos de los productos
inventario = [
    [101, "Mouse", 3, 10],
    [102, "Teclado", 12, 8],
    [103, "Cable HDMI", 2, 6],
    [104, "Memoria USB", 15, 10],
    [105, "Adaptador USB", 1, 5]
]


# Funcion para revisar el inventario
def revisar_inventario(inventario):
    print("===== CONTROL DE INVENTARIO =====")
    print()

    # Recorrer los productos de la matriz
    for articulo in inventario:
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Verificar si el stock es insuficiente
        if stock_actual < stock_minimo:
            cantidad_pedir = stock_minimo - stock_actual
        else:
            cantidad_pedir = 0

        # Mostrar informacion del producto
        print("Producto:", articulo[1])
        print("Stock actual:", stock_actual)
        print("Stock minimo:", stock_minimo)

        # Mostrar el resultado de la revision
        if cantidad_pedir > 0:
            print("Se deben pedir:", cantidad_pedir, "unidades")
        else:
            print("Stock suficiente, no se requiere pedido.")

        print("-------------------------------")


# Menu principal del programa
while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Revisar inventario")
    print("2. Salir")

    opcion = input("Seleccione una opcion: ")

    # Ejecutar la revision del inventario
    if opcion == "1":
        revisar_inventario(inventario)

    # Finalizar el programa
    elif opcion == "2":
        print("Programa finalizado.")
        break

    # Validar opciones incorrectas
    else:
        print("Opcion no valida. Intente nuevamente.")