from Config.config import images
def MTC_SURSGE_001_steps(sge_funct, data):

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
    sge_funct.send_text('15')
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 Presionar la combinacion de teclas: Ctrl + n")
    sge_funct.press_hotkeys('ctrl+n')
    print("11 Leer archivo dso.json para capturar la clave del almacen")
    sge_funct.send_text(data["almacen"])
    print("12 Teclear input")
    sge_funct.press_enter()
    print("13 Leer archivo dso.json para capturar la clave DSO")
    sge_funct.send_text(data["clave_DSO"])
    print("14 Teclear input")
    sge_funct.press_enter()
    print("15 Leer archivo dso.json para capturar la descripción")
    sge_funct.send_text(data["descripcion"])
    print("16 Teclear input")
    sge_funct.press_enter()
    print("17 Presionar la combinacion de teclas: Ctrl + w")
    sge_funct.press_hotkeys('ctrl+w')
