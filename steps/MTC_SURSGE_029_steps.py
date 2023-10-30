


def precondicion_mtc_SURSGE_028(sge_funct, img_utilerias_menu):

    print("step 1 En la pantalla sucursales Ingresar mm")
    sge_funct.activar_menu_mods()
    sge_funct.segundos_de_espera(1)
    assert sge_funct.validate_image_x(img_utilerias_menu), "No se ingreso en pantalla de MOD's"
    print("2 Teclear input")
    sge_funct.send_text('02')
    sge_funct.press_enter()
    print("31 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text('12')
    sge_funct.validar_sucursal_12_seleccionada()
    sge_funct.press_enter()
    print("4 Capturar b")
    sge_funct.send_text('b')
    sge_funct.press_tab()
    print("5 capturar almacen")
    sge_funct.send_text('01')
    sge_funct.press_enter()
    print("5 capturar linea")
    sge_funct.send_text('31')
    sge_funct.press_enter()
    print("6 teclear barra espacio 19 veces")
    for i in range(19):
        sge_funct.press_space()
    print("7 flecha izquierda 19 veces")
    for i in range(19):
        sge_funct.flecha_izquierda()
    print("8 capturar codigo")
    sge_funct.send_text('1000')
    sge_funct.press_enter()
    print("9 capturar m")
    sge_funct.send_text('m')
    print("10 capturar d16")
    sge_funct.send_text('d16')
    print("11 capturar 1.0000")
    sge_funct.send_text('1.0000')
    sge_funct.press_enter()
    print("12 capturar 99")
    sge_funct.send_text('99')
    sge_funct.press_enter()
    print("13 presionar 't' para terminar")
    sge_funct.send_text('t')
    sge_funct.segundos_de_espera(1)
    sge_funct.press_hotkeys('ctrl+a')
    assert sge_funct.validate_image_x(img_utilerias_menu), "No se ingreso en pantalla de MOD's"
    sge_funct.press_hotkeys('ctrl+a')
    sge_funct.press_hotkeys('ctrl+a')


def MTC_SURSGE_029_steps(sge_funct, data, img_valeInterno):

    print("2 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text(data["sucursal_origen"])
    sge_funct.validar_sucursal_seleccionada(data["sucursal_origen"])
    print("3 Teclear input")
    sge_funct.press_enter()
    print("4 Teclear input")
    sge_funct.send_text('2')
    print("5 Teclear input")
    sge_funct.press_enter()
    print("6 Seleccionar <<OPCION MENU>>")
    sge_funct.send_text('4')
    print("7 Teclear input ")
    sge_funct.press_enter()
    print("8 Seleccionar <<OPCION MENU>>")
    sge_funct.send_text('3')
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 Teclear input")
    sge_funct.send_text(data["sucursal_destino"])
    print("11 Teclear input")
    sge_funct.press_enter()
    print("12 Teclear input")
    sge_funct.press_enter()
    print("13 Teclear input")
    sge_funct.press_enter()
    print("14 Teclear input")
    sge_funct.press_enter()
    print("15 Teclear input")
    sge_funct.press_enter()
    print("16 Flecha abajo para posicionarnos en el tipo de traspaso urgente")
    sge_funct.flecha_abajo()
    print("17 Teclear input")
    sge_funct.press_enter()
    print(" Presionar la combinacion de teclas: Ctrl + w")
    sge_funct.press_hotkeys('ctrl+w')
    print("18 Leer archivo devolucion.json para capturar la linea del producto (LINEA 31) EJEMPLO")
    sge_funct.send_text(data["linea"])
    print("19 Teclear input")
    sge_funct.press_enter()
    print("20 Leer archivo devolucion.json para capturar el codigo del producto (CODIGO 1000) EJEMPLO")
    sge_funct.send_text(data["codigo"])
    print("21 Teclear input")
    sge_funct.press_enter()
    print("22 Leer archivo devolucion.json para capturar la cantidad")
    sge_funct.send_text(data["cantidad_a_mover"])
    print("23 Teclear input")
    sge_funct.press_enter()
    print("24 Teclear input")
    sge_funct.press_enter()
    print("25 Presionar la combinacion de teclas: Ctrl + w")
    sge_funct.press_hotkeys('ctrl+w')
    sge_funct.segundos_de_espera(1)
    print("26 Guardar el Vale Interno dando doble clic en el Vale")
    vale_interno = sge_funct.doubleclick_axis_y(img_valeInterno,20)
    print("----------------------------")
    print(vale_interno)
    print("----------------------------")
    print("27 Presionar ctrl + A para regresar al menu")
    sge_funct.press_hotkeys('ctrl+a')
    print("28 Presionar ctrl + A para regresar al menu")
    sge_funct.press_hotkeys('ctrl+a')
    print("29 Presionar ctrl + A para regresar al menu")
    sge_funct.press_hotkeys('ctrl+a')
    print("30 Presionar ctrl + A para regresar al menu")
    sge_funct.press_hotkeys('ctrl+a')
    print("31 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text(data["sucursal_destino"])
    sge_funct.validar_sucursal_seleccionada(data["sucursal_destino"])
    print("32 Teclear input")
    sge_funct.press_enter()
    print("33 Teclear input")
    sge_funct.send_text('2')
    print("34 Teclear input")
    sge_funct.press_enter()
    print("35 Teclear input")
    sge_funct.send_text('4')
    print("36 Teclear input")
    sge_funct.press_enter()
    print("37 Teclear input")
    sge_funct.send_text('4')
    print("38 Teclear input")
    sge_funct.press_enter()
    print("39 Situarse en el campo vale interno e ingresar el numero del Vale Interno.")
    sge_funct.send_text(vale_interno)
    print("40 Teclear input")
    sge_funct.press_enter()
    print("41 Teclear input")
    sge_funct.press_enter()
    print("42 Escribimos quien recibe la mercancia")
    sge_funct.send_text(data["nombre_recibe"])
    print("43 Teclear input")
    sge_funct.press_enter()
    print("44 Escribimos un comentario de recepcion")
    sge_funct.send_text(data["comentario_recepcion"])
    print("45 Teclear input")
    sge_funct.press_enter()
    print("46 Presionar la combinacion de teclas: Ctrl + w")
    sge_funct.press_hotkeys('ctrl+w')
    print("47 Teclear input")
    sge_funct.press_enter()
    print("48 Teclear input")
    sge_funct.press_enter()
    print("49 Presionar la combinacion de teclas: Ctrl + w")
    sge_funct.press_hotkeys('ctrl+w')
    print("50 Teclear input")
    sge_funct.send_text('s')
    print("51 Teclear input")
    sge_funct.press_enter()
    print("52 Presionar la combinacion de teclas: Ctrl + w")
    sge_funct.press_hotkeys('ctrl+w')
    print("53 Ingresar en Login el <<Usuario Almacen>>")
    sge_funct.send_text(data["usuario_almacen"])
    sge_funct.press_enter()