PRECIO_COMPUTADOR_ESCRITORIO = 800
PRECIO_COMPUTADOR_MESA = 600
PRECIO_TABLETA = 400
PRECIO_VIDEOBEAM = 1000
PRECIO_TELEVISOR = 1200


cantidad_computador_escritorio = 0
cantidad_computador_mesa = 0
cantidad_tableta = 0
cantidad_videobeam = 0
cantidad_televisor = 0

while True:
    print("\nPRODUCTOS DISPONIBLES:")
    print("1. Computador de escritorio")
    print("2. Computador de mesa")
    print("3. Tableta")
    print("4. Videobeam")
    print("5. Televisor")
    print("6. Facturar")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        cantidad_computador_escritorio += 1
    elif opcion == 2:
        cantidad_computador_mesa += 1
    elif opcion == 3:
        cantidad_tableta += 1
    elif opcion == 4:
        cantidad_videobeam += 1
    elif opcion == 5:
        cantidad_televisor += 1
    elif opcion == 6:
        total_pagar = (cantidad_computador_escritorio * PRECIO_COMPUTADOR_ESCRITORIO +
                       cantidad_computador_mesa * PRECIO_COMPUTADOR_MESA +
                       cantidad_tableta * PRECIO_TABLETA +
                       cantidad_videobeam * PRECIO_VIDEOBEAM +
                       cantidad_televisor * PRECIO_TELEVISOR)
        print("\nRESUMEN DE COMPRA:")
        print("Computadores de escritorio:", cantidad_computador_escritorio)
        print("Computadores de mesa:", cantidad_computador_mesa)
        print("Tabletas:", cantidad_tableta)
        print("Videobeams:", cantidad_videobeam)
        print("Televisores:", cantidad_televisor)
        print("Total a pagar:", total_pagar)
        break
