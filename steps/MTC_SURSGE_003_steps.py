from Config.config import images


def MTC_SURSGE_003_steps(sge_funct, data):

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
    print("8 Teclear input")
    sge_funct.send_text('8')
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 Presionamos ctrl + f ")
    sge_funct.press_hotkeys('ctrl+f')
    print("11 Capturar a para dar de alta una zona")
    sge_funct.send_text('a')
    print("12 Leer archivo zona.json para capturar el Cedi")
    sge_funct.send_text(data["sucursal"])
    print("13 Teclear input")
    sge_funct.press_enter()
    print("14 Leer archivo zona.json para capturar el almacen")
    sge_funct.send_text(data["almacen"])
    print("15 Teclear input")
    sge_funct.press_enter()
    print("16 Leer archivo zona.json para capturar la zona")
    sge_funct.send_text(data["zona"])
    print("17 Teclear input")
    sge_funct.press_enter()
    print("18 Leer archivo zona.json para capturar la descripcion de la zona")
    sge_funct.send_text(data["zona_descripcion"])
    print("19 Teclear input")
    sge_funct.press_enter()
    print("20 Leer archivo zona.json para capturar DSO")
    sge_funct.send_text(data["dso"])