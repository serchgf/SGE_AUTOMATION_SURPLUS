from Config.config import images


def MTC_SURSGE_011_steps(sge_funct, data):

    print("2 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text(data["sucursal"])
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("3 Teclear input")
    sge_funct.press_enter()
    print("4 Teclear input")
    sge_funct.send_text('2')
    print("5 Teclear input")
    sge_funct.press_enter()
    print("6 Teclear input")
    sge_funct.send_text('9')
    print("7 Teclear input")
    sge_funct.press_enter()
    print("8 Capturar la opcion Captura de localizaciones")
    sge_funct.send_text('8')
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 Leer archivo producto_localizacion.json para capturar la clave del almacen")
    sge_funct.send_text(data["almacen"])
    print("11 Teclear input")
    sge_funct.press_enter()
    print("12 Leer archivo producto_localizacion.json para capturar la linea del producto")
    sge_funct.send_text(data["linea"])
    print("13 Teclear input")
    sge_funct.press_enter()
    print("14 Leer archivo producto_localizacion.json para capturar el codigo del producto")
    sge_funct.send_text(data["codigo"])
    print("15 Teclear input")
    sge_funct.press_enter()
    print("16 Teclear input")
    sge_funct.press_enter()
    print("17 Capturar la opcion 1 Localizaciones y Limites")
    sge_funct.send_text('1')
    print("18 Leer archivo producto_localizacion.json para capturar la localizacion")
    sge_funct.send_text(data["localizacion"])
    print("19 Teclear input")
    sge_funct.press_enter()
    print("20 Leer archivo producto_localizacion.json para capturar el minimo")
    sge_funct.send_text(data["minimo"])
    print("21 Teclear input")
    sge_funct.press_enter()
    print("22 Leer archivo producto_localizacion.json para capturar el maximo")
    sge_funct.send_text(data["maximo"])
    print("23 Teclear input")
    sge_funct.press_enter()
    print("24 Presionar la combinacion de teclas: Ctrl + a para terminar")
    sge_funct.press_hotkeys('ctrl+a')







