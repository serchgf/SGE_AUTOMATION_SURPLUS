from Config.config import images


def MTC_SURSGE_016_steps(sge_funct, archivo_cm_Relleno_localizacion_permanente_a_multiple_masiva):
    # esta funcion recibe como parametro una instancia de la clase SGE functions y un archivo co los productos
    print("Ingresar uu (cambiar usuario) ")
    sge_funct.activar_cambio_usuario()
    print("Ingresar el usuario sfabian0")
    sge_funct.send_text("sfabian0")
    print("Press Enter")
    sge_funct.press_enter()
    print("Ingresar numero de sucursal ")
    sge_funct.send_text('12')
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("3 Press Enter")
    sge_funct.press_enter()
    print("4 Teclear input 2")
    sge_funct.send_text('2')
    print("5 Teclear input Enter")
    sge_funct.press_enter()
    print("6 Teclear input 9")
    sge_funct.send_text('9')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    print("6 Teclear input 13")
    sge_funct.send_text('13')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    print("10 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("11 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_Relleno_localizacion_permanente_a_multiple_masiva)
    sge_funct.segundos_de_espera(3)
    print("13 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos Enter para cambiar al campo password de sfabian0 ")
    sge_funct.send_text('sfabian0')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
