def MTC_SURSGE_023_steps(sge_funct, data, img_inicioFactura):

    print("2 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text(data["sucursal_origen"])
    sge_funct.validar_sucursal_seleccionada(data["sucursal_origen"])
    print("3 Teclear input")
    sge_funct.press_enter()
    print("4 Teclear input")
    sge_funct.send_text('4')
    print("5 Teclear input")
    sge_funct.press_enter()
    print("6 Teclear input")
    sge_funct.send_text('10')
    print("7 Teclear input")
    sge_funct.press_enter()
    print("8 Posicionarse en campo cuenta y capturar la cuenta 45820263")
    sge_funct.send_text(data["cuenta"])
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 Teclear input")
    sge_funct.press_enter()
    print("11 Teclear input")
    sge_funct.press_enter()
    print("12 Teclear input")
    sge_funct.press_enter()
    print("13 Presionar ctrl + W para pasar al detalle del pedido")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(1)
    print("14 Aparece mensaje de promociones o advertencias de la cuenta")
    while sge_funct.promociones_y_atrasos():
        sge_funct.press_hotkeys('ctrl+a')
    print("15 Posicionarse en Columna Linea y presionar la combinacion de teclas ctrl + E")
    sge_funct.press_hotkeys('ctrl+e')
    print("16 Ingresar la línea del producto")
    sge_funct.send_text(data["linea"])
    print("17 Teclear input")
    sge_funct.press_enter()
    print("18 Escribimos el codigo 1000")
    sge_funct.send_text(data["codigo"])
    print("19 Teclear input")
    sge_funct.press_enter()
    print("20 Presionamos Enter hasta posicionarnos en la columna cantidad y capturamos N unidades.")
    sge_funct.press_enter()
    print("21 Teclear input")
    sge_funct.press_enter()
    print("22 Teclear input")
    sge_funct.press_enter()
    print("23 Ingresar la cantidad de producto")
    sge_funct.send_text(data["cantidad"])
    print("24 Teclear input")
    sge_funct.press_enter()
    print("25 Presionamos ctrl + W para facturar lo capturado en la ventada del detalle esperar 5 segundos")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(5)
    print("26 Presionamos Enter para continuar ")
    sge_funct.press_enter()
    print("27 Guardar la factura para la devolución")
    folio_factura = sge_funct.doubleClick(img_inicioFactura)
    print("28 Teclear input")
    sge_funct.press_enter()
    print("29 Presionar ctrl + A para regresar al menu")
    sge_funct.press_hotkeys('ctrl+a')
    print("30 Teclear input")
    sge_funct.send_text('13')
    print("31 Teclear input")
    sge_funct.press_enter()
    print("32 Capturar la opcion Captura de localizaciones")
    sge_funct.send_text('1')
    print("33 Teclear input")
    sge_funct.press_enter()
    print("34 Oprimir click derecho del mouse para Pegar la factura previamente generada ")
    sge_funct.send_text(folio_factura)
    print("35 Teclear input")
    sge_funct.press_enter()
    print("36 Teclear input")
    sge_funct.press_enter()
    print("37 Presionar la combinacion de teclas: Ctrl + V")
    sge_funct.press_hotkeys('ctrl+v')
    print("38 Teclear input")
    sge_funct.press_enter()
    print("39 Teclear input")
    sge_funct.send_text('2')
    print("40 Teclear input")
    sge_funct.press_enter()
    print("41 Presionar la combinacion de teclas: Ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("42 Teclear input ")
    sge_funct.send_text('s')
    print("43 Teclear input")
    sge_funct.press_enter()
    print("44 Presionar la combinacion de teclas: Ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("45 Teclear input")
    sge_funct.press_enter()
    print("46 Teclear input")
    sge_funct.press_enter()
    print("47 Teclear input")
    sge_funct.press_enter()
