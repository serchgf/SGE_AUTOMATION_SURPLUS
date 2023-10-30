from Config.config import images


def MTC_SURSGE_007_steps(sge_funct, data):

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
    sge_funct.send_text('14')
    print("9 Teclear input")
    sge_funct.press_enter()
    print("10 Presionar la combinacion de teclas: Ctrl + n")
    sge_funct.press_hotkeys('ctrl+n')
    print("11 Leer archivo workzone.json para capturar la clave del almacen")
    sge_funct.send_text(data["almacen"])
    print("12 Teclear input")
    sge_funct.press_enter()
    print("13 Capturar p")
    sge_funct.send_text('p')
    print("14 Leer archivo workzone.json para capturar localizacion que tenga pasillo, bahía y nivel referente a una work zone ya creada")
    sge_funct.send_text(data["localizacion"])
    #Se agrega un enter
    print("Teclear input")
    sge_funct.press_enter()
    print("15 Presionar la combinacion de teclas: Ctrl + w para guardar")
    sge_funct.press_hotkeys('ctrl+w')





